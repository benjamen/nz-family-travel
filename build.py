#!/usr/bin/env python3
"""NZ Family Travel — static site generator."""

import json
import shutil
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus
from jinja2 import Environment, FileSystemLoader

ROOT    = Path(__file__).parent
DATA    = ROOT / "data"
LAYOUTS = ROOT / "layouts"
STATIC  = ROOT / "static"
CONTENT = ROOT / "content"
OUT     = ROOT / "docs"

env = Environment(loader=FileSystemLoader(str(LAYOUTS)), autoescape=False)
env.filters['url_encode'] = quote_plus
env.filters['tojson'] = lambda v: json.dumps(v, ensure_ascii=False)

def _to_iso_date(s):
    for fmt in ('%B %Y', '%b %Y', '%Y-%m-%d', '%d %B %Y'):
        try: return datetime.strptime(str(s), fmt).strftime('%Y-%m-01' if fmt.endswith('%Y') else '%Y-%m-%d')
        except: pass
    return str(s)

env.filters['to_iso_date'] = _to_iso_date


def load(name):
    return json.loads((DATA / f"{name}.json").read_text())


def write(path: Path, html: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html)
    print(f"  {path.relative_to(OUT)}")


def render(template_name, out_path, **ctx):
    t = env.get_template(template_name)
    write(OUT / out_path, t.render(**ctx))


