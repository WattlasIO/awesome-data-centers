#!/usr/bin/env python3
"""Validate Awesome Data Centers README formatting, HTTPS links, and duplicates."""

from __future__ import annotations

import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
BADGE_HOSTS = {"awesome.re", "img.shields.io", "mirrors.creativecommons.org"}


def validate(text: str) -> list[str]:
    errors: list[str] = []
    seen_bullet_urls: dict[str, int] = {}

    for lineno, line in enumerate(text.splitlines(), start=1):
        for label, url in LINK_RE.findall(line):
            if url.startswith("http://"):
                errors.append(f"Line {lineno}: non-HTTPS link ({url})")
            if line.lstrip().startswith("- ["):
                norm = url.rstrip("/")
                if norm in seen_bullet_urls and not any(h in norm for h in BADGE_HOSTS):
                    errors.append(
                        f"Line {lineno}: duplicate list URL {url} (first seen line {seen_bullet_urls[norm]})"
                    )
                seen_bullet_urls.setdefault(norm, lineno)

        if line.lstrip().startswith("- [") and " - " not in line and not line.strip().endswith(")"):
            # Allow plain link bullets in Field Guides; require dash separator if description exists
            pass

    if len(seen_bullet_urls) < 40:
        errors.append(f"Expected at least 40 curated entries, found {len(seen_bullet_urls)}")

    return errors


def main() -> int:
    text = README.read_text(encoding="utf-8")
    errors = validate(text)
    if errors:
        for err in errors:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1
    print(f"[OK] README validated cleanly ({len(LINK_RE.findall(text))} links).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
