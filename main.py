"""Ship It Friday entry writer.

Writes the competition entry line to entry.txt in the output dir
(defaults to /output, overridable via MAKEFUN_OUTPUT_DIR).
"""

import os
from pathlib import Path

ENTRY_LINE = (
    "feat: deploy to prod Friday 4:59 p.m. "
    "Tests green, docs updated, and I have never felt more alive."
)


def write_entry(output_dir: str | None = None) -> Path:
    directory = Path(output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    directory.mkdir(parents=True, exist_ok=True)
    entry_path = directory / "entry.txt"
    entry_path.write_text(ENTRY_LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