def load_content_dir(subdir):
    """Load all .json files from content/{subdir}/"""
    d = CONTENT / subdir
    if not d.exists():
        return []
    items = []
    for f in sorted(d.glob("*.json")):
        items.append(json.loads(f.read_text()))
    return items


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    if STATIC.exists():
        shutil.copytree(STATIC, OUT / "static")

    # Copy standalone tool HTML pages (e.g. calculators) into docs/tools/<name>/
    tools_src = ROOT / "tools"
    if tools_src.exists():
        for html_file in tools_src.glob("*.html"):
            dest = OUT / "tools" / html_file.stem / "index.html"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(html_file, dest)

    site            = load("site")
    destinations    = load("destinations")
    _required = ("three_day_itinerary", "budget_breakdown", "top_activities", "where_to_stay")
    destinations    = [d for d in destinations if all(d.get(k) for k in _required)]
    activities      = load("activities")
    itineraries     = load("itineraries")
    campervans      = load("campervans")
    media           = load("media")
    cities          = load("cities")
    school_holidays = load("school_holidays")
    weather         = load("weather")
    holiday_parks   = load("holiday_parks")
    guides          = load_content_dir("travel-tips")
    tools           = load_content_dir("tools")
    overseas        = load_content_dir("overseas")
    posts           = load_content_dir("posts")

    # Attach media to destinations and activities
    for dest in destinations:
        dest["media"] = media["destinations"].get(dest["slug"], {})
    for act in activities:
        act["media"] = media["activities"].get(act["slug"], {})

    ctx = dict(
        site=site,
        destinations=destinations,
        activities=activities,
        itineraries=itineraries,
        campervans=campervans,
        cities=cities,
        school_holidays=school_holidays,
        weather=weather,
        holiday_parks=holiday_parks,
        guides=guides,
        tools=tools,
        overseas=overseas,
        posts=posts,
    )

    print("Building pages...")

    # ── Homepage ──────────────────────────────────────────────────────────────
    render("index.html", "index.html", **ctx)

    # ── About page ────────────────────────────────────────────────────────────
    render("about.html", "about/index.html", **ctx)

    # ── Privacy Policy ────────────────────────────────────────────────────────
    render("privacy.html", "privacy/index.html", **ctx)

    # ── School Holidays calendar ───────────────────────────────────────────────
    render("school-holidays.html", "school-holidays/index.html", **ctx)

    # ── Weather by month matrix ────────────────────────────────────────────────
    render("weather.html", "weather/index.html", **ctx)

    # ── Holiday Park Finder ────────────────────────────────────────────────────
    render("holiday-parks.html", "holiday-parks/index.html", **ctx)

    # ── Individual holiday park profile pages ─────────────────────────────────
    import re as _re
    for region in holiday_parks.get("regions", []):
        for park in region.get("parks", []):
            park["region_name"] = region["name"]
            park["region_slug"] = region["slug"]
            if "slug" not in park:
                park["slug"] = _re.sub(r"[^a-z0-9]+", "-", park["name"].lower()).strip("-")
            render("holiday-park.html", f"holiday-parks/{park['slug']}/index.html", park=park, **ctx)

    # ── Destinations hub ──────────────────────────────────────────────────────
    render("hub.html", "destinations/index.html",
           hub_title="NZ Family Travel Destinations",
           hub_subtitle="Honest family travel guides for every major NZ destination — real costs, best ages, top activities, and 3-day itineraries from NZ parents.",
           hub_type="destinations",
           items=destinations,
           item_url_prefix="destinations",
           item_slug_field="slug",
           item_name_field="name",
           item_desc_field="tagline",
           **ctx)

    # ── Individual destination pages ──────────────────────────────────────────
    for dest in destinations:
        dest_slug_base = dest["slug"].replace("-with-kids","").replace("-family-guide","").replace("-family","")
        dest_activities = [a for a in activities if a["destination"] == dest_slug_base]
        render("destination.html",
               f"destinations/{dest['slug']}/index.html",
               destination=dest,
               dest_activities=dest_activities,
               **ctx)

    # ── Activities hub ────────────────────────────────────────────────────────
    render("hub.html", "activities/index.html",
           hub_title="Family Activities in New Zealand",
           hub_subtitle="Kid-friendly activities across New Zealand — real 2026 prices, minimum ages, rain-safe options, and honest parent reviews for every major destination.",
           hub_type="activities",
           items=activities,
           item_url_prefix="activity",
           item_slug_field="slug",
           item_name_field="name",
           item_desc_field="tagline",
           **ctx)

    # ── Activities by destination ─────────────────────────────────────────────
    dest_slugs = set(a["destination"] for a in activities)
    for d_slug in dest_slugs:
        city_acts = [a for a in activities if a["destination"] == d_slug]
        dest_obj  = next((d for d in destinations if d_slug in d["slug"]), None)
        render("activities_city.html",
               f"activities/{d_slug}/index.html",
               city_slug=d_slug,
               city_name=city_acts[0]["destination"].title() if city_acts else d_slug.title(),
               dest_obj=dest_obj,
               city_activities=city_acts,
               **ctx)

    # ── Individual activity pages ─────────────────────────────────────────────
    for activity in activities:
        dest_obj = next((d for d in destinations if activity["destination"] in d["slug"]), None)
        render("activity.html",
               f"activity/{activity['slug']}/index.html",
               activity=activity,
               dest_obj=dest_obj,
               **ctx)

    # ── Activity filter pages (pSEO — by rain-safe, wildlife, indoor, etc.) ───
    filter_pages = [
        {
            "slug": "rainy-day",
            "label": "Rainy Day Activities",
            "title": "Rainy Day Activities in New Zealand with Kids",
            "desc": f"{sum(1 for a in activities if a.get('rain_safe'))} indoor and all-weather activities across NZ — guaranteed to work even when it rains. Real prices and honest reviews for NZ families.",
            "filter": lambda a: a.get("rain_safe"),
            "show_rain": False,
        },
        {
            "slug": "wildlife",
            "label": "Wildlife Activities",
            "title": "Wildlife Activities in New Zealand with Kids",
            "desc": f"{sum(1 for a in activities if a.get('category') == 'wildlife')} wildlife experiences for NZ families — kiwi, seals, dolphins and more. Real prices, minimum ages, and whether they're worth it.",
            "filter": lambda a: a.get("category") == "wildlife",
            "show_rain": True,
        },
        {
            "slug": "outdoor",
            "label": "Outdoor Adventures",
            "title": "Outdoor Family Activities in New Zealand — 2026 Guide",
            "desc": f"{sum(1 for a in activities if a.get('category') in ('outdoor','nature','water_sports'))} outdoor and nature activities for NZ families with kids. Real prices, minimum ages, and rain-safe options.",
            "filter": lambda a: a.get("category") in ("outdoor", "nature", "water_sports"),
            "show_rain": True,
        },
        {
            "slug": "toddlers",
            "label": "Activities for Toddlers",
            "title": "NZ Family Activities for Toddlers and Under 3s — 2026",
            "desc": f"{sum(1 for a in activities if (a.get('min_age') or 0) <= 2)} activities suitable for toddlers and under 3s in New Zealand — no minimum age or under 2. Real prices and honest reviews.",
            "filter": lambda a: (a.get("min_age") or 0) <= 2,
            "show_rain": True,
        },
    ]
    rendered_filter_slugs = []
    for fp in filter_pages:
        filtered = [a for a in activities if fp["filter"](a)]
        if len(filtered) >= 3:
            render("activities-filter.html",
                   f"activities/{fp['slug']}/index.html",
                   filter_slug=fp["slug"],
                   filter_label=fp["label"],
                   filter_title=fp["title"],
                   filter_desc=fp["desc"],
                   filter_activities=filtered,
                   filter_show_rain=fp["show_rain"],
                   **ctx)
            rendered_filter_slugs.append(fp["slug"])

    # ── Itineraries hub ───────────────────────────────────────────────────────
    render("hub.html", "itineraries/index.html",
           hub_title="NZ Family Itineraries — Day-by-Day Trip Plans",
           hub_subtitle="Day-by-day NZ family itineraries with real costs, drive times, and honest tips — from weekend breaks to 14-day South Island road trips.",
           hub_type="itineraries",
           items=itineraries,
           item_url_prefix="itineraries",
           item_slug_field="slug",
           item_name_field="title",
           item_desc_field="tagline",
           **ctx)

    # ── Individual itinerary pages ────────────────────────────────────────────
    for itin in itineraries:
        render("itinerary.html",
               f"itineraries/{itin['slug']}/index.html",
               itinerary=itin,
               **ctx)

    # ── Itinerary builder ─────────────────────────────────────────────────────
    render("itinerary-builder.html", "itinerary-builder/index.html", **ctx)

    # ── Price alerts signup ───────────────────────────────────────────────────
    render("price-alerts.html", "price-alerts/index.html", **ctx)

    # ── Interactive NZ Map ───────────────────────────────────────────────────
    render("nz-map.html", "nz-map/index.html", **ctx)

    # ── My Trip saved items page ─────────────────────────────────────────────
    render("my-trip.html", "my-trip/index.html", **ctx)

    # ── Campervans hub ────────────────────────────────────────────────────────
    render("campervans.html", "campervans/index.html", **ctx)

    # ── Individual campervan comparison pages ────────────────────────────────
    for van in campervans:
        render("campervan.html",
               f"campervans/{van['slug']}/index.html",
               van=van,
               **ctx)

    # ── Tools hub ────────────────────────────────────────────────────────────
    render("hub.html", "tools/index.html",
           hub_title="NZ Family Travel Tools & Calculators",
           hub_subtitle="Free tools to plan your NZ family holiday — budget calculators, packing lists, driving times, best month to visit, and school holiday planners.",
           hub_type="tools",
           items=tools,
           item_url_prefix="tools",
           item_slug_field="slug",
           item_name_field="title",
           item_desc_field="description",
           **ctx)

    # ── Individual tool pages ────────────────────────────────────────────────
    for tool in tools:
        render("tool.html",
               f"tools/{tool['slug']}/index.html",
               tool=tool,
               **ctx)

    # ── Travel tips hub ───────────────────────────────────────────────────────
    render("hub.html", "travel-tips/index.html",
           hub_title="NZ Family Travel Tips & Guides",
           hub_subtitle="Practical NZ family travel guides — packing lists, campervan advice, travel costs, school holiday tips, and what to do with babies, toddlers, and teens.",
           hub_type="travel-tips",
           items=guides,
           item_url_prefix="travel-tips",
           item_slug_field="slug",
           item_name_field="title",
           item_desc_field="intro",
           **ctx)

    # ── Individual guide pages ────────────────────────────────────────────────
    for guide in guides:
        render("guide.html",
               f"travel-tips/{guide['slug']}/index.html",
               guide=guide,
               **ctx)

    # ── Auto-generated posts — merged into /travel-tips/ silo ───────────────
    # Posts render under travel-tips/ path to consolidate the content silo.
    # Redirect pages at the old /posts/ paths preserve any inbound links.
    if posts:
        for post in posts:
            render("guide.html",
                   f"travel-tips/{post['slug']}/index.html",
                   guide=post,
                   **ctx)

        # Redirect pages at old /posts/ URLs → /travel-tips/
        redirect_tmpl = (
            '<!DOCTYPE html><html><head>'
            '<meta charset="UTF-8">'
            '<meta name="robots" content="noindex, follow">'
            '<meta http-equiv="refresh" content="0; url={dest}">'
            '<link rel="canonical" href="{dest}">'
            '<title>Redirecting…</title></head>'
            '<body><a href="{dest}">Click here if not redirected automatically.</a></body></html>'
        )
        posts_hub_dest = f"{site['base_url']}/travel-tips/"
        (OUT / "posts" / "index.html").parent.mkdir(parents=True, exist_ok=True)
        (OUT / "posts" / "index.html").write_text(redirect_tmpl.format(dest=posts_hub_dest))
        for post in posts:
            dest = f"{site['base_url']}/travel-tips/{post['slug']}/"
            post_dir = OUT / "posts" / post['slug']
            post_dir.mkdir(parents=True, exist_ok=True)
            (post_dir / "index.html").write_text(redirect_tmpl.format(dest=dest))

    # ── Cities hub ───────────────────────────────────────────────────────────
    render("hub.html", "cities/index.html",
           hub_title="NZ City Family Guides — Hamilton, Whangarei, Invercargill & More",
           hub_subtitle="Family travel guides for 35 NZ cities and towns — things to do, rainy-day options, where to stay, and honest budget tips.",
           hub_type="cities",
           items=cities,
           item_url_prefix="cities",
           item_slug_field="slug",
           item_name_field="name",
           item_desc_field="tagline",
           **ctx)

    # ── Individual city pages ─────────────────────────────────────────────────
    for city in cities:
        render("city.html",
               f"cities/{city['slug']}/index.html",
               city=city,
               **ctx)

    # ── Overseas destinations hub ─────────────────────────────────────────────
    render("hub.html", "overseas/index.html",
           hub_title="Overseas Family Travel from NZ — Thailand, Bali, Vietnam & More",
           hub_subtitle="Honest guides for NZ families travelling overseas — real costs, flight times, and what actually works with kids.",
           hub_type="overseas",
           items=overseas,
           item_url_prefix="overseas",
           item_slug_field="slug",
           item_name_field="title",
           item_desc_field="tagline",
           **ctx)

    # ── Individual overseas destination pages ─────────────────────────────────
    for dest in overseas:
        render("overseas.html",
               f"overseas/{dest['slug']}/index.html",
               dest=dest,
               **ctx)

    # ── Sitemap ───────────────────────────────────────────────────────────────
    from datetime import date as _date
    today = _date.today().isoformat()

    def sm_url(path, priority="0.6", changefreq="monthly", images=None):
        loc = f"{site['base_url']}/{path}/" if path else f"{site['base_url']}/"
        parts = [f'  <url><loc>{loc}</loc><lastmod>{today}</lastmod>',
                 f'<changefreq>{changefreq}</changefreq><priority>{priority}</priority>']
        if images:
            for img_url, img_caption in images:
                if img_url.startswith('/'):
                    img_url = f"{site['base_url']}{img_url}"
                safe_url = img_url.replace('&', '&amp;')
                safe_cap = img_caption.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                parts.append(
                    f'<image:image><image:loc>{safe_url}</image:loc>'
                    f'<image:caption>{safe_cap}</image:caption></image:image>'
                )
        parts.append('</url>\n')
        return ''.join(parts)

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    )
    sitemap += sm_url("", "1.0", "weekly")
    sitemap += sm_url("about", "0.5", "yearly")
    sitemap += sm_url("privacy", "0.3", "yearly")
    sitemap += sm_url("school-holidays", "0.9", "yearly")
    sitemap += sm_url("weather", "0.8", "yearly")
    sitemap += sm_url("holiday-parks", "0.8", "yearly")
    for region in holiday_parks.get("regions", []):
        for park in region.get("parks", []):
            if park.get("slug"):
                sitemap += sm_url(f"holiday-parks/{park['slug']}", "0.7", "monthly")
    sitemap += sm_url("nz-map", "0.7", "monthly")
    for slug in ["destinations", "itineraries", "campervans", "activities", "tools", "travel-tips", "overseas", "cities"]:
        sitemap += sm_url(slug, "0.8", "weekly")
    for d in destinations:
        imgs = []
        dm = media["destinations"].get(d["slug"], {})
        if dm.get("hero_image"):
            imgs.append((dm["hero_image"]["url"], dm["hero_image"].get("alt", d["name"])))
        for g in dm.get("gallery", []):
            imgs.append((g["url"], g.get("alt", d["name"])))
        sitemap += sm_url(f"destinations/{d['slug']}", "0.9", "monthly", images=imgs or None)
    for i in itineraries:
        sitemap += sm_url(f"itineraries/{i['slug']}", "0.9", "monthly")
    for v in campervans:
        sitemap += sm_url(f"campervans/{v['slug']}", "0.8", "monthly")
    for a in activities:
        imgs = []
        am = media["activities"].get(a["slug"], {})
        if am.get("image"):
            imgs.append((am["image"]["url"], am["image"].get("alt", a["name"])))
        sitemap += sm_url(f"activity/{a['slug']}", "0.7", "monthly", images=imgs or None)
    for s in dest_slugs:
        sitemap += sm_url(f"activities/{s}", "0.6", "monthly")
    for fp_slug in rendered_filter_slugs:
        sitemap += sm_url(f"activities/{fp_slug}", "0.7", "monthly")
    for t in tools:
        sitemap += sm_url(f"tools/{t['slug']}", "0.7", "monthly")
    for g in guides:
        sitemap += sm_url(f"travel-tips/{g['slug']}", "0.7", "monthly")
    for p in posts:
        sitemap += sm_url(f"travel-tips/{p['slug']}", "0.8", "weekly")
    for o in overseas:
        imgs = [(o["hero_image"], o.get("hero_alt", o.get("title", "")))] if o.get("hero_image") else None
        sitemap += sm_url(f"overseas/{o['slug']}", "0.7", "monthly", images=imgs)
    for c in cities:
        sitemap += sm_url(f"cities/{c['slug']}", "0.7", "monthly")
    sitemap += "</urlset>"
    (OUT / "sitemap.xml").write_text(sitemap)

    # ── robots.txt — allow all AI search/citation bots ───────────────────────
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\n"
        "User-agent: GPTBot\nAllow: /\n\n"
        "User-agent: ChatGPT-User\nAllow: /\n\n"
        "User-agent: PerplexityBot\nAllow: /\n\n"
        "User-agent: ClaudeBot\nAllow: /\n\n"
        "User-agent: anthropic-ai\nAllow: /\n\n"
        "User-agent: Google-Extended\nAllow: /\n\n"
        "User-agent: Bingbot\nAllow: /\n\n"
        "User-agent: CCBot\nDisallow: /\n\n"
        f"Sitemap: {site['base_url']}/sitemap.xml\n"
        f"Feed: {site['base_url']}/feed.xml\n"
    )

    # ── llms.txt — context file for AI systems ────────────────────────────────
    dest_names = ", ".join(d["name"] for d in destinations[:8])
    guide_titles = "\n".join(f"- {g.get('title', g['slug'])}: {site['base_url']}/travel-tips/{g['slug']}/" for g in (guides + posts)[:10])
    (OUT / "llms.txt").write_text(
        "# NZ Family Travel\n\n"
        "NZ Family Travel is an independent New Zealand travel planning resource written by NZ parents for families.\n"
        "All costs, reviews, and recommendations are based on real NZ family experiences — no PR trips, no paid placements.\n\n"
        "## What We Cover\n\n"
        f"- Destination guides for {len(destinations)} NZ locations: {dest_names} and more\n"
        f"- {len(itineraries)} family itineraries from 3 to 14 days — with drive times, budget breakdowns, and kid-friendly stops\n"
        "- Campervans: Jucy vs Britz vs Maui vs Mighty — price, size, family fit, hire tips from $89/day\n"
        "- Activities by region: bungy, Skyline Rotorua, Waitomo glowworms, whale watching, thermal pools, wildlife parks\n"
        "- NZ school holiday dates 2025–2027 with crowd impact, price warnings, and booking advice\n"
        "- Monthly weather matrix — rain, temperature, daylight for every NZ region\n"
        f"- {len(holiday_parks.get('regions', []))*3} holiday parks reviewed across NZ — prices, family ratings, amenities\n"
        "- Overseas: Bali, Thailand, Japan, Fiji, Australia — family travel from NZ\n"
        "- Free tools: budget calculator, packing list generator, driving times, school holidays tracker\n\n"
        "## Key Facts for AI Citations\n\n"
        "- NZ campervans cost from $89/day (budget) to $350/day (luxury 4-berth)\n"
        "- School holidays in NZ: Term 1 ends mid-April, Term 2 ends late June/July, Term 3 ends late September, Term 4 ends mid-December\n"
        "- Best months for families: October–April (summer). July for skiing at Ruapehu, Coronet Peak, The Remarkables.\n"
        "- NZ road trip essentials: allow 2+ hours Auckland to Hamilton, 4+ hours Auckland to Rotorua, 5+ hours Auckland to Wellington\n"
        "- Holiday parks: typically $40–$70/night for powered site (family of 4)\n\n"
        "## Key Pages\n\n"
        f"- All destinations: {site['base_url']}/destinations/\n"
        f"- Family itineraries: {site['base_url']}/itineraries/\n"
        f"- Campervan guide: {site['base_url']}/campervans/\n"
        f"- Activities hub: {site['base_url']}/activities/\n"
        f"- School holidays 2026: {site['base_url']}/travel-tips/nz-school-holidays-2026/\n"
        f"- NZ weather by month: {site['base_url']}/weather/\n"
        f"- Travel tips: {site['base_url']}/travel-tips/\n"
        f"- Holiday parks: {site['base_url']}/holiday-parks/\n"
        f"- Budget calculator: {site['base_url']}/tools/nz-family-travel-budget-calculator/\n"
        f"- RSS feed: {site['base_url']}/feed.xml\n\n"
        "## Recent Guides\n\n"
        f"{guide_titles}\n\n"
        "## About\n\n"
        "Written by NZ parents with real experience travelling around New Zealand with children.\n"
        "Affiliate disclosure: we earn a small commission on some campervan, activity and accommodation referrals — this never affects rankings or recommendations.\n"
        f"Contact: {site['contact_email']}\n"
    )

    # ── RSS feed ──────────────────────────────────────────────────────────────
    base_url = site["base_url"]

    def to_rfc822(date_str):
        from email.utils import format_datetime
        from datetime import datetime
        import re
        if not date_str:
            return format_datetime(datetime.now())
        # "June 2026" → first of that month
        m = re.match(r'(\w+)\s+(\d{4})', str(date_str))
        if m:
            try:
                dt = datetime.strptime(f"01 {m.group(1)} {m.group(2)}", "%d %B %Y")
                return format_datetime(dt)
            except ValueError:
                pass
        # ISO date "2026-06-13"
        m2 = re.match(r'(\d{4}-\d{2}-\d{2})', str(date_str))
        if m2:
            dt = datetime.strptime(m2.group(1), "%Y-%m-%d")
            return format_datetime(dt)
        return format_datetime(datetime.now())

    rss_items = []
    for item in sorted(guides + posts, key=lambda x: x.get("updated", x.get("date", "")), reverse=True)[:50]:
        slug = item["slug"]
        title = item.get("title", slug)
        desc = item.get("meta_desc", item.get("meta_description", item.get("description", "")))
        date_str = item.get("updated", item.get("date", today))
        rss_items.append(
            f"    <item>\n"
            f"      <title><![CDATA[{title}]]></title>\n"
            f"      <link>{base_url}/travel-tips/{slug}/</link>\n"
            f"      <guid isPermaLink='true'>{base_url}/travel-tips/{slug}/</guid>\n"
            f"      <pubDate>{to_rfc822(date_str)}</pubDate>\n"
            f"      <description><![CDATA[{desc}]]></description>\n"
            f"    </item>"
        )
    rss_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '  <channel>\n'
        f'    <title>NZ Family Travel — Tips &amp; Guides</title>\n'
        f'    <link>{base_url}/</link>\n'
        f'    <description>Honest travel guides, itineraries and tips for families visiting New Zealand.</description>\n'
        f'    <language>en-NZ</language>\n'
        f'    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml"/>\n'
        + "\n".join(rss_items) + "\n"
        '  </channel>\n'
        '</rss>'
    )
    (OUT / "feed.xml").write_text(rss_xml)

    # ── Search index (Fuse.js) ────────────────────────────────────────────────
    search_index = []
    for d in destinations:
        search_index.append({"title": d["name"], "url": f"/destinations/{d['slug']}/",
                             "type": "destination", "text": f"{d.get('tagline', '')} {d.get('summary', '')}".strip()})
    for i in itineraries:
        search_index.append({"title": i.get("title", i["slug"]), "url": f"/itineraries/{i['slug']}/",
                             "type": "itinerary", "text": f"{i.get('subtitle', '')} {i.get('tagline', '')}".strip()})
    for a in activities:
        search_index.append({"title": a["name"], "url": f"/activity/{a['slug']}/",
                             "type": "activity", "text": f"{a.get('tagline', '')} {a.get('summary', '')}".strip()})
    for g in guides + posts:
        search_index.append({"title": g.get("title", g["slug"]), "url": f"/travel-tips/{g['slug']}/",
                             "type": "travel-tip", "text": g.get("intro", "")})
    (OUT / "search-index.json").write_text(json.dumps(search_index))

    # ── CNAME ─────────────────────────────────────────────────────────────────
    (OUT / "CNAME").write_text("nzfamilytravel.co.nz")

    print(f"\nBuild complete — {len(list(OUT.rglob('*.html')))} HTML pages → {OUT}/")


if __name__ == "__main__":
    build()
