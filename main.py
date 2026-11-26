"""Warning Label for Humans: One Line, Big Laugh.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line must stay within the bounty's 160-character limit.
"""

from pathlib import Path
import os

LINE = "WARNING: This human requires eight hours of sleep and three cups of coffee daily. Do not operate before the second cup."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_line(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


def main() -> None:
    # Second revision: kept the label's second sentence as a real "Do not operate" instruction so the form, not just the joke, reads like a printed warning.
    write_line(entry_path())


if __name__ == "__main__":
    main()
