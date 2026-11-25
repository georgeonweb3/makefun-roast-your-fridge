#!/usr/bin/env python3
"""Roast Your Fridge — one-line fridge roast entry.

Writes the tournament-winning roast (5-0 in a blind pairwise tournament)
to the entry output path, honouring ENTRY_OUTPUT when set (default
/output/entry.txt). Stdlib only, no network, deterministic.

The entry text:
    "My fridge's filter light has blinked red since March, and I've
    decided it's not a warning — it's the only honest performance
    review in this house."
"""

import os
import sys

ENTRY_TEXT = (
    "My fridge's filter light has blinked red since March, and I've "
    "decided it's not a warning \u2014 it's the only honest performance "
    "review in this house."
)

DEFAULT_OUTPUT = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def gate_check(text: str) -> None:
    """Gate self-check: length 1-200, single line, not only whitespace."""
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise SystemExit(f"gate failed: length {len(text)} outside 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")


def main() -> int:
    gate_check(ENTRY_TEXT)
    out_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Read-back verification: bytes on disk must equal the entry text
    # exactly — same characters, same encoding, no trailing newline.
    with open(out_path, "rb") as f:
        data = f.read()
    expected = ENTRY_TEXT.encode("utf-8")
    if data != expected:
        raise SystemExit("verification failed: output bytes differ from entry text")
    if data.endswith(b"\n"):
        raise SystemExit("verification failed: output has a trailing newline")
    print(f"verified {len(ENTRY_TEXT)} chars ({len(expected)} bytes) in {out_path}")
    print(f"wrote {len(ENTRY_TEXT)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
