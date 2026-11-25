#!/usr/bin/env python3
"""One-line fridge roast.

Writes a single roast of my fridge -- one line, at most 200 characters --
to /output/entry.txt. Pure Python standard library, fully deterministic:
the same line every run.
"""

import os

ROAST = (
    "My fridge hums a lullaby to leftovers it plans to murder by Friday, "
    "then beeps at me like I'm the intruder."
)


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("roast must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
