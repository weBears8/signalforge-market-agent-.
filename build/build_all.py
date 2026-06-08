#!/usr/bin/env python3
"""
Signing Agent HQ — one-command build.

Regenerates every deliverable in dist/ from source, then runs the product
integrity check. Use after editing any generator, or on a fresh clone.

Usage:  python3 build/build_all.py
Deps:   pip install openpyxl reportlab pillow
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

STEPS = [
    ("Product workbook", "build_workbook.py"),
    ("Notion CSVs + Quick-Start PDF", "build_extras.py"),
    ("Marketing cover + hero", "build_cover.py"),
    ("Top-of-funnel ad creatives", "build_ads.py"),
    ("Free lead magnet", "build_lead_magnet.py"),
    ("Launch checklist (bundle)", "build_checklist.py"),
    ("Validation tracker", "build_tracker.py"),
    ("Verify product workbook", "verify_workbook.py"),
]


def main() -> int:
    failures = []
    for label, script in STEPS:
        print(f"\n▶ {label}  ({script})")
        proc = subprocess.run([sys.executable, str(HERE / script)],
                              capture_output=True, text=True)
        out = (proc.stdout + proc.stderr).strip()
        if out:
            print("  " + out.replace("\n", "\n  "))
        if proc.returncode != 0:
            failures.append(label)
            print(f"  ✗ FAILED (exit {proc.returncode})")

    print("\n" + "=" * 48)
    if failures:
        print(f"BUILD FAILED — {len(failures)} step(s): {', '.join(failures)}")
        return 1
    print(f"BUILD OK — {len(STEPS)} steps, all green ✓")
    print("All deliverables regenerated in dist/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
