#!/usr/bin/env python3
"""
Auto-generates 5 travel articles per day for nz-family-travel.
Uses Groq API for content, affiliate links from site data.
Run daily via systemd timer or cron.

Usage:
  python3 scripts/auto_generate.py            # generate today's 5 posts
  python3 scripts/auto_generate.py --dry-run  # preview topics only
  python3 scripts/auto_generate.py --rebuild  # rebuild + push only
"""

import json
import os
import re
import sys
import subprocess
import hashlib
import argparse
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

# Load .env
env_file = ROOT / '.env'
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip(), v.strip())

from groq import Groq

GROQ_MODEL = "llama-3.3-70b-versatile"
client = Groq(api_key=os.environ['GROQ_API_KEY'])

# ── Load site data ────────────────────────────────────────────────────────────

def load_data():
    dests    = json.loads((ROOT / 'data/destinations.json').read_text())
    acts     = json.loads((ROOT / 'data/activities.json').read_text())
    site     = json.loads((ROOT / 'data/site.json').read_text())
    deals    = json.loads((ROOT / 'data/deals.json').read_text())
    return dests, acts, site, deals

# ── Topic pool ────────────────────────────────────────────────────────────────

ARTICLE_TYPES = [
    'deals',
    'month_guide',
    'budget',
    'activity_review',
    'hidden_gems',
    'age_guide',
    'comparison',
]

MONTHS = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']

AGE_GROUPS = ['toddlers (1–4)', 'kids aged 5–8', 'tweens (9–12)', 'teenagers']

def build_typed_pools(dests, acts):
    """Build separate pools per article type for balanced daily selection."""
    pools = {t: [] for t in ARTICLE_TYPES}
    for d in dests:
        for atype in ARTICLE_TYPES:
            if atype == 'activity_review':
                continue
            pools[atype].append({'type': atype, 'dest': d})
    for a in acts:
        pools['activity_review'].append({'type': 'activity_review', 'activity': a})
    # Comparison pairs
    for i, d1 in enumerate(dests):
        for d2 in dests[i+1:]:
            pools['comparison'].append({'type': 'comparison', 'dest1': d1, 'dest2': d2})
    return pools

def pick_todays_topics(pools, n=5):
    """Pick 1 topic per article type — guaranteed variety each day.
    Uses date seed for deterministic, day-to-day rotation through each type's pool.
    """
    today_str = date.today().isoformat()
    day_num = (date.today() - date(2026, 1, 1)).days  # days since epoch start

    # Daily rotation: cycle through types, pick one from each type's pool
    type_order = ARTICLE_TYPES * 10  # enough to fill n slots
    topics = []
    used_types = set()

    for atype in type_order:
        if len(topics) >= n:
            break
        if atype in used_types:
            continue
        pool = pools.get(atype, [])
        if not pool:
            continue
        # Pick deterministically from this type's pool using day_num
        seed = int(hashlib.md5(f"{today_str}:{atype}".encode()).hexdigest(), 16)
        idx = seed % len(pool)
        topics.append(pool[idx])
        used_types.add(atype)

    return topics

def already_generated(slug):
    return (ROOT / 'content/posts' / f'{slug}.json').exists()

# ── Slug helpers ─────────────────────────────────────────────────────────────

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def topic_slug(topic):
    today = date.today().strftime('%Y-%m')
    if topic['type'] == 'deals':
        return f"{topic['dest']['slug']}-family-deals-{today}"
    elif topic['type'] == 'month_guide':
        month = MONTHS[date.today().month - 1]
        return f"{topic['dest']['slug']}-{month.lower()}-family-guide"
    elif topic['type'] == 'budget':
        return f"{topic['dest']['slug']}-budget-family-guide-{today}"
    elif topic['type'] == 'activity_review':
        if 'activity' in topic:
            return f"{topic['activity']['slug']}-family-review-{today}"
        return f"{topic['dest']['slug']}-top-activities-{today}"
    elif topic['type'] == 'hidden_gems':
        return f"{topic['dest']['slug']}-hidden-gems-families"
    elif topic['type'] == 'age_guide':
        return f"{topic['dest']['slug']}-with-young-kids-guide"
    elif topic['type'] == 'comparison':
        return f"{topic['dest1']['slug']}-vs-{topic['dest2']['slug']}-families"
    return f"nz-family-travel-{today}"

