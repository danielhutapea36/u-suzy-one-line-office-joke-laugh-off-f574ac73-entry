"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt. The program is fully deterministic: the same joke,
byte for byte, on every run.
"""

import os
from pathlib import Path

JOKE = "HR said my salary is confidential, which is convenient, because so is my job search."

# The competition gate: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def validate(text: str) -> str:
    """Enforce the competition gate before anything is written."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def run() -> Path:
    """Write the joke to the output file and return its path."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(validate(JOKE) + "\n", encoding="utf-8")
    return OUTPUT_PATH


if __name__ == "__main__":
    path = run()
    print(f"Wrote {path} ({len(JOKE)} characters)")
