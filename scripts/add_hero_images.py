#!/usr/bin/env python3
"""Add hero_image fields to all travel-tips, posts, tools, and overseas content files."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Unsplash images mapped by slug (or partial slug match)
# Format: photo ID, alt text, credit
IMAGE_MAP = {
    # Monthly NZ guides
    "nz-in-january":   ("1507699622108-4be3abd695ad", "Families on a New Zealand beach in summer", "Unsplash / Devin Avery"),
    "nz-in-february":  ("1469854523086-cc02fe5d8800", "NZ outdoor family adventure in late summer", "Unsplash / Tobias Cornille"),
    "nz-in-march":     ("1508739773434-c26b3d09e071", "Autumn colours in New Zealand",              "Unsplash / Niko Photos"),
    "nz-in-april":     ("1464822759023-fed622ff2c3b", "NZ mountains and valleys in autumn",         "Unsplash / Tim Swaan"),
    "nz-in-may":       ("1433086966628-8de40b29beea", "Winter mist over NZ countryside in May",     "Unsplash / Patrick Selin"),
    "nz-in-june":      ("1551524559-8af4e6624178",    "Ski resort family holiday in NZ winter",     "Unsplash / Alain Bonnardeaux"),
    "nz-in-july":      ("1519863117922-f73b28e6a0a0", "Snow-covered NZ mountains in July",          "Unsplash / Jonathan Müller"),
    "nz-in-august":    ("1562690965-6adcc979cf97",    "Early spring thaw in New Zealand August",    "Unsplash / Adam Kool"),
    "nz-in-september": ("1462275646964-a0e3386b89fa", "NZ wildflowers in bloom September",          "Unsplash / Annie Spratt"),
    "nz-in-october":   ("1505228709967-7e61e12efdd2", "NZ spring hills green October",              "Unsplash / Photo by Dan Meyers"),
    "nz-in-november":  ("1553984840-b8cbc34f5214",    "NZ outdoor family activities in spring",     "Unsplash / Ashim D'Silva"),
    "nz-in-december":  ("1507699622108-4be3abd695ad", "NZ summer beach holiday December",           "Unsplash / Devin Avery"),

    # Travel tips — campervan / road trip
    "nz-campervan-guide-families":      ("1558618666-fcd25c85cd64", "Family campervan road trip in New Zealand",         "Unsplash / Stephan Bechert"),
    "campervan-vs-hotel-nz-families":   ("1519763816161-cf56e09d44a5", "Family road trip decision — car vs campervan",  "Unsplash / Jesper Aggergaard"),
    "jucy-vs-britz-campervan-comparison":("1527631746610-bea7253ae3d1", "Campervans parked at NZ holiday park",         "Unsplash / Goh Rhy Yan"),

    # Travel tips — accommodation / holiday parks
    "nz-holiday-parks-complete-guide":  ("1571896349842-33c89424de2d", "NZ holiday park with kids playing outside",     "Unsplash / Outdoor Park"),
    "best-holiday-parks-nz-families":   ("1504615755583-2916b52192a3", "NZ top holiday park swimming pool",             "Unsplash / Ethan Sexton"),

    # Travel tips — costs / budgets
    "nz-family-travel-costs":           ("1526958097901-5e6d742d3371", "Family counting budget for NZ trip",            "Unsplash / Michael Longmire"),
    "nz-family-travel-insurance-guide": ("1506905925346-21bda4d32df4", "Family safe travel insurance NZ",               "Unsplash / Victor Rodvang"),

    # Travel tips — packing / snacks
    "nz-road-trip-snacks-kids":         ("1553025934-296397db4010", "Kids road trip snacks packed for NZ journey",      "Unsplash / Maarten van den Heuvel"),

    # Travel tips — school holidays / timing
    "nz-school-holidays-travel-tips":   ("1502685104226-ee32379fefbe", "Kids enjoying NZ school holiday adventures",    "Unsplash / Leo Rivas"),

    # Travel tips — age-specific
    "nz-with-babies-travel-guide":      ("1565049793657-11cc47ec7c35", "Parent travelling with baby in NZ",             "Unsplash / Kelly Sikkema"),
    "nz-with-toddlers-travel-guide":    ("1471286174890-9c112740fbef", "Toddler exploring NZ outdoors",                 "Unsplash / Janko Ferlič"),
    "nz-with-teenagers-travel-guide":   ("1529156069898-49953e39b3ac", "Teenagers on NZ outdoor adventure",             "Unsplash / Mateus Campos Felipe"),

    # Travel tips — destination comparisons
    "rotorua-vs-queenstown-families":   ("1519699047748-de8e457a634e", "Comparing Rotorua and Queenstown NZ",           "Unsplash / Sergey Pesterev"),
    "queenstown-vs-wanaka-families":    ("1549887534-1541e9326642",    "Queenstown or Wanaka? NZ lake views",           "Unsplash / David Edelstein"),
    "auckland-day-trips-families":      ("1480714378408-67cf0d13bc1b", "Auckland skyline and Hauraki Gulf day trips",   "Unsplash / Dan Freeman"),

    # Posts — destination specific
    "hawkes-bay":        ("1470770841072-f978cf4d019e", "Hawke's Bay wine and family activities",        "Unsplash / Luca Bravo"),
    "hot-water-beach":   ("1507699622108-4be3abd695ad", "Hot Water Beach Coromandel family digging",     "Unsplash / Devin Avery"),
    "marlborough":       ("1543352634-a1c51d9f1fa7",    "Marlborough Sounds family boat trip",           "Unsplash / Nathan Jennings"),
    "nelson":            ("1464822759023-fed622ff2c3b", "Nelson Abel Tasman NZ coastal family walk",     "Unsplash / Tim Swaan"),
    "northland":         ("1533587851505-d119e13c2eca", "Cape Reinga Northland lighthouse NZ",           "Unsplash / David Straight"),
    "puzzling-world":    ("1549887534-1541e9326642",    "Puzzling World Wanaka family attraction",       "Unsplash / David Edelstein"),
    "taupo":             ("1519699047748-de8e457a634e", "Taupo family activities NZ lake",               "Unsplash / Sergey Pesterev"),
    "tauranga":          ("1507699622108-4be3abd695ad", "Tauranga Mount Maunganui beach family",         "Unsplash / Devin Avery"),

    # Tools
    "nz-family-travel-budget-calculator": ("1526958097901-5e6d742d3371", "NZ family travel budget planning",     "Unsplash / Michael Longmire"),
    "nz-family-packing-list":             ("1553025934-296397db4010",    "NZ family packing list essentials",    "Unsplash / Maarten van den Heuvel"),
    "nz-driving-times":                   ("1519763816161-cf56e09d44a5", "NZ road trip driving times map",       "Unsplash / Jesper Aggergaard"),
    "nz-best-month-to-visit":             ("1505228709967-7e61e12efdd2", "Best time to visit NZ with family",    "Unsplash / Dan Meyers"),
    "nz-trip-cost-by-destination":        ("1526958097901-5e6d742d3371", "NZ trip cost comparison by city",      "Unsplash / Michael Longmire"),
    "nz-school-holidays-2026":            ("1502685104226-ee32379fefbe", "NZ school holidays 2026 planning",     "Unsplash / Leo Rivas"),
    "nz-school-holidays-2027":            ("1502685104226-ee32379fefbe", "NZ school holidays 2027 planning",     "Unsplash / Leo Rivas"),
}

# Default fallback image
DEFAULT_IMAGE = ("1507699622108-4be3abd695ad", "New Zealand family travel", "Unsplash / Devin Avery")

def find_image(slug: str):
    # Direct slug match
    if slug in IMAGE_MAP:
        return IMAGE_MAP[slug]
    # Partial match on post slugs
    for key, val in IMAGE_MAP.items():
        if key in slug:
            return val
    return DEFAULT_IMAGE

def make_hero_image(photo_id, alt, credit):
    return {
        "url": f"https://images.unsplash.com/photo-{photo_id}?w=1200&q=80",
        "thumb": f"https://images.unsplash.com/photo-{photo_id}?w=600&q=70",
        "alt": alt,
        "credit": credit
    }

def process_dir(subdir):
    d = ROOT / "content" / subdir
    if not d.exists():
        return
    for f in sorted(d.glob("*.json")):
        data = json.loads(f.read_text())
        if "hero_image" in data:
            print(f"  skip (already has hero_image): {f.name}")
            continue
        slug = data.get("slug", f.stem)
        photo_id, alt, credit = find_image(slug)
        data["hero_image"] = make_hero_image(photo_id, alt, credit)
        f.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"  added hero_image to: {f.name}")

print("Adding hero_images...")
for subdir in ["travel-tips", "posts", "tools"]:
    print(f"\n[{subdir}]")
    process_dir(subdir)

print("\nDone.")
