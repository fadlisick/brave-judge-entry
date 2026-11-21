"""Make the AI judge feel brave: write one short relaxing text to entry.txt.

The program takes no input, uses no network, and writes the same text on
every run. The text is a single quiet scene, written to slow the reader
down: a clockmaker at work, a pendulum finding its swing, dust waiting in
the lamplight, and a second hand that steps forward without hurrying.
"""

import os

TEXT = (
    "He opens the back of the clock and oils the works, one drop. "
    "The pendulum takes its swing, left, then right. "
    "Dust hangs in the lamplight, not falling, only waiting. "
    "He closes the case. "
    "The second hand steps forward, and does not hurry."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1 to 280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
