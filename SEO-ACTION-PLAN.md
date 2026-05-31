# NZ Family Travel — SEO Action Plan
> Generated: 2026-05-30 | Audit Score: 73/100 (Good)

---

## Critical Blockers (Fix This Week)

### ✅ 1. Strip verbose title suffix (affects 87 pages, 37%)
**DONE 2026-05-30** — Fixed all layout templates with conditional title logic: `itinerary.html`, `activity.html`, `guide.html`, `hub.html`, `campervans.html`, `city.html`, `nz-map.html`, `campervan.html`, `activities-filter.html`, `activities_city.html`, `destination.html`. Deployed.

### ✅ 2. Fix `@type: Trip` → `TouristTrip` on itinerary pages (23 pages)
**DONE 2026-05-30** — Changed to `TouristTrip`, added `touristType: "Family with children"`, added `itinerary` ItemList with per-day ListItems in `layouts/itinerary.html`. Deployed.

### ✅ 3. Download and serve hero images locally
**DONE 2026-05-30** — All 19 destination hero images downloaded from Wikimedia, compressed to max 1200px / 80% quality via Pillow, saved to `/static/img/destinations/[slug].jpg`. Updated all `hero_image.url` values in `data/media.json`. Deployed.

---

## High Impact (This Month)

### ✅ 4. Add contextual internal links to itinerary body copy
**DONE 2026-05-30** — Added "Plan Your Trip" section to `layouts/itinerary.html` with dynamic links: matching destination page, campervan page (if road trip), school holidays page, and activity search.

### ✅ 5. Add `TouristDestination` schema to destination pages (20 pages)
**DONE 2026-05-30** — `TouristDestination` schema already present in `layouts/destination.html`. Confirmed via read; no change needed.

### ✅ 6. Add `hreflang="en-NZ"` self-declaration
**DONE 2026-05-30** — `hreflang="en-NZ"` already present in `layouts/base.html`. Confirmed; no change needed.

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
