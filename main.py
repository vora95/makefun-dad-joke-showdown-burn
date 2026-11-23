#!/usr/bin/env python3
"""Dad Joke Showdown (burn): write the one dad joke to /output/entry.txt."""
import os

ENTRY = "I told my laptop I needed a break and now it keeps sending me Kit Kats."

OUT = "/output/entry.txt"


def main():
    # Gate: the bounty requires UTF-8 text of 1-200 characters, not only
    # whitespace, a single line, no trailing newline.
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    # A dad joke is one sentence: exactly one terminal full stop, at the end.
    assert text.count(".") == 1 and text.endswith("."), "entry must be a single sentence"
    text.encode("ascii")  # ASCII-only by design; non-ASCII would still pass UTF-8
    os.makedirs("/output", exist_ok=True)
    data = text.encode("utf-8")
    with open(OUT, "wb") as f:
        f.write(data)
    with open(OUT, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    print(f"wrote {len(data)} bytes to {OUT}")


if __name__ == "__main__":
    main()
