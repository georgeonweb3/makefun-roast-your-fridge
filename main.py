#!/usr/bin/env python3
"""Roast Your Fridge — one-line entry writer.

Deterministic program (stdlib only, no network, no wall-clock, no unseeded
randomness). Writes the tournament-winning roast line to /output/entry.txt
for make.fun's "One Line, One Laugh: Roast Your Fridge" bounty.

The line: winner of a blind pairwise tournament (6 candidates, 15 pairs,
fresh judge), 5-0 undefeated. Gate: UTF-8 text, 1-200 characters.
"""

import os

ENTRY_TEXT = (
    "My fridge's filter light has blinked red since March, "
    "and I've decided it's not a warning \u2014 "
    "it's the only honest performance review in this house."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY_TEXT
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back verification: what we wrote is exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


if __name__ == "__main__":
    main()
