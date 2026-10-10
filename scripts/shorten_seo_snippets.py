#!/usr/bin/env python3
"""Add a short `seo_title` (the title shown in search results) to article JSON; optionally trim `meta_desc`.

Search results cut titles at about 60 characters and descriptions at about 160. The visible H1 (`title`) is left
alone: only `seo_title`, which layouts/guide.html uses for <title>, is new. Re-runnable: it only touches articles whose
title is over 60 characters. Descriptions are only trimmed with --metas: search engines shorten long ones
themselves, and an automatic cut can end mid-phrase, so review that output before applying it.

  python3 scripts/shorten_seo_snippets.py            # print the plan
  python3 scripts/shorten_seo_snippets.py --apply
  python3 scripts/shorten_seo_snippets.py --metas    # also plan description trims
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TITLE_MAX, META_MAX, MIN_HEAD = 60, 160, 28
BREAKS = (" — ", " – ", ": ", ", ", " & ", " | ", " (")


def short_title(title):
    if len(title) <= TITLE_MAX:
        return None
    window = title[: TITLE_MAX + 1]
    cuts = [window.rfind(b) for b in BREAKS]
    cuts = [c for c in cuts if c >= MIN_HEAD]
    if cuts:
        head = title[: max(cuts)]
    else:
        head = window[: window.rfind(" ")]
    head = re.sub(r"[\s,;:&\-–—(]+$", "", head)
    head = re.sub(r"\s+(and|or|the|a|of|to|for|with|in|vs)$", "", head, flags=re.I)
    year = re.search(r"\b20\d\d\b", title)
    if year and year.group(0) not in head and len(head) + 5 <= TITLE_MAX:
        head = f"{head} {year.group(0)}"  # keep the year: people search for it
    return head if MIN_HEAD <= len(head) <= TITLE_MAX else None


def short_meta(meta):
    """Cut at a sentence end, else at a comma, else at a word, so the snippet never stops mid-phrase."""
    if len(meta) <= META_MAX:
        return None
    window = meta[:META_MAX]
    sentence = max(window.rfind(". "), window.rfind("! "), window.rfind("? "))
    if sentence >= 90:
        return window[: sentence + 1]
    comma = max(window.rfind(", "), window.rfind(" – "), window.rfind(" — "))
    if comma >= 110:
        return window[:comma].rstrip(" ,;:-–—&") + "."
    cut = meta[: META_MAX - 1]
    cut = cut[: cut.rfind(" ")].rstrip(" ,;:-–—&")
    cut = re.sub(r"\s+(and|or|the|a|an|of|to|for|with|in|on|at|vs|your|our)$", "", cut, flags=re.I)
    return cut + "…"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--metas", action="store_true", help="also trim descriptions over 160 characters")
    args = ap.parse_args()
    changed = 0
    for folder in ("posts", "travel-tips"):
        for f in sorted((ROOT / "content" / folder).glob("*.json")):
            raw = f.read_text(encoding="utf-8")
            d = json.loads(raw)
            new_title = short_title(d.get("title", "")) if not d.get("seo_title") else None
            new_meta = short_meta(d.get("meta_desc", "")) if args.metas else None
            if not (new_title or new_meta):
                continue
            changed += 1
            if new_title:
                print(f"TITLE {len(d['title']):>3}→{len(new_title):>2}  {d['title']}\n               {new_title}")
                d["seo_title"] = new_title
            if new_meta:
                print(f"META  {len(d['meta_desc']):>3}→{len(new_meta):>3}  …{d['meta_desc'][-45:]}\n               …{new_meta[-45:]}")
                d["meta_desc"] = new_meta
            if args.apply:
                f.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n{changed} articles {'updated' if args.apply else 'would change'}")


if __name__ == "__main__":
    main()
