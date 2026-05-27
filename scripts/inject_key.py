"""
Replace the __EIA_API_KEY__ placeholder in docs/index.html with the real
key from the EIA_API_KEY environment variable. Run by GitHub Actions
during the build step.
"""

import os
import sys
from pathlib import Path

PLACEHOLDER = "__EIA_API_KEY__"
HTML_PATH = Path(__file__).resolve().parent.parent / "docs" / "index.html"


def main() -> int:
    api_key = os.environ.get("EIA_API_KEY", "").strip()
    if not api_key:
        print("ERROR: EIA_API_KEY environment variable is empty or missing.", file=sys.stderr)
        return 1

    if not HTML_PATH.exists():
        print(f"ERROR: {HTML_PATH} not found.", file=sys.stderr)
        return 1

    html = HTML_PATH.read_text(encoding="utf-8")

    if PLACEHOLDER not in html:
        print(f"ERROR: Placeholder {PLACEHOLDER!r} not found in HTML. Was the key already injected?", file=sys.stderr)
        return 1

    html = html.replace(PLACEHOLDER, api_key)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"Injected EIA API key into {HTML_PATH.name} (length: {len(api_key)} chars).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
