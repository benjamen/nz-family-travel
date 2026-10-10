#!/usr/bin/env python3
"""Merge dated duplicate articles into one page per topic.

The article generator used to put the month in the slug (`abel-tasman-water-taxi-family-review-2026-05`), so it
wrote the same article again every month at a new URL. Many near-identical pages on one topic compete with each
other in search and dilute each other's links. This keeps ONE page per topic (the one Search Console says performs
best, else the newest), moves the others to content/_merged/ (out of the build, still in git history), writes
content/redirects.json so their old URLs redirect to the survivor, and rewrites internal links to the survivor.

  python3 scripts/consolidate_dated_duplicates.py --perf perf.json            # dry run: print the plan
  python3 scripts/consolidate_dated_duplicates.py --perf perf.json --apply    # do it

perf.json maps a page path to [clicks, impressions, sessions], e.g. {"/travel-tips/slug": [3, 120, 9]}.
"""

import argparse
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATED = re.compile(r"^(?P<base>.+)-(?P<month>20\d\d-\d\d)$")
DIRS = ("posts", "travel-tips")  # both render under /travel-tips/


def find_groups():
    groups = defaultdict(list)
    for d in DIRS:
        for f in sorted((ROOT / "content" / d).glob("*.json")):
            m = DATED.match(f.stem)
            if m:
                groups[m["base"]].append({"slug": f.stem, "month": m["month"], "dir": d, "file": f})
    return {base: items for base, items in groups.items() if len(items) > 1}


def score(item, perf):
    clicks = impressions = sessions = 0
    for prefix in ("/travel-tips/", "/posts/"):
        c, i, s = perf.get(prefix + item["slug"], [0, 0, 0])
        clicks, impressions, sessions = clicks + c, impressions + i, sessions + s
    return (clicks, impressions, sessions, item["month"])


def plan(perf):
    out = []
    for base, items in sorted(find_groups().items()):
        keep = max(items, key=lambda it: score(it, perf))
        out.append({"base": base, "keep": keep, "merge": [it for it in items if it is not keep]})
    return out


def rewrite_links(merged, keep_slug):
    """Point internal links to the removed pages at the survivor. Returns the number of files changed."""
    pattern = re.compile(r"(?:/travel-tips|/posts)/" + re.escape(merged) + r"(?=[/\"'#?\s)\\])")
    changed = 0
    for path in [*(ROOT / "content").rglob("*.json"), *(ROOT / "data").glob("*.json"), *(ROOT / "layouts").glob("*.html")]:
        if "_merged" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new = pattern.sub(f"/travel-tips/{keep_slug}", text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--perf", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    perf = json.loads(Path(args.perf).read_text())
    steps = plan(perf)
    surplus = sum(len(s["merge"]) for s in steps)
    print(f"{len(steps)} topics with duplicates, {surplus} pages to merge\n")
    for s in steps:
        k = s["keep"]
        print(f"{s['base']}\n   keep  {k['slug']}  {score(k, perf)[:3]}")
        for m in s["merge"]:
            print(f"   merge {m['slug']}  {score(m, perf)[:3]}")
    if not args.apply:
        print("\n(dry run: nothing changed)")
        return

    redirects_path = ROOT / "content" / "redirects.json"
    redirects = json.loads(redirects_path.read_text()) if redirects_path.exists() else {}
    merged_dir = ROOT / "content" / "_merged"
    for s in steps:
        keep_slug = s["keep"]["slug"]
        for m in s["merge"]:
            target = merged_dir / m["dir"]
            target.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "mv", str(m["file"]), str(target / m["file"].name)], cwd=ROOT, check=True)
            redirects[f"travel-tips/{m['slug']}"] = f"travel-tips/{keep_slug}"
            redirects[f"posts/{m['slug']}"] = f"travel-tips/{keep_slug}"
            rewrite_links(m["slug"], keep_slug)
    redirects_path.write_text(json.dumps(redirects, indent=2, sort_keys=True) + "\n")
    print(f"\nMoved {surplus} files to content/_merged/, wrote {len(redirects)} redirects.")


if __name__ == "__main__":
    main()
