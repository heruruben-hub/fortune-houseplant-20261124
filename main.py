"""Fortune in a Pot — entry for make.fun.

Writes one kind, funny fortune for the houseplant on the windowsill
to /output/entry.txt. The fortune is a single line of at most 120
characters: a prediction about the plant's own future, warm toward
both the plant and its keeper, with a small joke that lands — the
keeper taking all the credit for a leaf the plant grew itself.
"""

import os

FORTUNE = (
    "Soon your newest leaf will unfurl toward the sun, "
    "and your keeper will tell everyone it was all their doing."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune must be 1-120 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
