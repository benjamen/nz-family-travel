# HEARTBEAT.md — NZ Family Travel

## Daily Task: Generate 1 Post Per Heartbeat Run

**Working directory:** `/home/ben/nz-family-travel/`
**Site URL:** https://nzfamilytravel.co.nz
**GitHub Pages:** push to deploy (`git push`)

---

## STEP 1 — Check daily limit

```bash
bash /home/ben/nz-family-travel/scripts/article-gate.sh
```

- **Exit code 1** → daily limit reached (3 posts today). Write NOTHING. Reply `HEARTBEAT_OK`.
- **Exit code 0** → proceed to Step 2.

---

## STEP 2 — Pick today's topic

Read `content/posts/` to see what's already been written. Avoid duplicates.

Pick **ONE** topic from this rotating priority list (use current date to rotate):

| Day mod 4 | Article type |
|-----------|-------------|
| 0 | **Deals** — current booking deals for a NZ destination |
| 1 | **Hidden gems** — lesser-known spots families miss in a specific NZ location |
| 2 | **Location guide** — "[City] with Kids in [Month]" seasonal guide |
| 3 | **Practical tips** — age group, budget, packing, transport or activity comparison |

**Destinations to rotate through** (pick an uncovered one):
Queenstown, Rotorua, Taupo, Auckland, Christchurch, Wellington, Bay of Islands, Coromandel, Fiordland, Wanaka, Nelson, Marlborough, Hawke's Bay, Mount Maunganui, Northland, Kaikōura, Dunedin, Hamilton, Hanmer Springs, Akaroa, Paihia

**Also valid:** NZ-wide topics (campervans, packing, school holidays, budget tips, age guides)

Current NZ month context: check `date` command for today's month and year.

---

## STEP 3 — Write the article

Write a new JSON file to `content/posts/[slug].json`.

**Required JSON structure:**
```json
{
  "slug": "rotorua-hidden-gems-families",
  "title": "Hidden Gems in Rotorua: What Most NZ Families Miss",
  "short_title": "Rotorua Hidden Gems",
  "meta_desc": "7 hidden gems in Rotorua families love — free hot pools, secret walks, and locals-only spots. All ages, all budgets.",
  "intro": "2–3 sentence intro. Hook the reader.",
  "updated": "May 2026",
  "reading_time": 7,
  "auto_generated": true,
  "generated_date": "2026-05-26",
  "hero_image": {
    "url": "https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=1200&q=80",
    "thumb": "https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=600&q=70",
    "alt": "Rotorua geothermal pools with family",
    "credit": "Unsplash"
  },
  "sections": [
    {
      "heading": "Section heading",
      "body": "<p>Body paragraph 1.</p><p>Body paragraph 2.</p>",
      "list": ["bullet 1", "bullet 2"],
      "cta": {
        "text": "Book Rotorua activities on Bookme →",
        "url": "https://www.bookme.co.nz/results/?where=Rotorua",
        "affiliate": true
      }
    }
  ]
}
```

**Rules:**
- `slug` must be unique — check `content/posts/` first
- Minimum 4 sections, ideally 5–6
- `body` uses `<p>` tags (HTML, not markdown)
- At least one `list` with 4–6 bullet points
- At least one `cta` linking to an affiliate (Bookme, Discover Cars, Booking.com, or Cover-More)
- `hero_image.url` — pick a relevant Unsplash photo ID. Format: `https://images.unsplash.com/photo-{ID}?w=1200&q=80`
  Good NZ photo IDs: `1507699622108-4be3abd695ad` (beach), `1519699047748-de8e457a634e` (Rotorua), `1549887534-1541e9326642` (Queenstown lake), `1558618666-fcd25c85cd64` (campervan), `1464822759023-fed622ff2c3b` (mountains), `1480714378408-67cf0d13bc1b` (Auckland)
- Tone: warm, specific, helpful NZ parent voice. Include real prices, ages, drive times.
- Article must be genuinely useful — not filler. If unsure of a topic, pick a different one.

**Slug format:**
- Deals: `{destination-slug}-family-deals-{YYYY-MM}`
- Hidden gems: `{destination-slug}-hidden-gems-families`
- Location guide: `{destination-slug}-{month}-with-kids`
- Tips: descriptive slug e.g. `nz-family-road-trip-tips-2026`

---

## STEP 4 — Build and deploy

```bash
cd /home/ben/nz-family-travel
.venv/bin/python3 build.py
git add -A
git commit -m "Auto-post: [article title] — $(date +%Y-%m-%d)"
git push
```

Verify build completed with no errors before pushing.

---

## STEP 5 — Done

Reply with: `HEARTBEAT_OK — wrote [slug] ([article type])`

---

## If anything goes wrong

- Build fails → do NOT push. Report the error.
- Duplicate slug → pick a different topic and try again.
- Can't think of a unique uncovered topic → skip this run and reply `HEARTBEAT_OK — no new topic needed`.

---

## Affiliate URLs for CTAs

| Affiliate | URL |
|-----------|-----|
| Bookme (activities) | `https://www.bookme.co.nz/results/?where={City}` |
| Booking.com (accommodation) | `https://www.booking.com/searchresults.html?ss={City}%2C+New+Zealand&group_adults=2&group_children=2` |
| Discover Cars (campervans) | `https://www.discovercars.com/` |
| Cover-More (insurance) | `https://www.covermore.co.nz/` |
| Viator (tours) | `https://www.viator.com/en-NZ/searchResults/all?text={City}+New+Zealand&pid=P00098580` |
