#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, written to /output/entry.txt."""

import os

ENTRY = "I told my laptop I needed a break and now it keeps sending me Kit Kats."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    back = f.read()
assert back == ENTRY, "read-back must be byte-identical to the entry"
assert len(back.encode("utf-8")) == 71, "entry must be exactly 71 bytes"

print(f"wrote {len(ENTRY.encode('utf-8'))} bytes")
