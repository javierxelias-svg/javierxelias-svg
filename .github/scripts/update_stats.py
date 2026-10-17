#!/usr/bin/env python3
"""
Rewrite the CareerOS line in README.md (between the careeros:start and
careeros:end markers) from the public receipt that careeros-public writes
every day.

    python3 .github/scripts/update_stats.py                 # fetch the live receipt
    python3 .github/scripts/update_stats.py --file x.json   # use a saved one

If the receipt can't be fetched or read, README.md is left exactly as it was.
"""

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

URL = ("https://raw.githubusercontent.com/javierxelias-svg/careeros-public/"
       "main/proof/latest.json")
README = Path(__file__).resolve().parents[2] / "README.md"
BLOCK = re.compile(r"(<!-- careeros:start -->\n)(.*?)(\n<!-- careeros:end -->)", re.S)


def render(proof):
    """One line from the receipt. Raises on a receipt that isn't the expected shape."""
    if not isinstance(proof, dict):
        raise ValueError("receipt is not a JSON object")
    when = datetime.strptime(proof["run_at_utc"], "%Y-%m-%dT%H:%M:%SZ")
    date = f"{when:%b} {when.day}, {when.year}"
    url = proof["run_url"]
    tests = proof["tests"]
    if proof["status"] != "ok":
        return (f"Public copy, run by GitHub every day: {date} · **failed** ({proof['reason']}), "
                f"shown here as-is · [run log]({url})")
    n = proof["numbers"]
    return (f"Public copy, run by GitHub every day. Last run {date}: {n['listings_fetched']:,} listings from "
            f"{n['boards_read']} job boards · {tests['checks_passed']} checks passing · "
            f"[run log]({url})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="read the receipt from a local file")
    args = parser.parse_args()

    try:
        if args.file:
            raw = Path(args.file).read_text("utf-8")
        else:
            with urllib.request.urlopen(URL, timeout=30) as response:
                raw = response.read().decode("utf-8")
        line = render(json.loads(raw))
    except Exception as exc:  # any failure: keep the old line, say why
        print(f"receipt unavailable, README left unchanged: {exc}")
        return 0

    text = README.read_text("utf-8")
    if not BLOCK.search(text):
        print("markers not found in README.md")
        return 1
    README.write_text(BLOCK.sub(lambda m: m.group(1) + line + m.group(3), text, count=1), "utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