# ── Prompt builders ───────────────────────────────────────────────────────────

def _to_str(item):
    """Convert a list item that may be a string or dict to a plain string."""
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        return item.get('name', item.get('title', str(item)))
    return str(item)

def dest_context(dest):
    qf = dest.get('quick_facts', {})
    acts = ', '.join(_to_str(a) for a in dest.get('top_activities', [])[:5])
    free = ', '.join(_to_str(a) for a in dest.get('free_activities', [])[:3])
    tips = ' '.join(_to_str(t) for t in dest.get('hidden_gems', [])[:2])
    return (
        f"Destination: {dest['name']}, New Zealand.\n"
        f"Tagline: {dest.get('tagline','')}\n"
        f"Budget: {qf.get('budget_family4_per_day','')}/day for a family of 4.\n"
        f"Best ages: {qf.get('best_ages','all ages')}.\n"
        f"Top activities: {acts}.\n"
        f"Free activities: {free}.\n"
        f"Hidden gems: {tips}\n"
        f"Summary: {dest.get('summary','')[:300]}"
    )

def activity_context(act):
    price = act.get('price', {})
    adult = price.get('adult', 0)
    child = price.get('child', 0)
    return (
        f"Activity: {act['name']} in {act.get('destination','').title()}, NZ.\n"
        f"Price: ${adult}/adult, ${child}/child.\n"
        f"Duration: {act.get('duration','2 hours')}.\n"
        f"Min age: {act.get('min_age',3)}+.\n"
        f"Family suitability: {act.get('family_suitability',8)}/10.\n"
        f"Summary: {act.get('summary','')[:300]}"
    )

def deals_context(deals, dest_name):
    items = []
    for d in deals.get('current_deals', []):
        items.append(f"- {d['title']}: {d['description']} ({d['saving']})")
    general = '\n'.join(items[:4])
    return (
        f"Current NZ travel deals relevant to {dest_name}:\n{general}\n"
        f"Main booking affiliate: Bookme.co.nz (up to 40% off activities), "
        f"Discover Cars (campervan hire from $89/day), "
        f"Cover-More travel insurance."
    )

SYSTEM_PROMPT = """You are a friendly, practical NZ family travel writer for nzfamilytravel.co.nz.
Write for NZ parents planning family holidays. Tone: warm, honest, specific, helpful.
Always include real prices, drive times, and age-suitability.
Output valid JSON only — no markdown, no extra text outside the JSON object."""

