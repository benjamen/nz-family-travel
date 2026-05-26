#!/usr/bin/env python3
"""NZ Family Travel — static site generator."""

import json
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ROOT    = Path(__file__).parent
DATA    = ROOT / "data"
LAYOUTS = ROOT / "layouts"
STATIC  = ROOT / "static"
CONTENT = ROOT / "content"
OUT     = ROOT / "docs"

env = Environment(loader=FileSystemLoader(str(LAYOUTS)), autoescape=False)


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

    site         = load("site")
    destinations = load("destinations")
    activities   = load("activities")
    itineraries  = load("itineraries")
    campervans   = load("campervans")
    media        = load("media")
    guides       = load_content_dir("travel-tips")
    tools        = load_content_dir("tools")
    overseas     = load_content_dir("overseas")
    posts        = load_content_dir("posts")

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

    # ── Destinations hub ──────────────────────────────────────────────────────
    render("hub.html", "destinations/index.html",
           hub_title="NZ Family Travel Destinations",
           hub_subtitle="Where to take the family in New Zealand — honest guides for every major destination.",
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
           hub_subtitle="Kid-friendly activities across NZ — with real prices, minimum ages, and honest reviews.",
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

    # ── Itineraries hub ───────────────────────────────────────────────────────
    render("hub.html", "itineraries/index.html",
           hub_title="NZ Family Itineraries — Day-by-Day Trip Plans",
           hub_subtitle="Fully planned NZ family holidays with costs, drive times and honest tips.",
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

    # ── Interactive NZ Map ───────────────────────────────────────────────────
    render("nz-map.html", "nz-map/index.html", **ctx)

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
           hub_subtitle="Free tools to plan your NZ family holiday — budget calculators, packing lists, driving times.",
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
           hub_subtitle="Practical advice for planning a New Zealand family holiday — costs, campervans, and what to pack.",
           hub_type="guides",
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

    # ── Auto-generated posts hub ─────────────────────────────────────────────
    if posts:
        render("hub.html", "posts/index.html",
               hub_title="NZ Family Travel News & Deals",
               hub_subtitle="Daily travel tips, current deals, and destination guides for NZ families — updated every day.",
               hub_type="guides",
               items=posts,
               item_url_prefix="posts",
               item_slug_field="slug",
               item_name_field="title",
               item_desc_field="intro",
               **ctx)

        for post in posts:
            render("guide.html",
                   f"posts/{post['slug']}/index.html",
                   guide=post,
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

    def sm_url(path, priority="0.6", changefreq="monthly"):
        loc = f"{site['base_url']}/{path}" if path else site['base_url']
        return f'  <url><loc>{loc}</loc><lastmod>{today}</lastmod><changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>\n'

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += sm_url("", "1.0", "weekly")
    sitemap += sm_url("about", "0.5", "yearly")
    sitemap += sm_url("nz-map", "0.7", "monthly")
    for slug in ["destinations", "itineraries", "campervans", "activities", "tools", "travel-tips", "overseas"]:
        sitemap += sm_url(slug, "0.8", "weekly")
    for d in destinations:
        sitemap += sm_url(f"destinations/{d['slug']}", "0.9", "monthly")
    for i in itineraries:
        sitemap += sm_url(f"itineraries/{i['slug']}", "0.9", "monthly")
    for v in campervans:
        sitemap += sm_url(f"campervans/{v['slug']}", "0.8", "monthly")
    for a in activities:
        sitemap += sm_url(f"activity/{a['slug']}", "0.7", "monthly")
    for s in dest_slugs:
        sitemap += sm_url(f"activities/{s}", "0.6", "monthly")
    for t in tools:
        sitemap += sm_url(f"tools/{t['slug']}", "0.7", "monthly")
    for g in guides:
        sitemap += sm_url(f"travel-tips/{g['slug']}", "0.7", "monthly")
    for o in overseas:
        sitemap += sm_url(f"overseas/{o['slug']}", "0.7", "monthly")
    if posts:
        sitemap += sm_url("posts", "0.8", "daily")
        for p in posts:
            sitemap += sm_url(f"posts/{p['slug']}", "0.8", "weekly")
    sitemap += "</urlset>"
    (OUT / "sitemap.xml").write_text(sitemap)

    # ── robots.txt ────────────────────────────────────────────────────────────
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {site['base_url']}/sitemap.xml\n"
    )

    # ── CNAME ─────────────────────────────────────────────────────────────────
    (OUT / "CNAME").write_text("nzfamilytravel.co.nz")

    print(f"\nBuild complete — {len(list(OUT.rglob('*.html')))} HTML pages → {OUT}/")


if __name__ == "__main__":
    build()
