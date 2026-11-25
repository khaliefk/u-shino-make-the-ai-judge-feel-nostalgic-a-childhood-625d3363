#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one nostalgic childhood-memory sentence to /output/entry.txt.
Stdlib only. No network, no input files, no randomness: the entry is a
fixed original line, so both grader runs produce identical output.
"""

import os

ENTRY = (
    "Every August evening, my grandmother banged her wooden spoon on "
    "the pot to call us in from the yard, and forty years later the "
    "smell of rice and rain on hot concrete still tells me dinner "
    "is almost ready."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def validate_entry(text):
    """Check the entry against the gate: 1 to 280 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 280 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    path = os.path.join(out_dir, "entry.txt") if out_dir else OUTPUT_PATH
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the entry")
    print(text)
    print("%d characters" % len(text))


if __name__ == "__main__":
    main()