def build_prompt(topic, deals):
    month = MONTHS[date.today().month - 1]
    year = date.today().year

    if topic['type'] == 'deals':
        dest = topic['dest']
        ctx = dest_context(dest) + '\n\n' + deals_context(deals, dest['name'])
        instruction = (
            f"Write a 'Best Family Deals in {dest['name']} — {month} {year}' article. "
            f"Cover: current booking deals and discounts, best-value activities, "
            f"money-saving tips for families, when to book for best prices. "
            f"Include 5–6 specific money-saving tips. Mention Bookme.co.nz for activity discounts."
        )

    elif topic['type'] == 'month_guide':
        dest = topic['dest']
        ctx = dest_context(dest)
        instruction = (
            f"Write a '{month} in {dest['name']} with Kids' guide for {year}. "
            f"Cover: what the weather is like, what's on, what's best this month, "
            f"what to book ahead, crowd levels, and 4–5 practical tips for families visiting in {month}."
        )

    elif topic['type'] == 'budget':
        dest = topic['dest']
        ctx = dest_context(dest)
        qf = dest.get('quick_facts', {})
        budget = qf.get('budget_family4_per_day', '$200')
        instruction = (
            f"Write a budget guide: 'How to Visit {dest['name']} on a Family Budget'. "
            f"Cover: realistic daily costs (family of 4 around {budget}/day), "
            f"free activities, accommodation options from cheap to mid-range, "
            f"where to save money, what's worth splashing out on. "
            f"Include a rough 3-day budget breakdown table."
        )

    elif topic['type'] == 'activity_review':
        if 'activity' in topic:
            act = topic['activity']
            ctx = activity_context(act)
            instruction = (
                f"Write an honest family review of '{act['name']}'. "
                f"Cover: what it's actually like with kids, age suitability, value for money, "
                f"insider tips, best time to visit, how to book and save money. "
                f"Be honest about any downsides for families."
            )
        else:
            dest = topic['dest']
            ctx = dest_context(dest)
            instruction = (
                f"Write 'Top Family Activities in {dest['name']} — {year} Guide'. "
                f"Cover the 5 best activities with prices, ages, and honest tips. "
                f"Include at least 2 free options. Rate each activity for family value."
            )

    elif topic['type'] == 'hidden_gems':
        dest = topic['dest']
        ctx = dest_context(dest)
        instruction = (
            f"Write 'Hidden Gems in {dest['name']}: What Most NZ Families Miss'. "
            f"Cover 5–6 lesser-known spots, free activities, or insider tips that "
            f"don't appear in mainstream guides. Focus on things families with kids would love "
            f"but wouldn't easily find. Include practical info (how to get there, costs, ages)."
        )

    elif topic['type'] == 'age_guide':
        dest = topic['dest']
        age_group = AGE_GROUPS[date.today().day % len(AGE_GROUPS)]
        ctx = dest_context(dest)
        instruction = (
            f"Write '{dest['name']} with {age_group.title()}: Complete Family Guide'. "
            f"Cover: which activities suit this age group, what to avoid, "
            f"practical tips (sleep, food, pacing), best accommodation type, "
            f"and a sample 2-day itinerary suited to this age group."
        )

    elif topic['type'] == 'comparison':
        d1, d2 = topic['dest1'], topic['dest2']
        ctx = dest_context(d1) + '\n\n' + dest_context(d2)
        instruction = (
            f"Write '{d1['name']} vs {d2['name']}: Which is Better for NZ Families?'. "
            f"Compare on: cost, family activities, ease with young kids, accommodation, "
            f"weather reliability, and a final verdict with a recommendation based on family type. "
            f"Use a comparison table for the key facts."
        )

    else:
        dest = topic['dest']
        ctx = dest_context(dest)
        instruction = f"Write a useful family travel guide for {dest['name']}, New Zealand."

    schema = json.dumps({
        "title": "Full SEO article title (under 70 chars)",
        "short_title": "Short title (under 30 chars)",
        "meta_desc": "SEO meta description (150-160 chars)",
        "intro": "2-3 sentence intro paragraph",
        "reading_time": 6,
        "sections": [
            {
                "heading": "Section heading",
                "body": "2-3 paragraphs of body text (use <p> tags)",
                "list": ["optional bullet points"],
                "table": {
                    "headers": ["Col1", "Col2"],
                    "rows": [["val1", "val2"]]
                }
            }
        ]
    }, indent=2)

    return (
        f"CONTEXT:\n{ctx}\n\n"
        f"TASK: {instruction}\n\n"
        f"OUTPUT: Return a JSON object matching this schema (include 4–6 sections, "
        f"omit 'list' or 'table' keys if not needed for that section):\n{schema}"
    )

# ── Generate one article ──────────────────────────────────────────────────────

