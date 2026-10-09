"""Builds the NZ school holidays calendar file (.ics) from data/school_holidays.json.

One source of truth: the same data drives the /school-holidays page, so the download can never disagree with it.
All events are all-day. Only the last year's summer break is a single "begins" day, because the following year's
Term 1 start has not been published.
"""

import hashlib
from datetime import date, timedelta

CAL_NAME = "NZ School Holidays"
DOMAIN = "nzfamilytravel.co.nz"
REVISION_STAMP = "20261010T000000Z"  # bump when the data is corrected so calendars pick up the change


def _ics_date(d):
    return d.strftime("%Y%m%d")


def _escape(text):
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def _fold(line):
    """RFC 5545: lines are at most 75 octets; continuation lines start with a space."""
    raw = line.encode("utf-8")
    if len(raw) <= 75:
        return line
    out, chunk = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(chunk) + len(b) > (75 if not out else 74):
            out.append(chunk.decode("utf-8"))
            chunk = b""
        chunk += b
    out.append(chunk.decode("utf-8"))
    return "\r\n ".join(out)


def _event(uid_key, start, end_inclusive, summary, description, url):
    uid = hashlib.sha1(uid_key.encode()).hexdigest()[:16] + "@" + DOMAIN
    return [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{REVISION_STAMP}",
        f"DTSTART;VALUE=DATE:{_ics_date(start)}",
        f"DTEND;VALUE=DATE:{_ics_date(end_inclusive + timedelta(days=1))}",  # all-day DTEND is exclusive
        f"SUMMARY:{_escape(summary)}",
        f"DESCRIPTION:{_escape(description)}",
        f"URL:{url}",
        "TRANSP:TRANSPARENT",
        "END:VEVENT",
    ]


def build_ics(school_holidays, base_url, today=None, first_year=None):
    """Return the calendar text. Events that finished before `today` are left out."""
    today = today or date.today()
    years = sorted(school_holidays["years"], key=lambda y: y["year"])
    last_year = years[-1]["year"]
    page = f"{base_url}/school-holidays/"
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        f"PRODID:-//{DOMAIN}//NZ School Holidays//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{CAL_NAME}",
        "X-WR-TIMEZONE:Pacific/Auckland",
    ]
    for y in years:
        if first_year and y["year"] < first_year:
            continue
        for h in y["holidays"]:
            start, end = date.fromisoformat(h["start"]), date.fromisoformat(h["end"])
            summary = f"NZ school holidays: {h['name'].replace(' Holidays', '')}"
            note = "Official Ministry of Education dates, the same for all state schools."
            if h["name"] == "Summer Holidays" and y["year"] == last_year:
                end = start  # next year's Term 1 start is not published yet
                summary = "NZ school holidays: Summer begins"
                note += " Term 1 of the following year starts in late January or early February."
            if end < today:
                continue
            tip = h.get("tip", "")
            lines += _event(f"holiday-{y['year']}-{h['name']}", start, end, summary, f"{note} {tip}".strip() + f" Dates and ideas: {page}", page)
        for t in y["terms"]:
            if t["term"] == 1:
                continue  # Term 1 starts anywhere in a window, depending on the school
            start = date.fromisoformat(t["start"])
            if start < today:
                continue
            lines += _event(f"term-{y['year']}-{t['term']}", start, start, f"NZ school: Term {t['term']} starts", f"Official Ministry of Education term dates. Dates and ideas: {page}", page)
    lines.append("END:VCALENDAR")
    return "\r\n".join(_fold(l) for l in lines) + "\r\n"
