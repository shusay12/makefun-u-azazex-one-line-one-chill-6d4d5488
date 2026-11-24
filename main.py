#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (1-200 characters) to /output/entry.txt.
Python 3.13 standard library only; no network, no randomness, no input files.
The text is fixed: the program is deterministic, so every run produces the
same bytes.
"""

import os

ENTRY = (
    "The dentist turned the X-ray toward me: a second set of teeth growing "
    "behind mine, and the new ones are already chewing."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