def generate_article(topic, deals, slug):
    prompt = build_prompt(topic, deals)
    print(f"  Calling Groq ({GROQ_MODEL})...")

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=3000,
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)

    # Inject guaranteed fields
    data['slug'] = slug
    data['updated'] = date.today().strftime('%B %Y')
    data['auto_generated'] = True
    data['generated_date'] = date.today().isoformat()
    data.setdefault('reading_time', 6)

    # Add affiliate CTA to last section if not present
    last = data['sections'][-1] if data.get('sections') else None
    if last and 'cta' not in last:
        last['cta'] = {
            "text": "Compare campervan prices & book activities",
            "url": "https://www.discovercars.com/",
            "affiliate": True
        }

    return data

# ── Save article ──────────────────────────────────────────────────────────────

def save_article(data):
    slug = data['slug']
    out_path = ROOT / 'content/posts' / f'{slug}.json'
    out_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"  Saved: content/posts/{slug}.json")
    return out_path

# ── Build & push ──────────────────────────────────────────────────────────────

def rebuild_and_push(dry_run=False):
    if dry_run:
        print("[dry-run] Would rebuild and push")
        return
    print("\nRebuilding site...")
    result = subprocess.run(
        ['/usr/bin/python3', 'build.py'],
        cwd=ROOT, capture_output=True, text=True
    )
    if result.returncode != 0:
        print("BUILD ERROR:", result.stderr[-500:])
        return False
    # Count pages
    last_line = [l for l in result.stdout.splitlines() if l.strip()][-1]
    print(f"  {last_line}")

    # Git commit and push
    today = date.today().isoformat()
    subprocess.run(['git', 'add', '-A'], cwd=ROOT)
    commit_msg = f"Auto-generate 5 articles — {today}"
    subprocess.run(['git', 'commit', '-m', commit_msg], cwd=ROOT)
    push = subprocess.run(['git', 'push'], cwd=ROOT, capture_output=True, text=True)
    if push.returncode == 0:
        print("  Pushed to GitHub Pages")
    else:
        print("  Push failed:", push.stderr[:200])
    return True

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Preview topics only')
    parser.add_argument('--rebuild', action='store_true', help='Rebuild + push only')
    parser.add_argument('--force', action='store_true', help='Regenerate even if already done today')
    parser.add_argument('--count', type=int, default=5, help='Number of articles (default 5)')
    args = parser.parse_args()

    dests, acts, site, deals = load_data()

    if args.rebuild:
        rebuild_and_push()
        return

    pools = build_typed_pools(dests, acts)
    topics = pick_todays_topics(pools, n=args.count)

    print(f"\nToday's {len(topics)} articles ({date.today().isoformat()}):\n")
    for i, topic in enumerate(topics, 1):
        slug = topic_slug(topic)
        exists = already_generated(slug)
        status = "EXISTS" if exists else "WILL GENERATE"
        if topic['type'] == 'comparison':
            label = f"{topic['dest1']['name']} vs {topic['dest2']['name']}"
        elif 'dest' in topic:
            label = topic['dest']['name']
        elif 'activity' in topic:
            label = topic['activity']['name']
        else:
            label = '?'
        print(f"  {i}. [{topic['type']:15}] {label:35} — {slug}")
        print(f"     {status}")

    if args.dry_run:
        print("\n[dry-run] No files written.")
        return

    generated = []
    for i, topic in enumerate(topics, 1):
        slug = topic_slug(topic)
        if already_generated(slug) and not args.force:
            print(f"\n[{i}/{len(topics)}] Skipping (already exists): {slug}")
            continue
        print(f"\n[{i}/{len(topics)}] Generating: {slug}")
        try:
            data = generate_article(topic, deals, slug)
            save_article(data)
            generated.append(slug)
        except Exception as e:
            print(f"  ERROR: {e}")

    if generated:
        print(f"\nGenerated {len(generated)} articles.")
        rebuild_and_push()
    else:
        print("\nNothing new to generate today.")

if __name__ == '__main__':
    main()
