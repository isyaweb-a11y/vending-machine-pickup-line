#!/usr/bin/env python3
"""The Vending Machine Pickup Line.

A pickup line spoken by the vending machine itself, in its own world:
a slot code (B7), something sweet dropping, and the exact-change gag
as the punchline — a machine that never gives exact change, especially
not on a first date. Short, speakable in one breath, and the laugh
arrives in the last few words.

Writes the line to /output/entry.txt. Stdlib only, no network.
"""

import os

LINE = (
    "Hey, beautiful — press B7 and I'll drop something sweet, but fair "
    "warning, I never give exact change on a first date."
)

# The gate allows 1 to 200 characters.
MAX_CHARS = 200


def check_line_form(text: str) -> None:
    """The line must be spoken by the machine in its own world: a slot
    code, something sweet dropping, and the exact-change gag as the
    closing punch."""
    assert "B7" in text, "the line uses the machine's slot code"
    assert "exact change" in text, "the punchline is the machine's change"
    assert text.rstrip(".").endswith("first date"), "the laugh lands last"


def entry_text() -> str:
    """Return the pickup line, checked against the bounty's gate."""
    text = LINE.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 200-char gate"
    assert "\n" not in text, "the entry must be exactly one line"
    check_line_form(text)
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
