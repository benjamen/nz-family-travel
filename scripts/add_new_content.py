#!/usr/bin/env python3
"""
Add 6 high-value itineraries and 4 top travel guides.
Run: .venv/bin/python3 scripts/add_new_content.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ── 6 NEW ITINERARIES ─────────────────────────────────────────────────────────

NEW_ITINERARIES = [

  {
    "slug": "golden-triangle-auckland-waitomo-rotorua-3-days",
    "title": "Golden Triangle NZ — Auckland, Waitomo & Rotorua in 3 Days",
    "subtitle": "Auckland → Waitomo Caves → Rotorua",
    "tagline": "NZ's most popular short family loop — glowworm caves, geothermal parks, and hobbit holes",
    "duration_days": 3,
    "distance_km": 460,
    "budget_family4": "$1,400–2,200",
    "budget_breakdown": {
      "accommodation": "$130–280/night",
      "activities": "$150–350/day",
      "food": "$70–120/day",
      "fuel": "~$80 total"
    },
    "best_for": "All ages — perfect first NZ trip or school holiday long weekend",
    "best_season": "Year-round (Waitomo and Rotorua run in all weather)",
    "transport": "Rental car or campervan",
    "commercial_intent_score": 98,
    "highlights": [
      "Waitomo Glowworm Caves (underground starfield of glowworms)",
      "Hobbiton Movie Set option (Matamata, 45 min detour)",
      "Te Puia geothermal park and Māori cultural performance",
      "Skyline Rotorua Gondola and Luge",
      "Kuirau Park free hot pools"
    ],
    "days": [
      {
        "day": 1,
        "location": "Auckland → Waitomo",
        "title": "Drive South — The Waitomo Caves",
        "drive_from_prev": "2.5–3 hrs from Auckland (via SH1 then SH3)",
        "activities": [
          "Leave Auckland by 8am to beat traffic (SH1 south, then SH3 at Otorohanga)",
          "Arrive Waitomo — Glowworm Cave tour (45 min guided, runs every 30 min, $55/adult $27/child)",
          "Option: add Ruakuri Cave (2 hrs, more dramatic, $75/adult) or Black Labyrinth tube tour for teens",
          "Lunch at Waitomo Caves Hotel café or Huhu Restaurant",
          "Afternoon: Otorohanga Kiwi House (25 min back north, great for young kids, $14/adult)",
          "Drive to Rotorua (1.5 hrs via Cambridge or direct via SH1)"
        ],
        "accommodation": "Rotorua (holiday park, hotel or motel)",
        "estimated_cost": "$200–380",
        "tips": [
          "Pre-book Waitomo cave tours online — school holidays sell out. Save 10% online vs gate.",
          "Glowworm Cave suits all ages including toddlers. Ruakuri has stairs — no prams.",
          "Otorohanga Kiwi House is one of the best kiwi encounters in NZ — skip if pressed for time."
        ]
      },
      {
        "day": 2,
        "location": "Rotorua",
        "title": "Geothermal Wonders & Māori Culture",
        "drive_from_prev": null,
        "activities": [
          "Morning: Te Puia — geysers, mud pools, kiwi house, and Māori cultural performance ($55/adult)",
          "Lunch: Eat Streat Rotorua — NZ's most family-friendly food street, $10–15 mains",
          "Afternoon: Skyline Gondola (free) + Luge ($15/ride, get multi-ride pass)",
          "Late afternoon: Kuirau Park free geothermal walk and public foot baths",
          "Evening: Tamaki Māori Village hāngī dinner (optional, $150/adult — unforgettable)"
        ],
        "accommodation": "Rotorua (same)",
        "estimated_cost": "$180–350",
        "tips": [
          "Te Puia kiwi house is one of the best in NZ — they're nocturnal, so the dark indoor enclosure works.",
          "Kuirau Park is completely free and has boiling mud pools right on the street — surreal.",
          "The Luge closes in heavy rain — afternoon is best for weather."
        ]
      },
      {
        "day": 3,
        "location": "Rotorua → Auckland (via optional Hobbiton)",
        "title": "Hobbiton & The Drive Home",
        "drive_from_prev": null,
        "activities": [
          "Option A (recommended): Hobbiton Movie Set at Matamata (45 min from Rotorua, $49/adult, 2.5 hr tour)",
          "Option B: Wai-O-Tapu Thermal Wonderland (30 min south of Rotorua — Lady Knox Geyser 10:15am daily)",
          "Drive back to Auckland (2.5–3 hrs from Matamata, or 2.5 hrs direct from Rotorua)",
          "Optional stop: Hamilton Gardens (free, 54 themed gardens) en route"
        ],
        "accommodation": "N/A — return to Auckland",
        "estimated_cost": "$80–200",
        "tips": [
          "Hobbiton under-9s are free — best value in NZ. Book early, especially holidays.",
          "If doing Hobbiton, take the Crown Range Road back via Cambridge — beautiful farmland.",
          "Hamilton Gardens only needs 2 hrs — perfect time filler before returning the rental car."
        ]
      }
    ],
    "affiliate_blocks": [
      {"type": "rental_car", "affiliate_key": "discover_cars", "cta": "Compare rental cars for the Golden Triangle", "note": "Any small car works — roads are all sealed SH routes."},
      {"type": "activities", "affiliate_key": "bookme", "cta": "Pre-book Waitomo & Rotorua activities", "note": "Waitomo caves sell out in school holidays — book before you leave Auckland."},
      {"type": "accommodation", "affiliate_key": "booking_com", "cta": "Find Rotorua accommodation"}
    ],
    "packing_tips": [
      "Warm layer for Waitomo — it's 12°C underground year-round",
      "Swimwear for Rotorua hot pools (Polynesian Spa or Wai Ariki)",
      "Cash or card — most Waitomo operators accept both but EFTPOS only at some cafés"
    ],
    "faqs": [
      {"q": "What order should I do the Golden Triangle?", "a": "Auckland → Waitomo → Rotorua is best. It puts Waitomo on day 1 when everyone is fresh, Rotorua is the main destination for day 2, and you return via Hobbiton on day 3. Going the other way (Rotorua first) can feel like an anticlimax."},
      {"q": "Can we add Hobbiton to the Golden Triangle?", "a": "Yes — Hobbiton at Matamata sits exactly on the Golden Triangle route, 45 min west of Rotorua and 30 min off the Auckland road. You can combine it with Waitomo on day 1 (long but doable, ~4.5 hrs driving total) or do it on the return on day 3."},
      {"q": "Is 3 days enough for the Golden Triangle?", "a": "3 days is the minimum — you'll see the key highlights. 4 days is more comfortable: gives you time for both Waitomo cave options, a full Rotorua day, and Hobbiton without rushing. Add Taupo (1.5 hrs south of Rotorua) for a 5-day loop."},
      {"q": "Is the Golden Triangle suitable for toddlers?", "a": "Mostly yes. Waitomo Glowworm Cave is pram-friendly (smooth path). Te Puia suits all ages. Skyline Luge has a minimum height of 110cm. Kuirau Park is fully pram-friendly. The main issue is the driving — 3 days is manageable but pack entertainment."}
    ]
  },

  {
    "slug": "christchurch-queenstown-south-island-7-days",
    "title": "Christchurch to Queenstown — 7-Day South Island Family Road Trip",
    "subtitle": "Christchurch → Akaroa → Mt Cook → Wanaka → Queenstown",
    "tagline": "The great South Island drive — mountain passes, turquoise lakes, French bays, and NZ's adventure capital",
    "duration_days": 7,
    "distance_km": 680,
    "budget_family4": "$4,200–6,800",
    "budget_breakdown": {
      "accommodation": "$160–380/night",
      "activities": "$120–300/day",
      "food": "$80–140/day",
      "fuel": "~$180 total"
    },
    "best_for": "Families with kids 4+, scenic drive lovers, first South Island visits",
    "best_season": "October–April (avoid July–August on mountain passes if nervous of snow)",
    "transport": "Rental car or campervan (all roads sealed)",
    "commercial_intent_score": 97,
    "highlights": [
      "Akaroa — swim with dolphins in a French colonial harbour town",
      "Lake Tekapo turquoise blue and Church of the Good Shepherd",
      "Aoraki/Mt Cook — NZ's highest peak, Hooker Valley walk",
      "Lake Wanaka and Puzzling World",
      "Queenstown gondola, luge, and lake activities"
    ],
    "days": [
      {
        "day": 1,
        "location": "Christchurch",
        "title": "Arrive Christchurch — City Exploration",
        "drive_from_prev": null,
        "activities": [
          "Christchurch Botanic Gardens (free, beautiful, 2 hrs)",
          "International Antarctic Centre (great for kids, $30/adult)",
          "Riverside Market for lunch ($10–18 mains)",
          "Tram tour of the city rebuild ($25/adult, kids free)"
        ],
        "accommodation": "Christchurch CBD or suburbs",
        "estimated_cost": "$80–180",
        "tips": [
          "Pick up your rental car the night before or early day 1 — morning rush hour out of CHC is significant.",
          "Mona Vale gardens (free) and the Cardboard Cathedral are good short stops."
        ]
      },
      {
        "day": 2,
        "location": "Christchurch → Akaroa",
        "title": "Akaroa — Dolphins and French Charm",
        "drive_from_prev": "1.5 hrs via Summit Road (Banks Peninsula)",
        "activities": [
          "Drive over the volcanic caldera rim — stop at Barry's Bay Cheese factory",
          "Black Cat Dolphin Swimming Cruise (min age 8 to swim, $170/adult — book ahead)",
          "Non-swimmers watch from the boat — guaranteed dolphin sightings",
          "Walk the Akaroa waterfront and main street",
          "Dinner in Akaroa — The French Farm Winery Restaurant has great views"
        ],
        "accommodation": "Akaroa (stay overnight for sunset over the harbour)",
        "estimated_cost": "$250–450",
        "tips": [
          "Black Cat cruises depart 9:30am and 1:30pm. The morning cruise is calmer water.",
          "Akaroa has only one ATM — bring cash or use payWave.",
          "The drive back via Summit Road at sunset is spectacular — allow extra time."
        ]
      },
      {
        "day": 3,
        "location": "Christchurch → Lake Tekapo",
        "title": "Canterbury Plains → Turquoise Tekapo",
        "drive_from_prev": "3.5 hrs (via Akaroa return + SH1/79 inland)",
        "activities": [
          "Return to Christchurch via Summit Road (adds 30 min, worth it)",
          "Drive inland via Methven (optional Mt Hutt ski field visit in winter)",
          "Arrive Lake Tekapo — Church of the Good Shepherd (free, 15 min)",
          "Lupins along the lakeshore November–December (spectacular)",
          "Lake Tekapo Springs hot pools (evening — great stargazing from the pools)"
        ],
        "accommodation": "Lake Tekapo township",
        "estimated_cost": "$120–250",
        "tips": [
          "Lake Tekapo is a Dark Sky Reserve — if it's clear, stargazing is world-class.",
          "Lupins are at peak mid-November to mid-December — absolutely worth timing your trip around.",
          "Book Tekapo Springs in advance in summer — it sells out."
        ]
      },
      {
        "day": 4,
        "location": "Lake Tekapo → Aoraki/Mt Cook",
        "title": "Mt Cook — NZ's Highest Peak",
        "drive_from_prev": "1.5 hrs via SH8 and SH80",
        "activities": [
          "Morning: Drive to Mt Cook Village (stop at Lake Pūkaki lookout — vivid blue, amazing photos)",
          "Hooker Valley Track (3 hrs return, easy, all ages, ends at a glacier lake with Mt Cook views)",
          "Lunch at the Old Mountaineer's Café (great food, Mt Cook views)",
          "Afternoon: Tasman Glacier viewpoint (20 min walk) or kayaking on the glacier lake"
        ],
        "accommodation": "Mt Cook Village or return to Tekapo",
        "estimated_cost": "$100–220",
        "tips": [
          "Hooker Valley Track is THE must-do walk in NZ. Flat, well-formed path. Prams possible but 3 swing bridges.",
          "Leave Mt Cook by 3pm to get to Wanaka at a reasonable hour.",
          "The drive from Lake Pūkaki to Mt Cook on SH80 is one of the world's great scenic drives."
        ]
      },
      {
        "day": 5,
        "location": "Aoraki/Mt Cook → Wanaka",
        "title": "Central Otago — Wine Country to Wanaka",
        "drive_from_prev": "3 hrs via Twizel and Cromwell",
        "activities": [
          "Stop at Cromwell for stone fruit from roadside stalls (summer only)",
          "Cromwell Historic Precinct — free, interesting, 30 min walk",
          "Arrive Wanaka — Puzzling World (2 hrs, excellent for kids $20/adult)",
          "Walk to That Wanaka Tree (free, 15 min walk from town)",
          "Evening swim at Lake Wanaka beach or kayak hire"
        ],
        "accommodation": "Wanaka township",
        "estimated_cost": "$130–260",
        "tips": [
          "Wanaka's waterfront has free swimming and paddleboarding — pack it in on a sunny afternoon.",
          "Book accommodation early — Wanaka is very popular and a small town."
        ]
      },
      {
        "day": 6,
        "location": "Wanaka → Queenstown",
        "title": "Crown Range — The Great Drive into Queenstown",
        "drive_from_prev": "1.5 hrs via Crown Range (SH89) — NZ's highest sealed road",
        "activities": [
          "Drive Crown Range Road (views over Wanaka valley — stop at the summit viewpoint)",
          "Arrowtown detour (20 min — gold panning, historic Chinese settlement, great cafés)",
          "Arrive Queenstown — check in and explore the lakefront",
          "Queenstown gondola for sunset views over Lake Wakatipu ($40/adult)",
          "Dinner on the Queenstown waterfront"
        ],
        "accommodation": "Queenstown",
        "estimated_cost": "$120–280",
        "tips": [
          "Crown Range adds only 20 min vs SH6 but is infinitely more scenic. Do it.",
          "Arrowtown Bakery has NZ's best pies. Stop."
        ]
      },
      {
        "day": 7,
        "location": "Queenstown",
        "title": "Full Queenstown Day — Adventure & Lake",
        "drive_from_prev": null,
        "activities": [
          "Skyline Gondola + Luge (multi-ride pass $55/adult)",
          "Queenstown Gardens (free, frisbee golf)",
          "TSS Earnslaw steamship cruise on Lake Wakatipu ($69/adult)",
          "Kjet jetboat on the Shotover River (teens/adults, $149/adult, 1 hr)",
          "Evening: Fergburger (NZ's most famous burger, arrive by 5pm to avoid queues)"
        ],
        "accommodation": "Queenstown (or depart)",
        "estimated_cost": "$200–400",
        "tips": [
          "Queenstown is expensive. Save money: free gondola ride for kids under 5, pack lunch for the gardens.",
          "Book Queenstown activities the day before — most run same-day but weather affects jetboating."
        ]
      }
    ],
    "affiliate_blocks": [
      {"type": "rental_car", "affiliate_key": "discover_cars", "cta": "Compare cars for Christchurch → Queenstown", "note": "One-way rentals available — fly into CHC, fly out of ZQN. Budget extra ~$150–200 for one-way fee."},
      {"type": "activities", "affiliate_key": "bookme", "cta": "Pre-book Akaroa, Queenstown & Wanaka activities"},
      {"type": "accommodation", "affiliate_key": "booking_com", "cta": "Book accommodation along the route"}
    ],
    "packing_tips": [
      "Layers — you'll go from Christchurch coast to 1,000m passes in one day",
      "Sunscreen — South Island UV is intense even on cloudy days",
      "Swimwear (multiple lake swims, hot pools at Tekapo)",
      "Good walking shoes for Hooker Valley Track"
    ],
    "faqs": [
      {"q": "Can I do this trip one-way (fly into Christchurch, out of Queenstown)?", "a": "Yes — this is the most popular way to do it. Most rental companies allow one-way rentals for an extra fee ($100–200). Alternatively, fly into Queenstown and do the route in reverse. Book return flights to Christchurch or onward from Queenstown."},
      {"q": "Is this itinerary suitable for young kids (under 5)?", "a": "Mostly yes. Botanic Gardens, Church of the Good Shepherd, Hooker Valley Track (mostly), Cromwell, Puzzling World, and Queenstown Gardens are all pram-friendly. The Akaroa dolphin swim requires kids to be 8+, but non-swimming kids can still watch from the boat."},
      {"q": "What if we skip Akaroa?", "a": "Akaroa is optional but highly recommended. If you skip it, add Kaikōura to the route instead (2.5 hrs north of Christchurch) for whale watching, or go directly inland to Tekapo and add a Methven day for Mt Hutt in winter."},
      {"q": "Is this route doable in a campervan?", "a": "Excellent campervan route — all roads are sealed and campsite infrastructure is strong. Allow an extra day for flexibility. Mt Cook campsite is excellent. Crown Range Road is fine for most campervans (check height/weight with your operator)."}
    ]
  },

  {
    "slug": "abel-tasman-family-3-days",
    "title": "Abel Tasman with Kids — 3-Day Family Guide",
    "subtitle": "Nelson → Motueka → Abel Tasman National Park → Golden Bay",
    "tagline": "Turquoise coves, golden beaches, and water taxis — NZ's most beautiful coastal national park",
    "duration_days": 3,
    "distance_km": 120,
    "budget_family4": "$1,600–2,600",
    "budget_breakdown": {
      "accommodation": "$140–300/night",
      "activities": "$200–400/day (water taxis + kayaks)",
      "food": "$70–120/day",
      "fuel": "~$40 total"
    },
    "best_for": "All ages — especially 5+. Summer (Dec–Mar) is best. Younger kids in calm bay kayaking.",
    "best_season": "December–March for swimming. October–November for fewer crowds.",
    "transport": "Car to Marahau/Kaiteriteri, then water taxi and feet",
    "commercial_intent_score": 93,
    "highlights": [
      "Abel Tasman Coast Track sections — NZ's most beautiful walking track",
      "Water taxi hopping between golden sand coves",
      "Sea kayaking in sheltered Abel Tasman bays",
      "Tonga Island marine reserve snorkelling",
      "Golden Bay — Takaka and Farewell Spit"
    ],
    "days": [
      {
        "day": 1,
        "location": "Nelson → Motueka → Abel Tasman",
        "title": "Arrive — Water Taxi into the Park",
        "drive_from_prev": "Nelson to Marahau: 1 hr via Motueka",
        "activities": [
          "Drive from Nelson via Motueka (Friday market 8am–1pm if timing allows)",
          "Park car at Marahau ($15/day secure parking) — this is the main park entrance",
          "Water taxi to Anchorage Bay or Torrent Bay (30 min, $32/adult each way)",
          "Afternoon: swim, explore rock pools, walk the coastal track to Apple Tree Bay",
          "Sunset from the beach — pure gold"
        ],
        "accommodation": "Anchorage DOC campsite ($20/person) or Awaroa Lodge (splurge, $400+/night)",
        "estimated_cost": "$200–380",
        "tips": [
          "Abel Tasman Aquataxi and Sea Shuttle run water taxis from Marahau — book ahead in summer.",
          "Anchorage campsite is the most family-friendly in the park (sheltered, flat, good facilities).",
          "Pack all food in. The park has no shops."
        ]
      },
      {
        "day": 2,
        "location": "Abel Tasman National Park",
        "title": "Kayak Day — Turquoise Bays and Seals",
        "drive_from_prev": null,
        "activities": [
          "Morning: Guided kayak tour from Marahau or Kaiteriteri (half-day from $95/adult, kids $65)",
          "Paddle to Split Apple Rock (iconic formation at sea level)",
          "Tonga Island seal colony kayak past (seals swim alongside your kayak)",
          "Lunch on a deserted beach — you'll likely have it to yourselves",
          "Afternoon: Walk the coastal track section Anchorage to Te Pukatea Bay (1 hr return, easy)",
          "Evening: stars from the campsite (no light pollution)"
        ],
        "accommodation": "Anchorage campsite or Marahau beachside cabin",
        "estimated_cost": "$250–420",
        "tips": [
          "Kayak NZ and Abel Tasman Sea Shuttle offer guided tours — fully guided is recommended with kids under 8.",
          "The calm morning window (before 11am) is best for kayaking. Afternoon sea breeze picks up.",
          "Wetsuits provided. Water is cold even in summer — still swimmable for most families."
        ]
      },
      {
        "day": 3,
        "location": "Abel Tasman → Golden Bay (Takaka)",
        "title": "Golden Bay — The Best Kept Secret",
        "drive_from_prev": "Takaka Hill Road: 1 hr from Motueka (marble mountain pass — spectacular)",
        "activities": [
          "Drive the Takaka Hill Road — stop at Ngarua Caves (marble caves, 45 min tour, $20/adult)",
          "Te Waihou Spring (Pupu Springs) — the world's clearest spring water, free boardwalk walk",
          "Pohara Beach — Golden Bay's best swimming beach, calm and warm",
          "Takaka town — great café culture, craft beer, and fresh local produce",
          "Option: Farewell Spit guided tour (4 hrs, $120/adult — NZ's longest sand spit)"
        ],
        "accommodation": "N/A — return to Nelson or stay Takaka",
        "estimated_cost": "$100–280",
        "tips": [
          "Pupu Springs (Te Waihou) is not to be missed — the water clarity is almost unreal.",
          "Farewell Spit is guided tours only past the lighthouse — book well ahead.",
          "The Takaka Hill drive is safe but winding — allow extra time if towing or in a campervan."
        ]
      }
    ],
    "affiliate_blocks": [
      {"type": "activities", "affiliate_key": "bookme", "cta": "Book Abel Tasman water taxis & kayak tours"},
      {"type": "accommodation", "affiliate_key": "booking_com", "cta": "Find Nelson & Motueka accommodation"},
      {"type": "rental_car", "affiliate_key": "discover_cars", "cta": "Compare campervan & car hire in Nelson"}
    ],
    "packing_tips": [
      "Sunscreen — Golden Bay and Abel Tasman UV is intense",
      "Rash vest or wetsuit top for kayaking (provided by operators but bring your own for comfort)",
      "Sandflies repellent (DEET-based) — Abel Tasman sandflies are vicious at dusk",
      "Dry bag for cameras and phones on water taxis and kayaks",
      "Snorkelling gear — Tonga Island marine reserve has great visibility"
    ],
    "faqs": [
      {"q": "Is Abel Tasman suitable for young kids?", "a": "Yes, with the right planning. Water taxi hopping (no walking required) works for any age. Guided kayaking works for kids 5+ who can sit still. The coastal track sections between bays are easy flat paths suitable for older toddlers. Anchorage campsite has good facilities for families."},
      {"q": "Do I need to camp? Are there other accommodation options?", "a": "No — you can do a day trip from Marahau on a water taxi without camping. For overnight stays, options range from DOC campsites ($20/person) to Awaroa Lodge (luxury, $400+/night). Most families do 1–2 nights camping or stay in cabins at Marahau and do day trips into the park."},
      {"q": "What time of year is best for Abel Tasman?", "a": "December–March for warmest water and reliable swimming weather. October–November is excellent — tracks are less crowded and water is swimmable. July–August is beautiful but cold for swimming. School holidays (Jan, Apr, Jul) are busy — book water taxis and campsites months ahead."}
    ]
  },

  {
    "slug": "nz-campervan-south-island-14-days",
    "title": "14-Day South Island Campervan Family Road Trip",
    "subtitle": "Picton → Nelson → West Coast → Queenstown → Dunedin → Christchurch",
    "tagline": "The ultimate South Island loop in a campervan — glaciers, fiords, wine country, penguins, and a thousand things in between",
    "duration_days": 14,
    "distance_km": 2100,
    "budget_family4": "$5,800–9,500",
    "budget_breakdown": {
      "accommodation": "$45–90/night (holiday parks)",
      "activities": "$100–250/day",
      "food": "$80–130/day (self-catering saves a lot)",
      "fuel": "~$500–700 total",
      "campervan_hire": "$1,400–2,800 for 14 days (Jucy/Britz/Maui — compare prices)"
    },
    "best_for": "Adventurous families, campervan first-timers, school summer holidays (Dec–Jan)",
    "best_season": "December–March. Shoulder (Oct–Nov, Mar–Apr) has better value and fewer crowds.",
    "transport": "Campervan (4–6 berth) — book 3–6 months ahead for summer",
    "commercial_intent_score": 96,
    "highlights": [
      "Marlborough Sounds by ferry from Wellington",
      "Abel Tasman water taxi day trip",
      "Pancake Rocks and West Coast rainforest",
      "Franz Josef Glacier walk",
      "Milford Sound cruise from Te Anau",
      "Dunedin Otago Peninsula — penguins, albatross, sea lions",
      "Aoraki/Mt Cook Hooker Valley walk"
    ],
    "days": [
      {"day": 1, "location": "Picton (ferry arrival)", "title": "Interislander Ferry → Marlborough Sounds",
       "drive_from_prev": "Wellington to Picton: 3.5 hr ferry",
       "activities": ["Interislander ferry from Wellington (book ahead, $150–220/car)", "Arrive Picton — explore the Sounds by kayak or water taxi ($30–50/adult)", "Queen Charlotte Drive to Havelock (45 min, spectacular)", "Set up camp at Linkwater or Havelock"],
       "accommodation": "Havelock Motor Camp", "estimated_cost": "$180–320",
       "tips": ["Book the Interislander ferry 4–6 weeks ahead — campervans pay by metre length.", "The Interislander scenic sailing through the Sounds is spectacular — sit on deck."]},
      {"day": 2, "location": "Marlborough → Nelson", "title": "Wine Country to NZ's Sunshine Capital",
       "drive_from_prev": "2 hrs via Blenheim and SH6",
       "activities": ["Brancott Estate Blenheim — vineyard walk, restaurant, and kids playground (free to visit)", "Nelson Arts Quarter walk (free, great street art)", "Nelson Saturday Market (if weekend)", "Tahuna Beach — Nelson's best family swimming beach"],
       "accommodation": "Nelson holiday park", "estimated_cost": "$80–160",
       "tips": ["Nelson gets more sunshine than anywhere else in NZ. It's consistently warm.", "Tahuna Beach has excellent facilities — playground, changing rooms, café."]},
      {"day": 3, "location": "Nelson → Abel Tasman (Marahau)", "title": "Abel Tasman Water Taxi Day",
       "drive_from_prev": "1 hr to Marahau",
       "activities": ["Water taxi to Anchorage Bay (book ahead, $32/adult)", "Beach, swimming, coastal walk to Apple Tree Bay", "Option: half-day guided kayak ($90/adult)", "Return water taxi to Marahau"],
       "accommodation": "Marahau or Motueka campsite", "estimated_cost": "$200–380",
       "tips": ["Leave your campervan at the Marahau car park and do the park on foot/water taxi.", "Pack lunch — no shops in the park."]},
      {"day": 4, "location": "Motueka → Golden Bay → Westport", "title": "Takaka Hill and the Wild West Coast",
       "drive_from_prev": "3.5 hrs via Takaka Hill and SH60",
       "activities": ["Pupu Springs (Te Waihou) — 10 min boardwalk, free, world-clearest spring", "Pohara Beach swim", "Cross the Takaka Hill back to Motueka then head south on SH6", "Arrive Westport — Cape Foulwind Seal Colony (free, 45 min walk)"],
       "accommodation": "Westport holiday park", "estimated_cost": "$80–150",
       "tips": ["Cape Foulwind seal colony is free and excellent — 100+ NZ fur seals on the rocks."]},
      {"day": 5, "location": "Westport → Punakaiki → Greymouth", "title": "Pancake Rocks and the Wild West Coast",
       "drive_from_prev": "2.5 hrs",
       "activities": ["Pancake Rocks at Punakaiki — 15 min loop walk, free, spectacular blowholes", "Truman Track (30 min return, coastal rainforest, free)", "Greymouth — Monteith's Brewery tour ($20/adult)", "Hokitika Gorge detour (40 min east, turquoise water, free)"],
       "accommodation": "Greymouth or Hokitika holiday park", "estimated_cost": "$80–140",
       "tips": ["Pancake Rocks blowholes are best at high tide — check tide times before you go.", "Hokitika Gorge is 100% worth the detour — turquoise water in a narrow schist gorge."]},
      {"day": 6, "location": "Hokitika → Franz Josef Glacier", "title": "Rainforest Meets Ice",
       "drive_from_prev": "2 hrs south via SH6",
       "activities": ["Franz Josef township — gear up", "Valley floor walk (free, 1 hr return) to glacier viewpoint", "Heli-hike if budget allows ($350/adult — spectacular, minimum age 8)", "Roberts Point Track (2–3 hrs, for older kids)", "Cook flat walk for river views"],
       "accommodation": "Franz Josef township holiday park", "estimated_cost": "$100–400",
       "tips": ["Heli-hikes depend on weather — don't plan your trip around them.", "The free valley floor walk gets you to within 500m of the ice face — very impressive."]},
      {"day": 7, "location": "Franz Josef → Fox Glacier → Haast → Wanaka", "title": "The Haast Pass — South Island's Wild Heart",
       "drive_from_prev": "4 hrs via Fox Glacier and Haast",
       "activities": ["Fox Glacier Lake Matheson (mirror lake, 1 hr walk, free — perfect at sunrise)", "Haast Pass Scenic Route — Knights Point lookout, Thunder Creek Falls", "Arrive Wanaka — Puzzling World ($20/adult)", "Lake Wanaka swim and waterfront walk"],
       "accommodation": "Wanaka holiday park", "estimated_cost": "$120–280",
       "tips": ["Lake Matheson is best at sunrise or shortly after — get up early.", "Haast Pass is spectacular and empty. Stop at every lookout."]},
      {"day": 8, "location": "Wanaka", "title": "Wanaka Rest Day",
       "drive_from_prev": null,
       "activities": ["Kayak or paddleboard on Lake Wanaka", "That Wanaka Tree (15 min walk, iconic photo)", "Rippon Vineyard (free walk, incredible lake views)", "Mount Iron Track (1.5 hrs, great views over Wanaka)", "Free evening — campfire, stars"],
       "accommodation": "Wanaka holiday park (same)", "estimated_cost": "$80–180",
       "tips": ["Wanaka is where you breathe. Don't over-schedule this day."]},
      {"day": 9, "location": "Wanaka → Queenstown via Arrowtown", "title": "Crown Range and Arrowtown Gold",
       "drive_from_prev": "2 hrs via Crown Range (SH89)",
       "activities": ["Crown Range summit viewpoint (free, stunning)", "Arrowtown — gold panning ($5), Arrow River walk, Chinese Settlement", "Arrive Queenstown, lakefront walk", "Gondola for sunset ($40/adult)"],
       "accommodation": "Queenstown holiday park", "estimated_cost": "$120–280",
       "tips": ["Arrowtown is the best small town in the South Island. Give it 3 hrs."]},
      {"day": 10, "location": "Queenstown", "title": "Adventure Capital Day",
       "drive_from_prev": null,
       "activities": ["Skyline Gondola + Luge ($55/adult multi-ride)", "Queenstown Gardens frisbee golf (free)", "TSS Earnslaw steamship cruise ($69/adult)", "Fergburger queue — worth every minute"],
       "accommodation": "Queenstown holiday park (same)", "estimated_cost": "$200–400",
       "tips": ["Queenstown on a budget: pack breakfast, use the holiday park kitchen, picnic lunch."]},
      {"day": 11, "location": "Queenstown → Te Anau → Milford Sound", "title": "Milford Sound — NZ's Greatest Experience",
       "drive_from_prev": "4 hrs to Milford via Te Anau",
       "activities": ["Drive Te Anau to Milford (2 hrs, one of NZ's great drives)", "Mirror Lakes (free, 5 min stop)", "Homer Tunnel — watch for kea (mountain parrots)", "Milford Sound cruise (2 hrs, $80–130/adult) — waterfalls and dolphins", "Return to Te Anau (2 hrs drive)"],
       "accommodation": "Te Anau holiday park", "estimated_cost": "$250–450",
       "tips": ["Book Milford Sound cruise well ahead — Real Journeys and Go Orange are best.", "Leave Te Anau by 7:30am. Return by 6pm."]},
      {"day": 12, "location": "Te Anau → Dunedin", "title": "Drive to Dunedin — Penguin Coast",
       "drive_from_prev": "4 hrs via Gore and the Catlins",
       "activities": ["Optional Catlins detour (Purakaunui Falls, Nugget Point) — adds 2 hrs", "Arrive Dunedin", "Otago Settlers Museum (free)", "Baldwin Street — world's steepest street (free, fun photo stop)"],
       "accommodation": "Dunedin holiday park", "estimated_cost": "$80–200",
       "tips": ["The Catlins is spectacular and completely empty. Add 2 days if you can."]},
      {"day": 13, "location": "Dunedin — Otago Peninsula", "title": "Penguins, Albatross, and Sea Lions",
       "drive_from_prev": null,
       "activities": ["Oamaru Blue Penguin Colony (1.5 hrs north — evening viewing is best, $35/adult)", "OR Otago Peninsula wildlife tour — yellow-eyed penguins, sea lions, albatross ($90/adult)", "Larnach Castle (30 min from Dunedin, NZ's only castle, $28/adult)", "Dunedin Railway Station (free to view exterior)"],
       "accommodation": "Dunedin holiday park (same)", "estimated_cost": "$150–350",
       "tips": ["Oamaru penguin colony evening viewing has 100+ penguins coming in — extraordinary.", "Yellow-eyed penguins are critically endangered — guided tours only on the Otago Peninsula."]},
      {"day": 14, "location": "Dunedin → Christchurch (via Moeraki + Mt Cook)", "title": "Drive Home via Moeraki Boulders and Lake Tekapo",
       "drive_from_prev": "5–6 hrs direct, or longer via Mt Cook",
       "activities": ["Moeraki Boulders (1 hr north, free, 20 min walk on beach)", "Continue north on SH1", "Optional: Aoraki/Mt Cook turnoff (Hooker Valley Track, adds 3 hrs)", "Lake Tekapo sunset/stargazing (Church of the Good Shepherd)", "Return campervan in Christchurch"],
       "accommodation": "N/A — return vehicle",
       "estimated_cost": "$100–200",
       "tips": ["Book your return flight from CHC for the evening — gives time to clean/return the van.", "Moeraki Boulders at low tide are best — check the tide before you go."]}
    ],
    "affiliate_blocks": [
      {"heading": "Book Your Campervan", "affiliate_key": "discover_cars", "cta": "Compare South Island campervans", "text": "Jucy, Maui, Britz, Mighty and Wilderness Motorhomes — 14-day South Island hire from $1,400. Book 3–6 months ahead for summer."},
      {"affiliate_key": "bookme", "cta": "Book activities along the route"},
      {"affiliate_key": "booking_com", "cta": "Find holiday parks (backup if campsites full)"},
      {"affiliate_key": "covermore", "cta": "Get family travel insurance"}
    ],
    "packing_tips": [
      "Sandfly repellent (DEET) — West Coast and Fiordland sandflies are legendary",
      "Layers — you'll go from 30°C Wanaka to 8°C Franz Josef in one day",
      "Campervan kitchen kit: sharp knife, good cutting board, cast iron pan, coffee plunger",
      "Tow rope and portable jump start (just in case — remote roads)",
      "One warm sleeping bag per person — South Island nights are cold even in summer"
    ],
    "faqs": [
      {"q": "Which campervan company is best for families?", "a": "Britz and Maui have the most family-focused campervans (2-berth + bunks, or 6-berth). Jucy is the cheapest and works well for smaller families. Wilderness Motorhomes has the best-equipped vans. Compare all on Discover Cars — prices vary enormously by availability."},
      {"q": "Do we need to book holiday parks in advance?", "a": "In summer (Dec–Jan) absolutely yes — especially Queenstown, Franz Josef, and Te Anau. Book these 4–6 weeks ahead. Other holiday parks are generally fine to turn up, but calling ahead never hurts. DOC campsites are first-come first-served."},
      {"q": "Is 14 days enough for the South Island?", "a": "14 days is the sweet spot — you'll see the highlights without rushing. 10 days is tight but doable (skip the Catlins and combine some days). 21 days is ideal if you want to add the Catlins properly, do multi-day walks, and linger in great spots."}
    ]
  },

  {
    "slug": "wellington-to-auckland-north-island-classic-7-days",
    "title": "Wellington to Auckland — 7-Day North Island Classic Road Trip",
    "subtitle": "Wellington → Whanganui → Tongariro → Taupo → Rotorua → Hobbiton → Auckland",
    "tagline": "The great North Island drive — national parks, volcanic landscapes, geothermal wonders, and the world's best movie set",
    "duration_days": 7,
    "distance_km": 800,
    "budget_family4": "$3,800–6,200",
    "budget_breakdown": {
      "accommodation": "$140–320/night",
      "activities": "$100–280/day",
      "food": "$75–130/day",
      "fuel": "~$160 total"
    },
    "best_for": "Families with kids 3+, especially those doing a one-way North Island trip",
    "best_season": "October–April (Tongariro crossing only safe November–April)",
    "transport": "Rental car (one-way WLG → AKL common)",
    "commercial_intent_score": 94,
    "highlights": [
      "Te Papa Museum Wellington (free — NZ's best museum)",
      "Whanganui River jet boat",
      "Tongariro National Park — volcanic plateau scenery",
      "Huka Falls and Lake Taupo",
      "Rotorua geothermal and cultural experience",
      "Hobbiton Movie Set — Matamata",
      "Hamilton Gardens (free)"
    ],
    "days": [
      {"day": 1, "location": "Wellington", "title": "Capital City — Te Papa and the Waterfront",
       "drive_from_prev": null,
       "activities": ["Te Papa Museum — full day, free (New Zealand's greatest museum)", "Cuba Street for lunch ($12–18 food court options)", "Wellington Cable Car to Botanic Gardens (free return walk down)", "Wellington waterfront evening walk"],
       "accommodation": "Wellington CBD", "estimated_cost": "$60–150",
       "tips": ["Te Papa is genuinely world-class — allow 4 hrs minimum. Free.", "Wellington is very compact — walk everywhere in the CBD."]},
      {"day": 2, "location": "Wellington → Whanganui", "title": "Palmerston North and the Whanganui River",
       "drive_from_prev": "2.5 hrs via SH1",
       "activities": ["Palmerston North — Te Manawa Museum (free, good for kids)", "Arrive Whanganui — riverside walk and city murals (free)", "Durie Hill Elevator ($2, old elevator to hilltop views)", "Whanganui Regional Museum (free)"],
       "accommodation": "Whanganui holiday park", "estimated_cost": "$60–150",
       "tips": ["Whanganui is underrated and has a great art scene. Give it an afternoon."]},
      {"day": 3, "location": "Whanganui → Ohakune → Tongariro", "title": "National Park — Volcanic Plateau",
       "drive_from_prev": "2 hrs via Ohakune (SH4)",
       "activities": ["Ohakune Carrot Sculpture (free, excellent photo op)", "Ohakune Mountain Road to the ski area (DOC walks from $0)", "Arrive Tongariro National Park — Whakapapa Village", "Tawhai Falls short walk (30 min return, free, beautiful waterfall)"],
       "accommodation": "Whakapapa Holiday Park or National Park Village", "estimated_cost": "$80–200",
       "tips": ["Tongariro Alpine Crossing (19km, 7–8 hrs) is for teens + fit adults only — not for young kids.", "The short walks around Whakapapa are excellent and suitable for all ages."]},
      {"day": 4, "location": "Tongariro → Taupo", "title": "Huka Falls and Lake Taupo",
       "drive_from_prev": "1.5 hrs via SH1",
       "activities": ["Huka Falls (free, 10 min walk — massive water flow)", "Huka Jet boat ride (thrilling, $59/adult, 30 min)", "Taupo town and lakefront", "Volcanic Activity Centre ($8/adult)", "Evening — Taupo i-SITE for Māori rock carvings cruise"],
       "accommodation": "Taupo holiday park (on the lake)", "estimated_cost": "$130–280",
       "tips": ["Taupo holiday parks on the lake are exceptional — wake up to Mount Ruapehu views.", "Book the evening mine bay Māori carvings boat cruise — these rock carvings are only accessible by water."]},
      {"day": 5, "location": "Taupo → Rotorua", "title": "Geothermal Rotorua",
       "drive_from_prev": "1 hr via SH5",
       "activities": ["Wai-O-Tapu Thermal Wonderland (Lady Knox Geyser 10:15am, $35/adult)", "Lunch on Eat Streat Rotorua", "Skyline Gondola + Luge (multi-ride pass)", "Te Puia — geysers and Māori culture ($55/adult)"],
       "accommodation": "Rotorua holiday park", "estimated_cost": "$200–380",
       "tips": ["Leave Taupo by 9am to catch the Lady Knox geyser. It erupts once only — 10:15am daily."]},
      {"day": 6, "location": "Rotorua → Matamata (Hobbiton) → Hamilton", "title": "Hobbiton and Hamilton Gardens",
       "drive_from_prev": "30 min to Matamata, 1.5 hrs to Hamilton",
       "activities": ["Hobbiton Movie Set Tour (2.5 hrs, $49/adult, book ahead)", "Green Dragon Inn drink included", "Hamilton Gardens (free — 54 themed gardens, allow 2 hrs)", "Hamilton riverside walk"],
       "accommodation": "Hamilton motel or holiday park", "estimated_cost": "$150–300",
       "tips": ["Hobbiton books out weeks ahead in school holidays — book before your trip.", "Hamilton Gardens are consistently rated one of NZ's best free attractions."]},
      {"day": 7, "location": "Hamilton → Auckland", "title": "Waitomo Caves Option + Auckland Arrival",
       "drive_from_prev": "1.5 hrs direct, or 3 hrs via Waitomo",
       "activities": ["Option A: Waitomo Glowworm Caves detour (45 min off route, $55/adult)", "Option B: Drive direct to Auckland, afternoon at the waterfront", "Kelly Tarlton's Sea Life Aquarium ($32/adult, good if you have kids under 10)", "Return rental car at Auckland Airport"],
       "accommodation": "N/A — end of trip",
       "estimated_cost": "$100–250",
       "tips": ["Waitomo on the last day is tight if flying same-day — allow 2 hrs for the cave + drive.", "Reserve your rental car drop-off time to avoid fees."]}
    ],
    "affiliate_blocks": [
      {"heading": "Book a One-Way Rental Car", "affiliate_key": "discover_cars", "cta": "Compare one-way WLG → AKL car hire", "text": "One-way rentals Wellington → Auckland are common. Budget extra $100–200 for the one-way fee. SUVs and automatics are most popular."},
      {"affiliate_key": "bookme", "cta": "Pre-book Hobbiton, Waitomo & Rotorua"},
      {"affiliate_key": "booking_com", "cta": "Find accommodation along the route"}
    ],
    "packing_tips": [
      "Layers for Tongariro (wind and cold even in summer at altitude)",
      "Swimwear for Taupo lake and Rotorua hot pools",
      "Good walking shoes for Tawhai Falls and Hooker Valley",
      "Snacks for the Tongariro stretch — options are limited"
    ],
    "faqs": [
      {"q": "Can I do this route in reverse (Auckland to Wellington)?", "a": "Yes — identical content works just as well north-to-south. If flying Auckland → Wellington, you reverse the days and can do Waitomo on day 1 (from Auckland, 2.5 hrs) before heading south."},
      {"q": "What's the best stop on this route for families?", "a": "Rotorua is the undisputed highlight — the geothermal parks, luge, and cultural experiences are outstanding for all ages. Hobbiton is a close second, especially with kids who've seen the films."},
      {"q": "Is Tongariro National Park worth it for families with young kids?", "a": "The park is worth it for the scenery and short walks even if you don't do the Alpine Crossing. The Tawhai Falls walk (30 min) and Whakapapa Village boardwalk are suitable for all ages. In winter, the ski field at Whakapapa is great for family ski lessons."}
    ]
  },

  {
    "slug": "nz-ski-family-holiday-queenstown-7-days",
    "title": "NZ Family Ski Holiday — 7 Days in Queenstown & Wanaka",
    "subtitle": "Queenstown → The Remarkables → Cardrona → Wanaka",
    "tagline": "The South Island's best ski fields — The Remarkables, Coronet Peak, Cardrona, and Treble Cone — with world-class family snow facilities",
    "duration_days": 7,
    "distance_km": 180,
    "budget_family4": "$6,500–12,000",
    "budget_breakdown": {
      "accommodation": "$300–700/night (peak winter)",
      "activities": "$800–1,500 for ski passes (family passes better value)",
      "food": "$120–200/day",
      "fuel": "~$100 total",
      "ski_hire": "$200–400 for family (hire in town, not on mountain)"
    },
    "best_for": "Families with kids 4+, first-time skiers (Cardrona), advanced skiers (Treble Cone)",
    "best_season": "July–August (peak ski season). July school holidays are the busiest. Book months ahead.",
    "transport": "Rental car (AWD/4WD recommended, chains available at rental desks)",
    "commercial_intent_score": 91,
    "highlights": [
      "The Remarkables ski area (best learner terrain near Queenstown)",
      "Cardrona Alpine Resort (NZ's best family ski mountain)",
      "Coronet Peak (night skiing, great advanced terrain)",
      "Queenstown snow tubing at Snowz",
      "Arrowtown in the snow",
      "Wanaka skiing at Treble Cone or Cardrona"
    ],
    "days": [
      {"day": 1, "location": "Queenstown", "title": "Arrival — Gear Up and Explore",
       "drive_from_prev": null,
       "activities": ["Arrive Queenstown, pick up rental car", "Hire ski gear in town (Altitude Sports, Outside Sports — much cheaper than on-mountain)", "Queenstown gondola for snow views ($40/adult)", "Explore the lakefront, dinner at The Cow pizza"],
       "accommodation": "Queenstown (central is best for ski shuttle access)", "estimated_cost": "$200–400",
       "tips": ["Hire ski gear in Queenstown CBD — 30–40% cheaper than on-mountain hire.", "Book ski lessons for kids on day 2 before you arrive — instructors fill up fast."]},
      {"day": 2, "location": "The Remarkables Ski Area", "title": "First Day on Snow",
       "drive_from_prev": "45 min from Queenstown (road access, shuttle available)",
       "activities": ["The Remarkables learner area is excellent (Happy Valley — very gentle)", "Group ski lessons for beginners ($120/person)", "Family terrain park", "Snow tubing at Queenstown Snowz (if Remarkables is too advanced for young kids)"],
       "accommodation": "Queenstown (same)", "estimated_cost": "$400–700 (lift passes + lessons)",
       "tips": ["The Remarkables family pass is much better value than individual lift passes.", "Snow Play area at The Remarkables suits kids who aren't ready to ski."]},
      {"day": 3, "location": "Coronet Peak", "title": "Advanced Terrain Day",
       "drive_from_prev": "30 min from Queenstown",
       "activities": ["Coronet Peak — NZ's oldest ski field, excellent groomed runs", "Night skiing Thursday–Saturday ($72/adult, 4pm–8pm) — a unique NZ experience", "Apres-ski in Queenstown (The World Bar, Minus 5° Ice Bar for novelty)"],
       "accommodation": "Queenstown (same)", "estimated_cost": "$350–650",
       "tips": ["Buy a Queenstown ski combo pass (Remarkables + Coronet Peak) — saves 20% over individual days.", "Coronet Peak night skiing is open until late — wonderful atmosphere."]},
      {"day": 4, "location": "Arrowtown + Rest Day", "title": "Arrowtown and Snow Day",
       "drive_from_prev": "20 min from Queenstown",
       "activities": ["Arrowtown in snow — the most beautiful winter village in NZ", "Arrow River walk (free)", "Chinese Settlement (free)", "Lakes District Museum ($8/adult)", "Afternoon: spa or rest day, Queenstown Ice Arena if kids want a break from skiing"],
       "accommodation": "Queenstown (same)", "estimated_cost": "$80–200",
       "tips": ["Build in a rest/town day — ski legs need recovery, especially for young kids."]},
      {"day": 5, "location": "Cardrona Alpine Resort", "title": "NZ's Best Family Ski Mountain",
       "drive_from_prev": "1 hr from Queenstown via Crown Range",
       "activities": ["Cardrona — widely rated NZ's best family ski resort", "Excellent beginners' area and ski school", "Super Pipe for experienced skiers", "Snow tubing park for non-skiers and toddlers", "Stay in Wanaka tonight (30 min from Cardrona)"],
       "accommodation": "Wanaka (base for remaining days)", "estimated_cost": "$400–700",
       "tips": ["Cardrona has the best kids' ski school in NZ. Book in advance.", "The drive from Wanaka to Cardrona (30 min) is an easy commute."]},
      {"day": 6, "location": "Treble Cone", "title": "Advanced Mountain for Confident Skiers",
       "drive_from_prev": "20 min from Wanaka",
       "activities": ["Treble Cone — NZ's best advanced skiing, steep and challenging", "Not suitable for beginners — return to Cardrona if kids need more ski school", "Wanaka lakefront walk in the afternoon (ski legs recovery)", "Puzzling World if kids are tired of skiing ($20/adult)"],
       "accommodation": "Wanaka (same)", "estimated_cost": "$350–600",
       "tips": ["Treble Cone has dramatic views over Lake Wanaka — even if you don't ski, go up for the gondola views."]},
      {"day": 7, "location": "Wanaka → Queenstown → Depart", "title": "Last Day — Snow Play and Departure",
       "drive_from_prev": "1 hr from Wanaka",
       "activities": ["Morning: snow play or easy ski run at Cardrona", "Crown Range drive back to Queenstown (stunning winter views)", "Return ski hire, airport transfer", "Fergburger queue — mandatory last meal"],
       "accommodation": "N/A", "estimated_cost": "$100–200",
       "tips": ["Return ski gear the night before if your flight is early.", "Queenstown Airport has excellent facilities — arrive 90 min before domestic, 2 hrs international."]}
    ],
    "affiliate_blocks": [
      {"heading": "Book Accommodation Early", "affiliate_key": "booking_com", "cta": "Find Queenstown & Wanaka ski accommodation", "text": "Queenstown July school holidays book out 3–6 months ahead. Wanaka is quieter and better value."},
      {"affiliate_key": "discover_cars", "cta": "Compare AWD rental cars for the ski fields"},
      {"affiliate_key": "bookme", "cta": "Book ski lessons and Queenstown activities"}
    ],
    "packing_tips": [
      "Ski thermals and mid-layers (merino wool is best)",
      "Waterproof ski pants and jacket (non-negotiable — rental available in town)",
      "Hand and toe warmers for young kids",
      "Neck gaiter and goggles (goggles are cheaper to hire in town than on-mountain)",
      "High-SPF sunscreen — snow reflects UV intensely"
    ],
    "faqs": [
      {"q": "Which ski field is best for beginners in Queenstown?", "a": "The Remarkables has the best beginner-specific terrain (Happy Valley) and is closest to Queenstown. Cardrona (1 hr away near Wanaka) is rated NZ's best family ski resort overall with excellent ski school. For absolute first-timers, Cardrona's learner area is the most gentle and well-designed."},
      {"q": "When are NZ school ski holidays?", "a": "NZ school winter holidays run approximately 5 July – 18 July 2026. This is the busiest 2-week period for ski fields — book accommodation and ski lessons 3–4 months ahead. Outside school holidays (June and August) the fields are quieter and accommodation is cheaper."},
      {"q": "Is a ski holiday in NZ worth it vs Australia?", "a": "NZ ski fields have longer vertical drops, more varied terrain, and better guaranteed snow than most Australian resorts. The scenery (Lake Wakatipu, Lake Wanaka) is unmatched. Costs are similar to Thredbo or Falls Creek but with a longer season (June–September). For NZ families, it's almost always worth the South Island trip."}
    ]
  }

]

# ── 4 NEW TRAVEL GUIDES ───────────────────────────────────────────────────────

NEW_GUIDES = [

  {
    "slug": "best-nz-beaches-families",
    "short_title": "Best NZ Beaches for Families",
    "title": "20 Best Beaches in New Zealand for Families — With Kids of All Ages",
    "meta_desc": "The 20 best family beaches in NZ — from patrolled surf beaches to hidden coves. Includes swimming safety ratings, facilities, and nearest towns.",
    "intro": "New Zealand has over 15,000km of coastline and more than 200 surf beaches — but not all are equal for families. Here are the 20 best, chosen for calm water, lifeguard patrols, facilities, and the kind of magic that makes kids want to stay all day.",
    "updated": "May 2026",
    "reading_time": 8,
    "hero_image": {
      "url": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=1200&q=80",
      "thumb": "https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=600&q=70",
      "alt": "Family on a New Zealand beach in summer",
      "credit": "Unsplash / Devin Avery"
    },
    "sections": [
      {
        "heading": "North Island — The Top Family Beaches",
        "body": "<p>The North Island has NZ's warmest water (19–23°C in summer) and most of the patrolled beaches. Ocean Beach in Hawke's Bay and Ohope Beach near Whakatāne are perennial family favourites — long, flat, and rarely crowded. Mount Maunganui in Tauranga is the most popular family beach in NZ: patrolled every summer day, gentle waves, excellent facilities.</p><p>For absolute calm water, the Coromandel Peninsula's east coast (Whitianga, Hahei, Cooks Beach) and the Bay of Islands have sheltered harbours where young children can paddle safely. Hot Water Beach — where you dig your own spa at low tide — is in a class of its own.</p>",
        "list": [
          "Mount Maunganui (Tauranga) — NZ's best-patrolled beach, excellent facilities, gentle surf",
          "Ohope Beach (Whakatāne) — long, flat, almost always calm, great holiday park right behind the beach",
          "Hot Water Beach (Coromandel) — dig your own thermal spa at low tide (2 hrs either side)",
          "Hahei Beach (Coromandel) — sheltered cove near Cathedral Cove, calm water, small café",
          "Ocean Beach (Hawke's Bay) — 10km stretch, lifeguarded, dolphins often visible offshore",
          "Onetangi Beach (Waiheke Island) — long white sand, easy ferry from Auckland, fantastic"
        ]
      },
      {
        "heading": "South Island — Wild Beauty and Sheltered Bays",
        "body": "<p>South Island beaches are wilder, colder, and often completely empty. Water temperatures of 14–18°C in summer still allow swimming — NZ kids are tough. Kaiteriteri (near Nelson) is the golden exception: warm, sheltered, and the gateway to Abel Tasman National Park. Pohara Beach in Golden Bay is even better — clear warm water and almost no one there.</p><p>For drama without swimming, the West Coast's black sand beaches (Hokitika, Westport) and the Otago Peninsula's seal colonies and yellow-eyed penguin beaches are unforgettable. Blenheim has the sheltered Waikawa Bay. Dunedin's St Clair Beach is urban, patrolled, and has a famous hot salt water pool right on the beach.</p>",
        "list": [
          "Kaiteriteri Beach (Nelson/Tasman) — golden sand, warm, sheltered, good facilities, Abel Tasman gateway",
          "Pohara Beach (Golden Bay) — warmer than anywhere in the South Island, rarely crowded",
          "St Clair Beach (Dunedin) — patrolled, urban, excellent hot salt water pool right on the beach",
          "Totaranui Beach (Abel Tasman NP) — pure white sand, accessible by water taxi only — reward for effort",
          "Waikawa Bay (Marlborough) — sheltered, calm, great for younger kids"
        ]
      },
      {
        "heading": "Beach Safety in New Zealand — What Every Family Must Know",
        "body": "<p>New Zealand beaches can be dangerous. Rip currents cause most drowning deaths in NZ every year, and they're hardest to see on popular sandy beaches. Swim only at patrolled beaches (red and yellow flags) and stay between the flags at all times. Never swim at unpatrolled beaches unless you're an experienced swimmer who knows how to identify and escape a rip.</p><p>A rip current looks like a dark, choppy channel of water between sandbars — it pulls you offshore fast. If you're caught, don't fight it. Float, signal for help, and swim parallel to the beach until you're out of the rip, then back to shore at an angle.</p>",
        "list": [
          "Always swim between the red and yellow flags — these are the safest, patrolled zones",
          "Lifeguards patrol most popular beaches October–April, 10am–6pm",
          "Check Beach Safe NZ (beachsafe.org.nz) for patrol status before you visit",
          "Teach kids the rip current rule: float, don't fight, swim sideways",
          "Jellyfish (bluebottles) sting seasonally — treat with hot water (not cold), not vinegar"
        ]
      },
      {
        "heading": "Top Beach Gear for NZ Families",
        "body": "<p>Pack sunscreen rated SPF50+ — NZ has one of the world's highest UV indexes due to the thinning ozone layer. Reapply every 2 hours. Rash vests are standard NZ beach wear for kids — far better than reapplying sunscreen constantly. Sandfly repellent (DEET-based) is essential in coastal South Island spots at dusk.</p>",
        "list": [
          "SPF50+ sunscreen — reapply every 2 hrs, NZ UV is serious",
          "Rash vest for kids — UPF50+ is standard at NZ surf shops",
          "Boogie board — $30 from Kmart, delivers hours of entertainment at any beach",
          "Sandfly repellent for South Island beaches at dusk",
          "Waterproof dry bag for phones and cameras"
        ],
        "cta": {
          "text": "Find accommodation near NZ beaches →",
          "url": "https://www.booking.com/searchresults.html?ss=New+Zealand&group_adults=2&group_children=2",
          "affiliate": True
        }
      }
    ]
  },

  {
    "slug": "free-things-to-do-nz-families",
    "short_title": "Free Things in NZ for Kids",
    "title": "50 Free Things to Do in New Zealand with Kids — The Complete Family Guide",
    "meta_desc": "50 genuinely free things to do in NZ with kids — free museums, beaches, waterfalls, parks, wildlife, and markets. Updated 2026.",
    "intro": "New Zealand can be expensive for families — but the best things are often free. National parks, world-class museums, volcanic wonders, and wildlife encounters that cost nothing. Here are 50 completely free things to do with kids in NZ, organised by region.",
    "updated": "May 2026",
    "reading_time": 9,
    "hero_image": {
      "url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80",
      "thumb": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&q=70",
      "alt": "Kids exploring New Zealand mountains and nature",
      "credit": "Unsplash / Tim Swaan"
    },
    "sections": [
      {
        "heading": "Free Things in Auckland (10 picks)",
        "body": "<p>Auckland has excellent free options — the waterfront, regional parks, and volcanic cones are all free. The Auckland Museum charges entry but has free outdoor grounds; the Auckland Art Gallery is free for under-18s every day.</p>",
        "list": [
          "Auckland Waterfront (Wynyard Quarter) — free playground, ocean views, Saturday market",
          "One Tree Hill / Cornwall Park — extinct volcano, farm animals, free walking",
          "Muriwai Gannet Colony — 45 min west, hundreds of nesting gannets on the clifftop, free",
          "Auckland Domain park and duck pond (free, next to the museum)",
          "Devonport village (free ferry walk on a Sunday if paying for adults — kids under 5 free ferry)",
          "Henderson Valley Park — walking tracks, free BBQs",
          "Te Atatu Peninsula Park — great playground, harbour views",
          "Auckland Botanic Gardens (Manurewa) — 64 hectares, completely free",
          "Waiatarua Reserve wetland walk (free, birdlife)",
          "Long Bay Regional Park — beach, walking tracks, free (pay parking)"
        ]
      },
      {
        "heading": "Free Things in Rotorua, Taupo & Waikato",
        "body": "<p>Rotorua's geothermal wonders include free public experiences like Kuirau Park (boiling mud on city streets). Taupo's Huka Falls is NZ's most visited free natural attraction.</p>",
        "list": [
          "Kuirau Park, Rotorua — boiling mud pools, free foot baths on the street, free entry",
          "Huka Falls, Taupo — NZ's most visited natural attraction, completely free",
          "Wai-O-Tapu short viewpoints from public road (the best views are free, full park charges entry)",
          "Hamilton Gardens — 54 themed gardens, 58 hectares, completely free",
          "Waikato Museum, Hamilton — free entry, excellent hands-on exhibits for kids",
          "Blue Spring (Te Waihou Puna), Cambridge — world-clearest spring water, 45 min walk, free",
          "Lake Taupo foreshore and swim beach — free, beautiful",
          "Aratiatia Rapids, Taupo — dam release creates rapids, free viewing (10am, 12pm, 2pm, 4pm daily)",
          "Orakei Korako viewpoint from road (full park entry charged)"
        ]
      },
      {
        "heading": "Free Things in Wellington & Lower North Island",
        "body": "<p>Wellington has the highest density of free world-class cultural attractions in NZ. Te Papa Museum alone can fill two days at zero cost.</p>",
        "list": [
          "Te Papa Museum, Wellington — NZ's national museum, completely free, extraordinary",
          "Wellington Botanic Gardens — free, beautiful, rose garden, cable car walk-down",
          "Zealandia wildlife sanctuary — outside viewing free (full sanctuary entry charged)",
          "Pukaha Mount Bruce, near Masterton — kiwi feeding 1:30pm daily, free",
          "Carter Observatory Wellington — free grounds, telescope sessions extra",
          "Wellington Waterfront and Oriental Bay beach (free swimming)",
          "Paraparaumu Beach and Kāpiti Coast walking tracks"
        ]
      },
      {
        "heading": "Free Things in the South Island",
        "body": "<p>The South Island's greatest attractions are landscapes — and landscapes are free. The drive from Christchurch to Queenstown via Mt Cook and Tekapo is one of the great free road trips on earth.</p>",
        "list": [
          "Church of the Good Shepherd, Lake Tekapo — the most photographed building in NZ, free",
          "Lake Pūkaki lookout — the most vivid blue lake you'll ever see, free",
          "Hooker Valley Track, Aoraki/Mt Cook — NZ's best day walk, completely free",
          "Pancake Rocks, Punakaiki — 15 min free walk, spectacular coastal formations",
          "Hokitika Gorge — 30 min return walk, turquoise water, free",
          "Moeraki Boulders — giant spherical boulders on the beach, free",
          "Christchurch Botanic Gardens — extraordinary, free",
          "Milford Road — Mirror Lakes, Homer Tunnel, Valley of Sound — free to drive",
          "Cape Reinga Lighthouse walkway — the spiritual tip of NZ, free",
          "Arrowtown riverside walk and Chinese Settlement — free",
          "Kaikōura Seal Colony (Point Kean) — hundreds of seals, free",
          "Curio Bay Petrified Forest — fossilised forest on the beach, free"
        ],
        "cta": {
          "text": "Find cheap NZ family accommodation →",
          "url": "https://www.booking.com/searchresults.html?ss=New+Zealand&group_adults=2&group_children=2",
          "affiliate": True
        }
      }
    ]
  },

  {
    "slug": "north-island-vs-south-island-families",
    "short_title": "North vs South Island NZ",
    "title": "North Island vs South Island NZ — Which is Better for Families?",
    "meta_desc": "North Island vs South Island NZ for families — compare weather, costs, driving, wildlife, and best activities. Which should you visit first?",
    "intro": "It's the most common question for first-time NZ visitors: North Island or South Island? The honest answer is they're very different holidays. Here's how they compare for families with kids — and which you should prioritise based on ages, budget, and what you want to see.",
    "updated": "May 2026",
    "reading_time": 7,
    "hero_image": {
      "url": "https://images.unsplash.com/photo-1549887534-1541e9326642?w=1200&q=80",
      "thumb": "https://images.unsplash.com/photo-1549887534-1541e9326642?w=600&q=70",
      "alt": "New Zealand landscape comparison aerial view",
      "credit": "Unsplash / David Edelstein"
    },
    "sections": [
      {
        "heading": "The North Island — Culture, Geothermal, and Beaches",
        "body": "<p>The North Island is warmer, more compact, and better for families with young children. The key attractions — Auckland, Rotorua's geothermal parks, Waitomo Caves, Hobbiton, Taupo, and Wellington — are all within a 7-day road trip. The water is warmer (19–23°C in summer), the beaches are patrolled, and the cultural experiences (Māori culture at Rotorua, Te Papa in Wellington) are world-class.</p><p>Driving distances are shorter: Auckland to Rotorua is 2.5 hrs; Rotorua to Taupo is 1 hr; Wellington to Rotorua is 5 hrs. You can see the highlights of the North Island in 5–7 days without exhausting the kids. The North Island is the better choice for families with under-5s, those on tight budgets, and first-time visitors wanting culture and history alongside nature.</p>",
        "list": [
          "Warmer beaches — swimming season is longer and water is warmer (19–23°C)",
          "Shorter drives — Auckland to Rotorua is 2.5 hrs; the whole North Island in 7 days is very doable",
          "World-class culture — Māori culture at Rotorua, Te Papa in Wellington",
          "More for young kids — Waitomo (prams OK), Hobbiton (under-9 free), Taupo lake swimming",
          "Better value — accommodation and activities are generally 15–25% cheaper than Queenstown"
        ]
      },
      {
        "heading": "The South Island — Scenery, Adventure, and Wildlife",
        "body": "<p>The South Island has the most spectacular scenery in NZ — arguably in the Southern Hemisphere. Milford Sound, Aoraki/Mt Cook, Queenstown, the Franz Josef Glacier, and the Otago Peninsula wildlife are all world-class. The South Island is bigger, the drives are longer, and the weather is more changeable — but the reward is proportional.</p><p>Queenstown is expensive. The South Island generally costs 20–30% more for accommodation and activities than equivalent North Island destinations. But the experiences are unforgettable: a Milford Sound cruise, the Hooker Valley walk to a glacier lake, watching 100 blue penguins waddle home at Oamaru, or skiing The Remarkables while looking over Lake Wakatipu.</p>",
        "list": [
          "Dramatic scenery — Milford Sound, Aoraki/Mt Cook, Wanaka, Fiordland",
          "Better wildlife — blue penguins, yellow-eyed penguins, fur seals, albatross, dolphins",
          "Best skiing — Cardrona, The Remarkables, Coronet Peak, Treble Cone",
          "West Coast wilderness — Franz Josef, Pancake Rocks, Hokitika Gorge",
          "Wine country — Marlborough, Central Otago (Cromwell, Wanaka)"
        ]
      },
      {
        "heading": "The Honest Verdict — Which Island First?",
        "body": "<p><strong>First time to NZ with young kids (under 7)?</strong> North Island. Shorter drives, warmer beaches, excellent cultural experiences, and Hobbiton. Base in Auckland, do the Golden Triangle (Waitomo → Rotorua), add Taupo and Wellington.</p><p><strong>First time with older kids (7–14)?</strong> South Island. The scenery is more dramatic, the adventure activities more thrilling, and the wildlife encounters are extraordinary. Christchurch → Queenstown road trip or the 14-day South Island campervan loop.</p><p><strong>Two weeks or more?</strong> Do both. The classic sequence: fly into Auckland (North Island, 7 days), fly or ferry to the South Island (South Island, 7 days), fly out of Queenstown or Christchurch.</p>",
        "table": {
          "headers": ["", "North Island", "South Island"],
          "rows": [
            ["Best for ages", "All ages (great for under-5s)", "5+ (adventure, wildlife, skiing)"],
            ["Driving distances", "Shorter (2–3 hrs between stops)", "Longer (3–5 hrs between stops)"],
            ["Weather", "Warmer, more reliable", "More dramatic, more variable"],
            ["Cost", "More affordable", "20–30% more expensive"],
            ["Swimming beaches", "Warmer, more patrolled", "Colder, wilder, fewer patrols"],
            ["Cultural experiences", "Outstanding (Rotorua, Wellington)", "Good (Christchurch, Dunedin)"],
            ["Wildlife", "Dolphins, birds", "Penguins, seals, albatross, dolphins"],
            ["Skiing", "Ruapehu (good)", "Queenstown/Wanaka (world-class)"]
          ]
        },
        "cta": {
          "text": "Plan your North + South Island trip — compare campervans →",
          "url": "https://www.discovercars.com/",
          "affiliate": True
        }
      }
    ]
  },

  {
    "slug": "nz-family-first-trip-complete-guide",
    "short_title": "First Trip to NZ — Family Guide",
    "title": "First Family Trip to New Zealand — The Complete 2026 Planning Guide",
    "meta_desc": "Planning your first family holiday in New Zealand? This complete guide covers costs, driving, best months, must-see stops, and how to book everything.",
    "intro": "New Zealand is one of the world's best family holiday destinations — safe, English-speaking, with extraordinary nature and world-class infrastructure. But it can be overwhelming to plan from scratch. This guide covers everything a first-time NZ family visitor needs to know, from when to go to what it actually costs.",
    "updated": "May 2026",
    "reading_time": 11,
    "hero_image": {
      "url": "https://images.unsplash.com/photo-1519763816161-cf56e09d44a5?w=1200&q=80",
      "thumb": "https://images.unsplash.com/photo-1519763816161-cf56e09d44a5?w=600&q=70",
      "alt": "Family road trip New Zealand planning",
      "credit": "Unsplash / Jesper Aggergaard"
    },
    "sections": [
      {
        "heading": "When to Visit NZ with Kids",
        "body": "<p>New Zealand's summer (December–February) is the peak season — school holidays, warmest beaches, and long days. It's also the most expensive and crowded period. If flexibility allows, October–November and March–April are the best value: warm enough for swimming, fewer crowds, and 15–25% cheaper accommodation.</p><p>School holiday periods (January, mid-April, mid-July, late September) are busiest. July is the ski season peak for Queenstown and Wanaka. Avoid the Christmas–New Year fortnight if possible — prices are at maximum and popular spots are packed.</p>",
        "table": {
          "headers": ["Month", "Weather", "Crowds", "Cost", "Best for"],
          "rows": [
            ["January", "Hot, 22–28°C", "Very high", "$$$$$", "Beaches, summer activities"],
            ["February", "Hot, 21–27°C", "High", "$$$$", "Beaches, all activities"],
            ["March", "Warm, 18–24°C", "Medium", "$$$", "Best shoulder — warm + quiet"],
            ["April", "Mild, 15–21°C", "Low", "$$", "Autumn colour, school holidays mid-April"],
            ["May", "Cool, 12–18°C", "Low", "$$", "Cheap, quiet, attractions open"],
            ["June", "Cold, 8–15°C", "Very low", "$", "Ski season starts, cheapest month"],
            ["July", "Cold, 7–14°C", "Medium (ski)", "$$$", "Skiing — book Queenstown far ahead"],
            ["August", "Cold, 8–15°C", "Low", "$$", "Ski season, quiet outside ski areas"],
            ["September", "Mild, 11–18°C", "Low", "$$", "Spring — tracks open, cheap"],
            ["October", "Warm, 14–20°C", "Low–Medium", "$$$", "Excellent — warm + not crowded"],
            ["November", "Warm, 16–22°C", "Low–Medium", "$$$", "Pre-summer — great value"],
            ["December", "Hot, 20–26°C", "Very high", "$$$$$", "Summer begins — book far ahead"]
          ]
        }
      },
      {
        "heading": "How Much Does a NZ Family Holiday Cost?",
        "body": "<p>New Zealand is not cheap — but it's not as expensive as the horror stories suggest if you're smart. A family of 4 can do NZ well for $250–350/day (accommodation + food + activities + fuel) if you use holiday parks and self-cater some meals. Queenstown and peak summer push costs to $400–600/day. The biggest savings come from choosing a campervan over hotels (saves $80–150/night on accommodation) and cooking your own meals.</p>",
        "table": {
          "headers": ["Category", "Budget", "Mid-range", "Splurge"],
          "rows": [
            ["Accommodation (per night)", "$45–90 (holiday park)", "$150–280 (motel/hotel)", "$300–600+ (boutique)"],
            ["Activities (per day)", "$50–100 (mostly free stuff)", "$150–300 (paid attractions)", "$300–500 (bungy, heli-hike)"],
            ["Food (per day, family 4)", "$60–90 (supermarket + cook)", "$90–150 (mix)", "$150–250+ (restaurant every meal)"],
            ["Fuel (per week, 700km)", "$120–160", "$120–160", "$120–160"],
            ["Total per day (family 4)", "$250–400", "$400–700", "$700–1,200+"]
          ]
        }
      },
      {
        "heading": "Driving in New Zealand — What Families Need to Know",
        "body": "<p>New Zealand drives on the left. Roads are generally excellent but can be narrow and winding outside major highways. The speed limit is 100km/h on open roads — but expect 60–80km/h average speeds on winding South Island roads. Give yourself more time than Google Maps suggests for rural routes.</p><p>Key rules: seatbelts mandatory for all passengers; car seats required for under-7s (bring your own or hire from rental company); zero blood alcohol for drivers under 20, 0.05 BAC for adults. Fuel is available in all towns but stock up before remote stretches (West Coast, Milford Road).</p>",
        "list": [
          "Drive on the left — give way to traffic already on roundabouts",
          "Speed limit: 100km/h open road, 50km/h towns, 30km/h school zones",
          "Car seats required under-7s — hire from rental company ($5–10/day) or bring your own",
          "Allow 20–30% more time than Google Maps for South Island mountain roads",
          "Fuel up before the West Coast, Milford Road, and East Cape — long stretches between stations",
          "No passing unless the road is clearly clear — NZ has many blind corners"
        ],
        "cta": {
          "text": "Compare rental cars and campervans for NZ →",
          "url": "https://www.discovercars.com/",
          "affiliate": True
        }
      },
      {
        "heading": "The 5 Non-Negotiables for First-Time NZ Families",
        "body": "<p>If this is your first NZ trip, these five experiences should be on every itinerary regardless of ages:</p>",
        "list": [
          "Waitomo Glowworm Caves — the underground glowworm display is one of the world's great natural wonders. 45 min guided tour, all ages. Book ahead.",
          "Rotorua geothermal parks — Te Puia or Wai-O-Tapu. Boiling mud, geysers, and vivid colour. Nowhere else on earth looks like this.",
          "Aoraki/Mt Cook Hooker Valley Track — 3 hrs return, any fitness level, ends at a glacier lake with NZ's highest mountain as the backdrop. Unforgettable.",
          "Milford Sound or Doubtful Sound cruise — fiords formed by glaciers, waterfalls, and dolphins. One of the world's great landscapes. Book months ahead.",
          "A New Zealand beach — whichever one you get to. Mount Maunganui, Kaiteriteri, Pohara — the beaches here are genuinely world-class."
        ]
      }
    ]
  }

]


def main():
    # ── Add itineraries ─────────────────────────────────────────────────────
    itin_path = ROOT / "data/itineraries.json"
    itineraries = json.loads(itin_path.read_text())
    existing_slugs = {i["slug"] for i in itineraries}

    added_itins = 0
    for itin in NEW_ITINERARIES:
        if itin["slug"] in existing_slugs:
            print(f"  skip (exists): {itin['slug']}")
            continue
        itineraries.append(itin)
        added_itins += 1
        print(f"  + itinerary: {itin['slug']}")

    itin_path.write_text(json.dumps(itineraries, indent=2, ensure_ascii=False))

    # ── Add travel guides ───────────────────────────────────────────────────
    added_guides = 0
    for guide in NEW_GUIDES:
        out = ROOT / "content/travel-tips" / f"{guide['slug']}.json"
        if out.exists():
            print(f"  skip (exists): {guide['slug']}")
            continue
        out.write_text(json.dumps(guide, indent=2, ensure_ascii=False))
        added_guides += 1
        print(f"  + guide: {guide['slug']}")

    print(f"\nDone — {added_itins} itineraries, {added_guides} guides added.")


if __name__ == "__main__":
    main()
