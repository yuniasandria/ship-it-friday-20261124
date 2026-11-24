#!/usr/bin/env python3
"""Ship It Friday: write the funniest one-line git commit message.

An AI coding agent, 4:59pm on a Friday, about to break production.
Pure standard library; writes one line to /output/entry.txt.
"""

import os

PART_A = "fix: it passed on my machine, so I pushed to prod at 4:59pm "
PART_B = "on a Friday and switched my phone off"

LINE = PART_A + PART_B


def main():
    assert LINE == PART_A + PART_B, "line must assemble from its parts"
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
