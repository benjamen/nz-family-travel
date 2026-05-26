#!/usr/bin/env python3
"""
Patch destinations.json with nearby_cities (links to city pages) and
route_gems (notable stops / detours along the way to this destination).
Run once: .venv/bin/python3 scripts/add_route_gems.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

PATCHES = {
    "auckland-with-kids": {
        "nearby_cities": ["hamilton", "whitianga", "whangarei", "raglan"],
        "route_gems": [
            {
                "name": "Waiheke Island",
                "city_slug": None,
                "how_far": "35 min by ferry from Auckland Ferry Terminal",
                "tagline": "Beaches, olive groves, and child-friendly wineries — the best day trip from Auckland",
                "tip": "Take the Stonyridge or Goldie Estate winery tour. Kids love the tractor ride."
            },
            {
                "name": "Muriwai Gannet Colony",
                "city_slug": None,
                "how_far": "45 min west of Auckland (Muriwai Beach)",
                "tagline": "Hundreds of nesting Australasian gannets on the clifftop — completely free, surreal",
                "tip": "Gannets nest October–March. Muriwai black-sand surf beach is right below."
            },
            {
                "name": "Miranda Hot Springs",
                "city_slug": None,
                "how_far": "1.5 hrs south via Thames — en route to Coromandel or Rotorua",
                "tagline": "Thermal hot pools by the Firth of Thames — great first stop heading south",
                "tip": "Small admission fee. Wading pool for young kids, serious hot pool for adults."
            },
            {
                "name": "Hamilton & Waikato",
                "city_slug": "hamilton",
                "how_far": "1.5 hrs south on SH1",
                "tagline": "Hamilton Gardens (free), Hamilton Zoo, and the gateway to Hobbiton and Waitomo",
                "tip": "Perfect overnight stop before Rotorua or Taupo."
            }
        ]
    },

    "rotorua-family-guide": {
        "nearby_cities": ["hamilton", "matamata", "cambridge", "taupo"],
        "route_gems": [
            {
                "name": "Waitomo Caves",
                "city_slug": "hamilton",
                "how_far": "1.5 hrs west via Hamilton — classic Golden Triangle detour",
                "tagline": "Glowworm caves, black water rafting, and Ruakuri — the greatest underground spectacle in NZ",
                "tip": "The Glowworm Cave is suitable for all ages (15 min walk). Ruakuri is 2 hrs and more dramatic. Book online — schools holidays sell out weeks ahead."
            },
            {
                "name": "Hobbiton Movie Set",
                "city_slug": "matamata",
                "how_far": "30 min west of Rotorua at Matamata",
                "tagline": "The actual Shire from Lord of the Rings — guided tours run all day, magical for all ages",
                "tip": "Book at hobbitontours.com. Under-9s free. Allow 3 hrs including the Green Dragon Inn drink."
            },
            {
                "name": "Blue Spring (Te Waihou Puna)",
                "city_slug": "cambridge",
                "how_far": "45 min west via Cambridge",
                "tagline": "Crystal-clear spring water so blue it looks fake — 45 min return walk, completely free",
                "tip": "Easy flat walk suitable for all ages. Go early morning for the best light and fewer people."
            },
            {
                "name": "Wai-O-Tapu Thermal Wonderland",
                "city_slug": None,
                "how_far": "30 min south of Rotorua on SH5",
                "tagline": "Champagne Pool, Artist's Palette, and the Lady Knox Geyser — the best geothermal park in NZ",
                "tip": "Lady Knox Geyser erupts at 10:15am daily. Arrive by 10am. Allow 2 hrs for the full walk."
            }
        ]
    },

    "taupo-with-kids": {
        "nearby_cities": ["hamilton", "cambridge", "ohakune"],
        "route_gems": [
            {
                "name": "Huka Falls",
                "city_slug": None,
                "how_far": "10 min north of Taupo town",
                "tagline": "The Waikato River squeezes through a narrow gorge and explodes — NZ's most-visited natural attraction, free",
                "tip": "Park at the Huka Falls car park. Short walk (5 min). Jet boat tours run from here too — thrilling for kids 6+."
            },
            {
                "name": "Tongariro Alpine Crossing",
                "city_slug": "ohakune",
                "how_far": "2 hrs south via Ohakune",
                "tagline": "NZ's best day walk — volcanic craters, emerald lakes, and Mount Doom (Mt Ngauruhoe). Teens will love it.",
                "tip": "Too hard for under-10s. Shuttle from Ohakune or Whakapapa. Start early — 7am for the full crossing."
            },
            {
                "name": "Orakei Korako Geothermal Park",
                "city_slug": None,
                "how_far": "45 min north of Taupo via Wairakei",
                "tagline": "The Hidden Valley — active geysers, silica terraces, and a cave with geothermal pool. Less touristy than Rotorua.",
                "tip": "Ferry crossing included in entry. Allow 90 mins. Excellent rainy-day option."
            },
            {
                "name": "Waitomo Caves",
                "city_slug": "hamilton",
                "how_far": "1.5 hrs north-west via Hamilton",
                "tagline": "Glowworm caves on the classic Golden Triangle loop — Auckland → Waitomo → Rotorua → Taupo",
                "tip": "Do this as part of the drive from Auckland rather than a separate day trip from Taupo."
            }
        ]
    },

    "queenstown-with-kids": {
        "nearby_cities": ["arrowtown", "cromwell", "te-anau", "alexandra"],
        "route_gems": [
            {
                "name": "Arrowtown",
                "city_slug": "arrowtown",
                "how_far": "20 min north-east of Queenstown",
                "tagline": "Charming gold-rush town with an amazing autumn, the Chinese Settlement, and Arrow River gold panning",
                "tip": "Best in April–May for autumn colours. Gold panning ($5) is a big hit with kids. Arrowtown Bakery has legendary pies."
            },
            {
                "name": "Cromwell Fruit Stands",
                "city_slug": "cromwell",
                "how_far": "55 min north of Queenstown via SH6",
                "tagline": "Stone fruit capital of NZ — cherries, apricots, and peaches direct from the orchard in summer",
                "tip": "December–February for cherries. The giant fruit sculpture on the roundabout is a mandatory photo stop."
            },
            {
                "name": "Kawarau Bridge Bungy",
                "city_slug": None,
                "how_far": "20 min east of Queenstown at Kawarau Gorge",
                "tagline": "The world's first commercial bungy site — kids can watch from the viewing platform for free",
                "tip": "Free to watch from the viewing platform. Minimum age to jump is 10 (with parent consent). The gorge walk itself is beautiful and free."
            },
            {
                "name": "Te Anau & Milford Sound",
                "city_slug": "te-anau",
                "how_far": "2 hrs south — full-day trip to Milford Sound",
                "tagline": "Te Anau is the gateway to Milford Sound — fiord cruise, Mirror Lakes, and Homer Tunnel along the way",
                "tip": "The Milford Road is one of the world's great drives. Combine with a Milford Sound cruise — book ahead."
            }
        ]
    },

    "wanaka-with-kids": {
        "nearby_cities": ["cromwell", "arrowtown"],
        "route_gems": [
            {
                "name": "Puzzling World",
                "city_slug": None,
                "how_far": "10 min east of Wanaka on SH84",
                "tagline": "Optical illusions, the famous leaning tower, and NZ's best illusion rooms — kids go nuts for it",
                "tip": "Allow 2 hrs. The Hologram Hall and Room of Following Faces are the highlights. Book online for a small discount."
            },
            {
                "name": "Arrowtown",
                "city_slug": "arrowtown",
                "how_far": "40 min south via Crown Range Road",
                "tagline": "Gold-rush history, Arrow River gold panning, and NZ's best autumn colours",
                "tip": "Crown Range Road (SH89) is the scenic route — highest sealed road in NZ, stunning views. Allow extra time."
            },
            {
                "name": "Cromwell Old Town",
                "city_slug": "cromwell",
                "how_far": "30 min south on SH6",
                "tagline": "Historic goldfields township, Central Otago stone fruit, and the Clutha River — great family lunch stop",
                "tip": "The historic precinct is free to walk. Grab stone fruit at the roadside stalls December–March."
            },
            {
                "name": "Cardrona Alpine Resort",
                "city_slug": None,
                "how_far": "30 min south of Wanaka via Cardrona Valley Road",
                "tagline": "Family-friendly ski field with excellent beginners' terrain and a great snow tubing park for young kids",
                "tip": "Better for families with young kids than Treble Cone. Cardrona kids' learning area is excellent."
            }
        ]
    },

    "christchurch-with-kids": {
        "nearby_cities": ["hanmer-springs", "akaroa", "methven", "kaikoura", "timaru"],
        "route_gems": [
            {
                "name": "Akaroa",
                "city_slug": "akaroa",
                "how_far": "1.5 hrs south-east on the Banks Peninsula",
                "tagline": "NZ's only French colonial settlement — swim with Hector's dolphins, eat great food, explore the harbour",
                "tip": "Black Cat Cruises runs dolphin swimming tours (minimum age 8 to swim). Book ahead. The drive over the summit has spectacular views."
            },
            {
                "name": "Hanmer Springs Thermal Pools",
                "city_slug": "hanmer-springs",
                "how_far": "1.5 hrs north on SH7",
                "tagline": "NZ's premier alpine thermal resort — outdoor hot pools, water slides, and a great family base for adventure",
                "tip": "The Hanmer Springs Thermal Pools have a full water slide complex for kids. Busy school holidays — book accommodation early."
            },
            {
                "name": "Kaikōura",
                "city_slug": "kaikoura",
                "how_far": "2.5 hrs north on SH1 (hugging the Kaikōura Coast)",
                "tagline": "Whale watching, swimming with dolphins, seal colony, and the most scenic coastal drive in the South Island",
                "tip": "Whale Watch Kaikōura is the world's best sperm whale experience. Book months ahead in summer. Seal colony at Point Kean is free."
            },
            {
                "name": "Methven & Mount Hutt",
                "city_slug": "methven",
                "how_far": "1.5 hrs south-west on SH77",
                "tagline": "Base camp for Mt Hutt ski field — NZ's best intermediate terrain and a great family winter destination",
                "tip": "Stay in Methven (cheaper than Queenstown). Mt Hutt has excellent learner slopes and kids' snow tubing."
            }
        ]
    },

    "wellington-with-kids": {
        "nearby_cities": ["paraparaumu", "lower-hutt", "greytown", "martinborough", "masterton"],
        "route_gems": [
            {
                "name": "Pukaha Mount Bruce Wildlife Centre",
                "city_slug": None,
                "how_far": "2 hrs north on SH2 near Masterton",
                "tagline": "Free-roaming kiwi in a forest sanctuary — the easiest place in NZ to see a kiwi in the wild",
                "tip": "Kiwi feeding at 1:30pm daily. Also has white kiwi, kākāpō, and tuatara. Allow 3 hrs."
            },
            {
                "name": "Martinborough Wine Village",
                "city_slug": "martinborough",
                "how_far": "1 hr east via the Remutaka Hill Road",
                "tagline": "NZ's pinot noir capital with child-friendly cellar doors, great food, and a classic village green",
                "tip": "Palliser Estate and Craggy Range both welcome families. The village is extremely walkable."
            },
            {
                "name": "Kāpiti Island Bird Sanctuary",
                "city_slug": "paraparaumu",
                "how_far": "1.5 hrs north via Paraparaumu",
                "tagline": "Predator-free island reserve — hear birdsong like pre-European NZ. Kiwi active at dusk.",
                "tip": "Permit required — book months ahead at DOC. Day trips run from Paraparaumu Beach. Worth every bit of planning."
            },
            {
                "name": "Greytown",
                "city_slug": "greytown",
                "how_far": "1 hr north-east over Remutaka Hill",
                "tagline": "NZ's most beautiful small town — Victorian streetscape, artisan shops, excellent food, and the Cobblestones Museum",
                "tip": "Combine with Martinborough for a great day trip. Greytown Café strip on Main Street is outstanding for brunch."
            }
        ]
    },

    "nelson-abel-tasman-family": {
        "nearby_cities": ["motueka", "picton"],
        "route_gems": [
            {
                "name": "Motueka Market & Gateway",
                "city_slug": "motueka",
                "how_far": "45 min west of Nelson on SH60",
                "tagline": "The gateway to Abel Tasman — Friday market, great fish and chips, and hop gardens",
                "tip": "Motueka's Sunday Market (8am–1pm) has excellent local produce, arts, and food. Stock up before Abel Tasman water taxi."
            },
            {
                "name": "Pelorus Bridge",
                "city_slug": None,
                "how_far": "1.5 hrs east of Nelson on SH6",
                "tagline": "The actual river used in The Hobbit barrel-riding scene — crystal clear swimming holes, DOC campsite",
                "tip": "Free to visit (small parking fee). Swimming is best January–March. Short walks to the swingbridge and river pools."
            },
            {
                "name": "Farewell Spit",
                "city_slug": None,
                "how_far": "2.5 hrs west of Nelson via Takaka",
                "tagline": "NZ's longest sandspit — gannet colony, migratory waders, and one of the most remote landscapes in the country",
                "tip": "Guided tours only beyond the lighthouse (Farewell Spit Eco Tours). Allow a full day including the Takaka Hill drive."
            },
            {
                "name": "Picton & Marlborough Sounds",
                "city_slug": "picton",
                "how_far": "1.5 hrs east on SH6 to the ferry",
                "tagline": "Gateway to the South Island — Marlborough Sounds kayaking, Queen Charlotte Track, and the Interislander ferry",
                "tip": "If crossing Cook Strait, allow a full day — the Interislander ferry takes 3.5 hrs but the Sounds scenery is spectacular."
            }
        ]
    },

    "bay-of-islands-family": {
        "nearby_cities": ["paihia", "kerikeri", "whangarei"],
        "route_gems": [
            {
                "name": "Paihia & Waitangi Treaty Grounds",
                "city_slug": "paihia",
                "how_far": "In the Bay of Islands — the main township",
                "tagline": "NZ's most important historical site — the place the Treaty of Waitangi was signed in 1840",
                "tip": "The cultural performance and museum are genuinely excellent. Allow 2–3 hrs. Included with entry ticket."
            },
            {
                "name": "Kerikeri",
                "city_slug": "kerikeri",
                "how_far": "20 min north of Paihia",
                "tagline": "NZ's oldest town with excellent food, the Stone Store, and Rainbow Falls — easy half-day",
                "tip": "Rainbow Falls is a 30-min return walk from the car park. The Stone Store (1836) and Mission House are free to view outside."
            },
            {
                "name": "Cape Reinga & Ninety Mile Beach",
                "city_slug": None,
                "how_far": "3.5 hrs north on SH1",
                "tagline": "The spiritual tip of NZ where the Tasman and Pacific meet — and Ninety Mile Beach for sand tobogganing",
                "tip": "Book a day tour from Paihia — they drive the beach (locals-only, guide required) and stop at Te Paki sand dunes for sandboarding."
            },
            {
                "name": "Whangarei & Tutukaka",
                "city_slug": "whangarei",
                "how_far": "2 hrs south on SH1",
                "tagline": "Whangarei Falls (free, beautiful), Te Matau ā Pohe bridge walk, and the Poor Knights Islands dive",
                "tip": "Whangarei Falls is one of NZ's most accessible and beautiful waterfalls — 10-min walk from the car park."
            }
        ]
    },

    "coromandel-with-kids": {
        "nearby_cities": ["whitianga", "hamilton", "cambridge"],
        "route_gems": [
            {
                "name": "Hot Water Beach",
                "city_slug": "whitianga",
                "how_far": "35 min south of Whitianga on SH25",
                "tagline": "Dig your own thermal spa in the sand at low tide — one of the most unique beaches in the world",
                "tip": "Go 2 hrs either side of low tide. Hire spades from the café ($5). The hot water section is small — arrive early to get a spot."
            },
            {
                "name": "Cathedral Cove",
                "city_slug": "whitianga",
                "how_far": "20 min north of Hahei, near Whitianga",
                "tagline": "NZ's most photographed natural arch — a stunning sea cavern connecting two beaches",
                "tip": "The 45-min walk is suitable for all ages. Boat or kayak access available from Hahei — the sea cave approach is spectacular."
            },
            {
                "name": "Miranda Hot Springs",
                "city_slug": None,
                "how_far": "1 hr south of Thames via SH25 — en route from Auckland",
                "tagline": "Thermal pools by the Firth of Thames with one of NZ's largest outdoor hot pools — great stopover",
                "tip": "Located on the main Auckland–Coromandel highway. Perfect for tired legs at the start or end of a Coromandel trip."
            },
            {
                "name": "Hamilton Gardens",
                "city_slug": "hamilton",
                "how_far": "1.5 hrs south-west via Morrinsville",
                "tagline": "World-class themed gardens (54 gardens, 58 hectares) — completely free and stunning for all ages",
                "tip": "Combine with Hobbiton at Matamata (45 min from Hamilton) for a great Waikato loop."
            }
        ]
    },

    "fiordland-milford-sound-family": {
        "nearby_cities": ["te-anau", "cromwell"],
        "route_gems": [
            {
                "name": "Te Anau — Gateway Town",
                "city_slug": "te-anau",
                "how_far": "2 hrs from Queenstown — the base for Milford Sound",
                "tagline": "The best family base for Fiordland — Te Anau glowworm caves, lake cruises, and the start of the Milford Road",
                "tip": "Stay in Te Anau rather than driving Milford return from Queenstown — 2 hrs each way is a long day for kids."
            },
            {
                "name": "Mirror Lakes",
                "city_slug": None,
                "how_far": "1 hr from Te Anau on the Milford Road",
                "tagline": "Perfect mountain reflections on glassy lakes — a 10-minute boardwalk, free, completely stunning",
                "tip": "Stop early morning for the best reflections (no wind). The Milford Road has dozens of free stops — don't rush it."
            },
            {
                "name": "Lake Manapouri",
                "city_slug": None,
                "how_far": "20 min south of Te Anau on SH95",
                "tagline": "One of NZ's deepest and most beautiful lakes — the starting point for Doubtful Sound day trips",
                "tip": "Doubtful Sound (3× less visited than Milford, equally spectacular) departs from Pearl Harbour, Manapouri. Book a day tour."
            },
            {
                "name": "Homer Tunnel",
                "city_slug": None,
                "how_far": "En route on the Milford Road, 1.5 hrs from Te Anau",
                "tagline": "One of the world's most dramatic road tunnels — carved through sheer mountain, kea parrots hang around outside",
                "tip": "Kea (NZ mountain parrots) are often seen at the Homer Tunnel portal. Don't let them near your car — they chew rubber seals!"
            }
        ]
    },

    "northland-cape-reinga-family": {
        "nearby_cities": ["whangarei", "kerikeri", "paihia"],
        "route_gems": [
            {
                "name": "Whangarei Falls & Town Basin",
                "city_slug": "whangarei",
                "how_far": "2 hrs north of Auckland — the main city of Northland",
                "tagline": "Whangarei Falls (free, 26m, beautiful) plus a great waterfront precinct with playgrounds and cafés",
                "tip": "Good overnight stop. The Town Basin marina has free electric BBQs and a fab playground. Claphams National Clock Museum is nearby."
            },
            {
                "name": "Hokianga Harbour & Sand Dunes",
                "city_slug": None,
                "how_far": "2.5 hrs from Auckland via Whangarei — west coast Northland",
                "tagline": "Ancient kauri forests, the giant Tāne Mahuta kauri tree, and towering sand dunes across the harbour",
                "tip": "Tāne Mahuta (2,000-year-old kauri) is a 5-min walk from the car park in Waipoua Forest. The Hokianga harbour ferry and sand dunes are on the opposite bank."
            },
            {
                "name": "Te Paki Sand Dunes & Ninety Mile Beach",
                "city_slug": None,
                "how_far": "30 min south of Cape Reinga",
                "tagline": "Massive sand dunes you can toboggan — the biggest sand hill fun in NZ",
                "tip": "Boogie boards (free from tour operators) for sand tobogganing. The beach drive is guided tours only — don't attempt in a rental car."
            },
            {
                "name": "Bay of Islands",
                "city_slug": "paihia",
                "how_far": "From Kerikeri — the Bay of Islands is here (Paihia, Russell, Waitangi)",
                "tagline": "144 islands, dolphins, Waitangi Treaty Grounds, and the best sailing in NZ",
                "tip": "Hole in the Rock dolphin cruise from Paihia is the must-do. Book online. Dolphins are almost always guaranteed."
            }
        ]
    },

    "tauranga-mount-maunganui-family": {
        "nearby_cities": ["hamilton", "whitianga", "cambridge", "whanganui"],
        "route_gems": [
            {
                "name": "Hobbiton Movie Set",
                "city_slug": "matamata",
                "how_far": "1 hr south-west via Matamata",
                "tagline": "The most magical film set in NZ — you have to see the Shire at least once",
                "tip": "45 min each way from Tauranga. Book the 10am tour to beat the crowds. Under-9s free."
            },
            {
                "name": "McLaren Falls Park",
                "city_slug": None,
                "how_far": "30 min south of Tauranga via SH29",
                "tagline": "Stunning waterfalls in a DOC park with swimming holes, BBQ areas, and glowworm dell at night",
                "tip": "Free to visit. The glowworm dell is 500m from the car park — go after dark with a torch. Swimming is beautiful December–March."
            },
            {
                "name": "Waihi Beach & Gold Mine",
                "city_slug": None,
                "how_far": "45 min north of Mount Maunganui",
                "tagline": "Long surf beach plus the Waihi Gold Mine Experience — gold mining history meets gorgeous swimming",
                "tip": "Waihi Beach is less crowded than Mount Maunganui. The Gold Mine Experience ($30/adult) is genuinely impressive — NZ's largest open-cast mine."
            },
            {
                "name": "Coromandel Peninsula",
                "city_slug": "whitianga",
                "how_far": "1.5 hrs north to Whitianga — Hot Water Beach and Cathedral Cove",
                "tagline": "Hot Water Beach thermal spa, Cathedral Cove sea arch, and the gorgeous Coromandel coastline",
                "tip": "A natural loop: Tauranga → Waihi → Whitianga → Hot Water Beach → Thames → Auckland (or back south)."
            }
        ]
    },

    "hawkes-bay-family-guide": {
        "nearby_cities": ["masterton"],
        "route_gems": [
            {
                "name": "Cape Kidnappers Gannet Colony",
                "city_slug": None,
                "how_far": "30 min south-east of Napier via Clifton",
                "tagline": "The world's most accessible mainland gannet colony — 6,000+ birds nesting on dramatic coastal headland",
                "tip": "Guided tractors from Clifton (Oct–April). Book Cape Kidnappers Farm tours online. The cliff-top walk is free but seasonal."
            },
            {
                "name": "Te Mata Peak",
                "city_slug": None,
                "how_far": "20 min south of Napier near Havelock North",
                "tagline": "399m volcanic peak with sweeping views from Hawke's Bay to Mt Ruapehu — free, easy drive to the top",
                "tip": "Drive to the summit car park (free). Short walks from there. Excellent sunset spot. The Giant Sleeping legend makes a great story for kids."
            },
            {
                "name": "Napier Art Deco District",
                "city_slug": None,
                "how_far": "City centre — 5 min from the waterfront",
                "tagline": "The world's most intact Art Deco city — rebuilt after the 1931 earthquake, free to walk around",
                "tip": "Art Deco self-guided walk (free map from i-SITE). The Hawke's Bay Museum tells the earthquake story vividly. Marine Parade playground is excellent."
            },
            {
                "name": "Wairarapa & Martinborough",
                "city_slug": "masterton",
                "how_far": "2 hrs south over the Gentle Annie range",
                "tagline": "Wine country, olive groves, and the charming village of Martinborough — great for combining with a Wellington trip",
                "tip": "The Hawke's Bay → Martinborough → Wellington route makes a superb South-North Island road trip section."
            }
        ]
    },

    "dunedin-family-guide": {
        "nearby_cities": ["oamaru", "cromwell", "alexandra"],
        "route_gems": [
            {
                "name": "Oamaru Blue Penguin Colony",
                "city_slug": "oamaru",
                "how_far": "1.5 hrs north on SH1",
                "tagline": "Watch the world's smallest penguins waddle home at dusk — the most charming wildlife experience in NZ",
                "tip": "Evening viewing (after 8pm in summer) is spectacular — 100+ penguins coming in off the beach. Afternoon session is also good for kids. Book ahead."
            },
            {
                "name": "Moeraki Boulders",
                "city_slug": None,
                "how_far": "1 hr north of Dunedin on SH1",
                "tagline": "Giant perfectly spherical boulders on the beach — free, bizarre, and completely photogenic",
                "tip": "Best at low tide so you can walk between them. 15-min walk from the car park. Moeraki village café is good for lunch."
            },
            {
                "name": "Larnach Castle",
                "city_slug": None,
                "how_far": "30 min east of Dunedin on Otago Peninsula",
                "tagline": "NZ's only castle — Victorian Gothic mansion with spectacular harbour views and a great ballroom",
                "tip": "Gardens are excellent for a picnic. The castle tour (45 min) is family-friendly. Otago Peninsula wildlife tour nearby — albatross, sea lions, penguins."
            },
            {
                "name": "The Catlins",
                "city_slug": None,
                "how_far": "2 hrs south of Dunedin via Balclutha",
                "tagline": "The wild southern coast — Purakaunui Falls, Nugget Point Lighthouse, yellow-eyed penguins, and sea lions on the beach",
                "tip": "Allow 2 days in the Catlins. Stay at Papatowai. Wildlife is best at dawn and dusk. Porpoise Bay for Hector's dolphins."
            }
        ]
    },

    "new-plymouth-taranaki-family": {
        "nearby_cities": ["whanganui", "ohakune"],
        "route_gems": [
            {
                "name": "Mount Taranaki Lookout",
                "city_slug": None,
                "how_far": "30 min east of New Plymouth in Egmont National Park",
                "tagline": "One of the world's most perfectly symmetrical volcanic cones — the summit track and short walks are spectacular",
                "tip": "Drive to North Egmont visitor centre (free). The Pouakai Circuit (2 days) has incredible views. Short walks to Wilkies Pools and Bell Falls are family-friendly."
            },
            {
                "name": "Pukekura Park & Brooklands Zoo",
                "city_slug": None,
                "how_far": "In New Plymouth city centre",
                "tagline": "Free public park with beautiful gardens, rowing lake, waterfall, and a small zoo — all completely free",
                "tip": "Brooklands Zoo has free entry. The park is the best in NZ for a city park walk. The TSB Festival of Lights (December–February) is world-class."
            },
            {
                "name": "Tongaporutu (Three Sisters)",
                "city_slug": None,
                "how_far": "1 hr north of New Plymouth on SH3",
                "tagline": "Dramatic coastal rock formations (Elephant Rock, Three Sisters) — tide-dependent walk to sea caves and arches",
                "tip": "Check tide times — only accessible 2 hrs either side of low tide. Scrambling on rocks — wear good shoes. Totally free."
            },
            {
                "name": "Whanganui River & Town",
                "city_slug": "whanganui",
                "how_far": "1.5 hrs south of New Plymouth on SH3",
                "tagline": "NZ's third-longest river with a unique legal personality — explore by jet boat, canoe, or the stunning Whanganui Journey",
                "tip": "The Whanganui National Park canoe journey (3–5 days) is one of NZ's Great Walks. Day jet boat trips from Pipiriki also available."
            }
        ]
    },

    "marlborough-blenheim-family": {
        "nearby_cities": ["picton", "kaikoura"],
        "route_gems": [
            {
                "name": "Picton & Queen Charlotte Sound",
                "city_slug": "picton",
                "how_far": "30 min north of Blenheim on SH1",
                "tagline": "Scenic ferry terminal, Marlborough Sounds kayaking, and the Queen Charlotte Track — NZ's most beautiful sea kayaking",
                "tip": "Queen Charlotte Track water taxis drop you at various points for walking or kayaking. The Sounds by boat is unforgettable."
            },
            {
                "name": "Kaikōura — Whale Watching Capital",
                "city_slug": "kaikoura",
                "how_far": "1.5 hrs south on SH1",
                "tagline": "Sperm whale encounters, dolphin swimming, seal colony walks — the best wildlife destination in NZ",
                "tip": "Whale Watch Kaikōura books out months ahead in summer. Book the moment you know your dates. If whales are a must, this is worth planning your whole trip around."
            },
            {
                "name": "Marlborough Wine Trail",
                "city_slug": None,
                "how_far": "Wairau Valley, 10 min from Blenheim",
                "tagline": "NZ's most famous wine region — Cloudy Bay, Brancott Estate, and 30+ cellar doors in a 30km radius",
                "tip": "Brancott Heritage Vineyard is excellent for families (free playground, good restaurant, vineyard walk). The Marlborough Food & Wine Festival runs every February."
            },
            {
                "name": "Nelson & Abel Tasman",
                "city_slug": "motueka",
                "how_far": "1.5 hrs west on SH6",
                "tagline": "NZ's sunshine capital and the stunning Abel Tasman coast — perfect next stop after Marlborough",
                "tip": "The most natural south-to-north South Island road trip route: Christchurch → Kaikōura → Blenheim → Nelson → Abel Tasman → Westport."
            }
        ]
    },

    "west-coast-family-guide": {
        "nearby_cities": ["hokitika", "greymouth", "westport"],
        "route_gems": [
            {
                "name": "Hokitika Gorge",
                "city_slug": "hokitika",
                "how_far": "30 min east of Hokitika via Hokitika Gorge Road",
                "tagline": "Impossibly turquoise glacial water in a narrow schist gorge — the most beautiful short walk on the West Coast",
                "tip": "30-min return walk on good path. Suspended swingbridge. Free. Go early morning for best colour — the blue-green is extraordinary."
            },
            {
                "name": "Pancake Rocks at Punakaiki",
                "city_slug": "greymouth",
                "how_far": "1 hr north of Greymouth on SH6",
                "tagline": "Layered limestone formations and blowholes on the Tasman Sea — the most dramatic coastal scenery on the West Coast",
                "tip": "15-min loop walk from the car park. Blowholes are active at high tide — check the tide chart. Free parking and entry."
            },
            {
                "name": "Franz Josef Glacier",
                "city_slug": None,
                "how_far": "2 hrs south of Hokitika on SH6",
                "tagline": "A glacier that ends in a rainforest — heli-hike tours or the free valley floor walk to the ice face",
                "tip": "The free valley floor walk (1 hr return) gets you close enough to see the glacier. Heli-hikes are spectacular for older kids/teens. Guided ice walks for 8+."
            },
            {
                "name": "Westport & Charming Creek",
                "city_slug": "westport",
                "how_far": "2.5 hrs north of Greymouth on SH6",
                "tagline": "The coal mining town gateway to the Denniston Plateau and the outstanding Charming Creek Walkway",
                "tip": "Charming Creek Walkway (4 hrs, easy) follows an old coal railway through a spectacular gorge — one of NZ's most underrated family walks."
            }
        ]
    },

    "gisborne-east-cape-family": {
        "nearby_cities": ["masterton"],
        "route_gems": [
            {
                "name": "East Cape Lighthouse",
                "city_slug": None,
                "how_far": "3.5 hrs north of Gisborne around the East Cape",
                "tagline": "The easternmost lighthouse in NZ — 700 steps to the first place on Earth to see the sunrise on New Year's Day",
                "tip": "The East Cape road (SH35) is one of NZ's great coastal drives — 330km, allow 2 days. Empty beaches, marae, and no crowds."
            },
            {
                "name": "Rere Falls & Rockslide",
                "city_slug": None,
                "how_far": "45 min north-west of Gisborne via Ngatapa",
                "tagline": "NZ's longest natural waterslide — 60m of smooth rock to slide down into a pool. Completely free.",
                "tip": "Bring foam mat or boogie board for sliding. 25m falls just upstream are also impressive. Popular with locals on hot days."
            },
            {
                "name": "Tolaga Bay Wharf",
                "city_slug": None,
                "how_far": "1 hr north of Gisborne on SH35",
                "tagline": "NZ's longest wharf (660m) jutting into the Pacific — free to walk, great fishing, and stunning bay views",
                "tip": "Tolaga Bay is a good lunch stop on the East Cape drive. The wharf walk is popular with kids. Bring fishing rods."
            },
            {
                "name": "Mahia Peninsula",
                "city_slug": None,
                "how_far": "1.5 hrs south of Gisborne via Wairoa",
                "tagline": "Isolated surf beaches, dolphins, and the site of Rocket Lab's NZ launch facility — NZ's space coast",
                "tip": "Blue Bay Beach on Mahia is superb and rarely visited. Check Rocket Lab's website for upcoming launches — you can sometimes watch from the peninsula."
            }
        ]
    }
}


def main():
    dest_path = ROOT / "data/destinations.json"
    destinations = json.loads(dest_path.read_text())

    updated = 0
    for dest in destinations:
        slug = dest["slug"]
        if slug in PATCHES:
            patch = PATCHES[slug]
            if "nearby_cities" in patch:
                dest["nearby_cities"] = patch["nearby_cities"]
            if "route_gems" in patch:
                dest["route_gems"] = patch["route_gems"]
            updated += 1
            print(f"  patched: {slug} ({len(patch.get('route_gems',[]))} gems, {len(patch.get('nearby_cities',[]))} cities)")
        else:
            print(f"  no patch: {slug}")

    dest_path.write_text(json.dumps(destinations, indent=2, ensure_ascii=False))
    print(f"\nDone — {updated}/{len(destinations)} destinations patched.")


if __name__ == "__main__":
    main()
