# NZ Family Travel — SEO Action Plan
> Generated: 2026-05-30 | Audit Score: 73/100 (Good)

---

## Critical Blockers (Fix This Week)

### 1. Strip verbose title suffix (affects 87 pages, 37%)
**File:** `layouts/base.html` — `<title>` tag
**Problem:** " — NZ Family Travel 2026" appended to every title wastes ~25 chars. 87 titles exceed 70 chars.
**Fix:** Remove year from suffix OR strip suffix entirely on non-homepage pages. Use `{% if page.slug == 'index' %} — NZ Family Travel{% endif %}`.
**Impact:** Immediate CTR improvement; all 87 truncated titles fixed in 1 template change.

### 2. Fix `@type: Trip` → `TouristTrip` on itinerary pages (23 pages)
**File:** `layouts/itinerary.html` — JSON-LD schema block
**Problem:** `Trip` is not a Google-supported rich result type. `TouristTrip` is eligible for rich results.
**Fix:** Change `"@type": "Trip"` to `"@type": "TouristTrip"` and add:
```json
"touristType": {"@type": "Audience", "audienceType": "Families with children"},
"itinerary": {"@type": "ItemList", "itemListElement": [...days as ListItem...]}
```
**Impact:** Unlocks itinerary rich results in Google Search.

### 3. Download and serve hero images locally
**Problem:** All images are external Wikimedia URLs — no control, CWV risk, image sitemap ignored.
**Fix:** For each destination/itinerary, download 1 hero image, convert to WebP, save to `/static/img/[slug]-hero.webp`. Update data JSON `hero_image` fields.
**Priority destinations:** Queenstown, Rotorua, Abel Tasman, Fiordland, Bay of Islands
**Impact:** Fixes Core Web Vitals risk, enables image sitemap entries, removes external dependency.

---

## High Impact (This Month)

### 4. Add contextual internal links to itinerary body copy
**Problem:** All 23 itinerary pages have zero contextual links in body copy — only 169 nav links.
**Fix:** Per itinerary, add 3–5 inline links:
- Link to matching destination page (`/destinations/[slug]/`)
- Link to 1 related itinerary
- Link to 1 relevant travel tip or activity page
**Start with:** Fiordland, Abel Tasman, Hawke's Bay (newest itineraries)

### 5. Add `TouristDestination` schema to destination pages (20 pages)
**File:** `layouts/destination.html`
**Fix:**
```json
{"@type": "TouristDestination", "name": "...", "description": "...",
 "touristType": {"@type": "Audience", "audienceType": "Families"}}
```

### 6. Add `hreflang="en-NZ"` self-declaration
**File:** `layouts/base.html` — `<head>` block
**Fix:** `<link rel="alternate" hreflang="en-NZ" href="{{ page.canonical_url }}" />`

---

## Content Gaps — Build These Pages (Priority Order)

| # | URL | Target Keyword | Monthly Searches | Affiliate |
|---|---|---|---|---|
| 1 | `/school-holidays/` (expand) | nz school holidays 2026 | 3,400 | Bookme/TOP 10 |
| 2 | `/activities/rotorua-kids/` | things to do rotorua with kids | 1,200 | Bookme |
| 3 | `/activities/auckland-kids/` | things to do auckland with kids | 900 | Bookme/Viator |
| 4 | `/campervans/jucy-vs-maui-family/` | jucy vs maui campervan family | 720 | Jucy + Maui |
| 5 | `/activities/queenstown-kids/` | queenstown family activities | 590 | Bookme |
| 6 | `/activities/free-nz-kids/` | free things to do nz with kids | 480 | TOP 10 |
| 7 | `/travel-tips/nz-in-december/` | nz family holiday december | 410 | Booking.com |
| 8 | `/campervans/4-berth-vs-6-berth/` | 4 berth vs 6 berth campervan nz | 340 | Discover Cars |
| 9 | `/school-holidays/winter-2026/` | nz winter school holidays 2026 | 280+ spike | TOP 10 |
| 10 | `/best-time-to-visit-nz-with-kids/` | best time visit nz kids | AEO pillar | All |

### Content Clusters to Build

**Cluster 1 — School Holidays** (pillar: `/school-holidays/`)
- P1: `/school-holidays/winter-2026/`, `/school-holidays/october-2026/`, `/school-holidays/summer-2026/`
- P2: `/school-holidays/activities-auckland/`, `/school-holidays/cheap-ideas-nz/`

**Cluster 2 — Campervans** (pillar: `/campervans/`)
- P1: `/campervans/jucy-vs-maui-family/`, `/campervans/4-berth-vs-6-berth/`, `/campervans/cost-nz-family/`
- P2: `/campervans/freedom-camping-nz-families/`, `/campervans/north-island-route/`

**Cluster 3 — City Activities** (pillar: `/activities/`)
- P1: `/activities/rotorua-kids/`, `/activities/auckland-kids/`, `/activities/queenstown-kids/`, `/activities/christchurch-kids/`
- P2: `/activities/free-nz-kids/`, `/activities/rainy-day-nz/`

**Cluster 4 — Monthly Guides** (pillar: `/best-time-to-visit-nz-with-kids/`)
- P1: `/travel-tips/nz-in-december/`, `/travel-tips/nz-in-january/`
- P2: `/travel-tips/nz-in-april/`, `/travel-tips/nz-in-july/`

---

## Cannibalization Fixes

- **7-day vs 10-day North Island itineraries** both target "north island family road trip nz"
  - Fix: 7-day targets "one week north island family road trip"; 10-day targets "two weeks / fortnight"
- **Activities content split** across `/destinations/` and `/travel-tips/`
  - Fix: Move all city activity content to `/destinations/` or create `/activities/` section

---

## AEO Pages to Write (AI Engine Capture)

These formats have highest extraction probability for AI search answers:

| Query | Format | Page |
|---|---|---|
| "When are NZ school holidays 2026?" | Date table | `/school-holidays/` |
| "Which campervan is best for NZ families?" | Comparison table | `/campervans/jucy-vs-maui-family/` |
| "What month is best to visit NZ with kids?" | Month-by-month table | `/best-time-to-visit-nz-with-kids/` |
| "What are free things to do in NZ with kids?" | Bulleted list | `/activities/free-nz-kids/` |
| "How long do you need in NZ with kids?" | Direct answer + links | `/best-time-to-visit-nz-with-kids/` |

---

## Sitemap Check

232 built pages — verify all are included in `/sitemap.xml`. Check build script for any pages skipped.

---

## Score Recovery Estimate

| Fix | Category | Expected Score Gain |
|---|---|---|
| Fix title lengths | On-Page | +4 pts |
| TouristTrip schema | Technical | +3 pts |
| Contextual internal links | On-Page | +3 pts |
| TouristDestination schema | Technical | +2 pts |
| Local hero images | Technical | +3 pts |
| **Total** | | **+15 pts → ~88/100** |
