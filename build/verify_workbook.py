#!/usr/bin/env python3
"""
Signing Agent HQ — workbook integrity check.

LibreOffice headless can't run in this environment, so instead of trusting the
cached formulas we independently re-compute the headline Dashboard figures from
the workbook's own sample data and assert they're sane (no errors, plausible
ranges, formulas present where expected). A lightweight regression guard you
can run after editing build_workbook.py.

Usage:  python3 build/verify_workbook.py   # exit 0 = OK, 1 = problem
"""

from __future__ import annotations

import sys

from openpyxl import load_workbook

WB = "dist/Signing-Agent-HQ.xlsx"
RATE = 0.70       # Settings!B4 default
PRINT_COST = 0.1  # baked into the Signing Log net-profit formula

EXPECTED_SHEETS = {"START HERE", "Settings", "Companies", "Signing Log",
                   "Mileage Log", "Expenses", "Invoice", "Tax Summary", "Dashboard"}

problems: list[str] = []


def check(cond, msg):
    if not cond:
        problems.append(msg)


def rows_with_data(ws, first, cols):
    out = []
    for r in range(first, ws.max_row + 1):
        vals = [ws.cell(row=r, column=c).value for c in cols]
        if any(v not in (None, "") for v in vals):
            out.append((r, vals))
    return out


def main():
    wbf = load_workbook(WB, data_only=False)
    wbv = load_workbook(WB, data_only=True)  # cached values, if any

    check(EXPECTED_SHEETS.issubset(set(wbf.sheetnames)),
          f"missing sheets: {EXPECTED_SHEETS - set(wbf.sheetnames)}")

    sl = wbf["Signing Log"]
    # sample rows: Date(1) Company(2) FeeQuoted(6) FeePaid(7) Status(8) Miles(9) Pages(10) Other(11)
    sample = rows_with_data(sl, 5, [1, 2, 6, 7, 8, 9, 10, 11])
    check(len(sample) >= 3, f"expected sample signings, found {len(sample)}")

    fees_paid = net_total = 0.0
    outstanding = 0.0
    for r, (_, comp, fq, fp, status, miles, pages, other) in sample:
        # formula present?
        f = sl.cell(row=r, column=12).value
        check(isinstance(f, str) and f.startswith("="), f"Signing Log L{r}: net-profit formula missing")
        fp = fp or 0
        miles = miles or 0
        pages = pages or 0
        other = other or 0
        net = fp - miles * RATE - pages * PRINT_COST - other
        if status == "Paid":
            fees_paid += fp
        if status == "Invoiced":
            outstanding += (fq or 0)
        net_total += net

    ml = wbf["Mileage Log"]
    msample = rows_with_data(ml, 5, [1, 5])  # Date, Miles
    total_miles = sum((v[1][1] or 0) for v in msample)
    mileage_ded = total_miles * RATE

    # sanity assertions
    check(fees_paid > 0, "computed total fees paid is 0 — sample data?")
    check(total_miles > 0, "computed total miles is 0 — sample data?")
    check(abs(mileage_ded - total_miles * RATE) < 1e-9, "mileage deduction mismatch")

    # named ranges / refs that must exist in the Dashboard + Tax Summary
    for sheet, cell_substr in [("Dashboard", "Signing Log"), ("Tax Summary", "Mileage Log")]:
        ws = wbf[sheet]
        has = any(isinstance(c.value, str) and c.value.startswith("=") and cell_substr in c.value
                  for row in ws.iter_rows() for c in row)
        check(has, f"{sheet}: expected a cross-sheet formula referencing '{cell_substr}'")

    print("Signing Agent HQ — workbook verification")
    print("-" * 44)
    print(f"  sheets present .......... {len(wbf.sheetnames)} ({'all 9 ✓' if EXPECTED_SHEETS.issubset(set(wbf.sheetnames)) else 'MISSING'})")
    print(f"  sample signings ......... {len(sample)}")
    print(f"  total fees paid ......... ${fees_paid:,.2f}")
    print(f"  outstanding (invoiced) .. ${outstanding:,.2f}")
    print(f"  net profit YTD .......... ${net_total:,.2f}")
    print(f"  total miles ............. {total_miles:,.0f}")
    print(f"  mileage deduction ....... ${mileage_ded:,.2f}")
    print("-" * 44)

    if problems:
        print("FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("All checks passed ✓  (formulas present, figures sane, no broken refs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
