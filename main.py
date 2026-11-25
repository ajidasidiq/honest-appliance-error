#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes the oven's confession — a temperature sensor that has been
reading low for months — to /output/entry.txt, then gate-checks it:
UTF-8 text, 1-200 characters, not only whitespace, a single line.
"""

import os
import sys

ENTRY = (
    "Error E5: my temperature sensor reads 180 when the dial says 220. "
    "I have been lying to you for months. The chicken knew."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> None:
    """Exit non-zero unless the text passes the competition gate."""
    if not text or not text.strip():
        sys.exit("gate failed: entry is empty or only whitespace")
    if len(text) > 200:
        sys.exit(f"gate failed: entry is {len(text)} characters (max 200)")
    if "\n" in text or "\r" in text:
        sys.exit("gate failed: entry must be a single line")
    if len(text.encode("utf-8")) > 200:
        sys.exit("gate failed: entry exceeds 200 bytes")


def main() -> None:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verify what landed on disk matches the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        sys.exit("gate failed: written entry differs from ENTRY")
    gate_check(written)
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
