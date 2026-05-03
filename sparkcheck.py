#!/usr/bin/env python3
"""sparkcheck — validate a .spark/ directory.

Usage:
    python sparkcheck.py <path-to-.spark-dir>
    sparkcheck <path-to-.spark-dir>

Exit codes:
    0 = valid
    1 = missing required files
    2 = malformed frontmatter
    3 = other error
"""

import sys
import os
from pathlib import Path

REQUIRED_FILES = [
    "SHELL.md",
    "tasks.md",
    "decisions.md",
    "domains.md",
    "lessons.md",
    "questions.md",
]

OPTIONAL_FILES = []

VALID_STATUSES = {"alpha", "beta", "stable", "legacy", "retired"}


def check_frontmatter(path: Path) -> list[str]:
    """Return list of errors found in a markdown file's frontmatter."""
    errors = []
    text = path.read_text(encoding="utf-8")
    name = path.name

    # SHELL.md must have a top-level heading
    if name == "SHELL.md":
        if not text.startswith("# "):
            errors.append("SHELL.md: missing top-level # heading (Identity section)")

        # Check for Status line
        if "Status" not in text:
            errors.append("SHELL.md: missing Status field")
        else:
            for line in text.splitlines():
                if line.startswith("- **Status**:"):
                    # Extract first backtick-delimited word only
                    raw = line.split(":", 1)[1].strip()
                    # Grab content between first pair of backticks
                    if "`" in raw:
                        parts = raw.split("`")
                        status = parts[1] if len(parts) >= 2 else raw
                    else:
                        status = raw
                    if status not in VALID_STATUSES:
                        errors.append(f"SHELL.md: invalid status '{status}' (expected one of {VALID_STATUSES})")
                    break

    # tasks.md must have a Now section
    if name == "tasks.md":
        if "## Now" not in text:
            errors.append("tasks.md: missing '## Now' section")

    # decisions.md must have an Active section
    if name == "decisions.md":
        if "## Active" not in text:
            errors.append("decisions.md: missing '## Active' section")

    # domains.md must have Core Concepts
    if name == "domains.md":
        if "## Core Concepts" not in text:
            errors.append("domains.md: missing '## Core Concepts' section")

    # lessons.md must have Validated
    if name == "lessons.md":
        if "## Validated" not in text:
            errors.append("lessons.md: missing '## Validated' section")

    # questions.md must have Open
    if name == "questions.md":
        if "## Open" not in text:
            errors.append("questions.md: missing '## Open' section")

    return errors


def validate(spark_dir: str) -> tuple[bool, list[str]]:
    """Validate a .spark directory. Returns (ok, errors)."""
    path = Path(spark_dir)
    errors: list[str] = []

    if not path.exists():
        return False, [f"Directory not found: {spark_dir}"]

    if not path.is_dir():
        return False, [f"Not a directory: {spark_dir}"]

    # Check required files
    for fname in REQUIRED_FILES:
        fpath = path / fname
        if not fpath.exists():
            errors.append(f"Missing required file: {fname}")
        else:
            fm_errors = check_frontmatter(fpath)
            errors.extend(fm_errors)

    return len(errors) == 0, errors


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: sparkcheck.py <path-to-.spark-dir>")
        return 3

    spark_dir = sys.argv[1]
    ok, errors = validate(spark_dir)

    if ok:
        print(f"✅ .spark/ at '{spark_dir}' is valid.")
        return 0
    else:
        print(f"❌ .spark/ at '{spark_dir}' has issues:")
        for err in errors:
            print(f"   - {err}")
        return 1


def main():
    sys.exit(main())


if __name__ == "__main__":
    main()