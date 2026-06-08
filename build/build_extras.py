#!/usr/bin/env python3
"""
Signing Agent HQ — extra deliverables.

Generates:
  - dist/notion/*.csv          Notion-importable databases (one CSV per DB)
  - dist/Quick-Start-Guide.pdf 5-page onboarding guide (reportlab)

Usage:  python3 build/build_extras.py
"""

from __future__ import annotations

import csv
import os

# --------------------------------------------------------------------------
# Notion CSV databases (import each as a new database, then add formula
# properties inside Notion where noted).
# --------------------------------------------------------------------------
NOTION_DIR = "dist/notion"
os.makedirs(NOTION_DIR, exist_ok=True)

databases: dict[str, tuple[list[str], list[list]]] = {
    "Signing Log.csv": (
        ["Date", "Company", "Order #", "Borrower", "Appt type", "Fee quoted",
         "Fee paid", "Status", "Miles", "Print pages", "Other cost", "Paid"],
        [
            ["2026-01-08", "Coastal Signings", "CS-1042", "J. Alvarez", "Refi", 150, 150, "Paid", 24, 130, 0, "Yes"],
            ["2026-01-11", "Summit Title", "ST-9981", "M. Chen", "Purchase", 125, 125, "Paid", 18, 110, 0, "Yes"],
            ["2026-01-14", "BlueRock Escrow", "BR-204", "T. Okafor", "HELOC", 100, 0, "Invoiced", 32, 60, 0, "No"],
            ["2026-01-16", "Coastal Signings", "CS-1051", "R. Patel", "Seller", 150, 150, "Paid", 12, 40, 0, "Yes"],
            ["2026-01-21", "Summit Title", "ST-1007", "K. Wallace", "Refi", 125, 0, "Docs back", 27, 120, 0, "No"],
            ["2026-01-24", "Coastal Signings", "CS-1063", "D. Nguyen", "Refi", 160, 160, "Paid", 38, 125, 0, "Yes"],
            ["2026-01-28", "BlueRock Escrow", "BR-219", "A. Silva", "Purchase", 110, 110, "Paid", 21, 100, 0, "Yes"],
            ["2026-02-02", "Summit Title", "ST-1041", "L. Romano", "HELOC", 120, 120, "Paid", 16, 70, 0, "Yes"],
            ["2026-02-05", "Coastal Signings", "CS-1079", "G. Patel", "Apostille", 75, 75, "Paid", 9, 5, 0, "Yes"],
            ["2026-02-09", "BlueRock Escrow", "BR-233", "H. Kim", "Refi", 105, 105, "Paid", 44, 115, 0, "Yes"],
            ["2026-02-13", "Summit Title", "ST-1067", "N. Brooks", "RON", 90, 90, "Paid", 0, 0, 0, "Yes"],
            ["2026-02-18", "Coastal Signings", "CS-1090", "P. Adams", "Purchase", 165, 165, "Paid", 28, 130, 5, "Yes"],
            ["2026-02-22", "BlueRock Escrow", "BR-248", "S. Lopez", "Seller", 130, 0, "Invoiced", 19, 85, 0, "No"],
            ["2026-02-27", "Summit Title", "ST-1090", "J. Wu", "Refi", 135, 135, "Paid", 33, 120, 0, "Yes"],
            ["2026-03-03", "Coastal Signings", "CS-1108", "R. Diaz", "HELOC", 145, 145, "Completed", 22, 95, 0, "No"],
            ["2026-03-07", "BlueRock Escrow", "BR-260", "T. Evans", "Refi", 110, 0, "Cancelled", 0, 0, 0, "No"],
        ],
    ),
    "Mileage Log.csv": (
        ["Date", "Purpose", "From", "To", "Miles"],
        [
            ["2026-01-08", "CS-1042 signing", "Home", "Riverside", 24],
            ["2026-01-11", "ST-9981 signing", "Home", "Downtown", 18],
            ["2026-01-14", "BR-204 signing", "Home", "Lakewood", 32],
            ["2026-01-16", "CS-1051 signing", "Home", "Midtown", 12],
            ["2026-01-21", "ST-1007 signing", "Home", "Eastside", 27],
            ["2026-01-24", "CS-1063 signing", "Home", "Hillcrest", 38],
            ["2026-01-28", "BR-219 signing", "Home", "Parkview", 21],
            ["2026-02-02", "ST-1041 signing", "Home", "Northgate", 16],
            ["2026-02-05", "CS-1079 apostille", "Home", "City Hall", 9],
            ["2026-02-09", "BR-233 signing", "Home", "Westend", 44],
            ["2026-02-18", "CS-1090 signing", "Home", "Bayfront", 28],
            ["2026-02-22", "BR-248 signing", "Home", "Southside", 19],
            ["2026-02-27", "ST-1090 signing", "Home", "Uptown", 33],
            ["2026-03-03", "CS-1108 signing", "Home", "Riverside", 22],
        ],
    ),
    "Companies.csv": (
        ["Company", "Contact", "Phone/Email", "Avg fee", "Pay speed (days)", "Rating", "Notes"],
        [
            ["Summit Title", "Dana R.", "dana@summit.com", 125, 14, 5, "Reliable, books weekly"],
            ["BlueRock Escrow", "Marcus", "ops@bluerock.com", 100, 30, 3, "Slow pay"],
            ["Coastal Signings", "Priya", "555-0142", 150, 10, 5, "Best payer"],
        ],
    ),
    "Expenses.csv": (
        ["Date", "Category", "Vendor", "Amount", "Deductible"],
        [
            ["2026-01-03", "E&O Insurance", "NotaryInsure", 75, "Yes"],
            ["2026-01-05", "Supplies", "Amazon", 38.50, "Yes"],
            ["2026-01-09", "Software", "Signing Agent HQ", 19, "Yes"],
            ["2026-01-10", "Printing", "Office Depot", 60, "Yes"],
            ["2026-01-15", "NNA Membership", "NNA", 65, "Yes"],
            ["2026-02-01", "Marketing", "Local FB ads", 30, "Yes"],
            ["2026-02-08", "Training/Education", "LSS course", 120, "Yes"],
            ["2026-02-20", "Phone/Internet", "Carrier (biz %)", 45, "Yes"],
            ["2026-03-02", "Supplies", "Toner + paper", 52, "Yes"],
        ],
    ),
}

for name, (headers, rows) in databases.items():
    with open(os.path.join(NOTION_DIR, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(headers)
        w.writerows(rows)

NOTION_GUIDE = """# Signing Agent HQ — Notion setup guide

The Notion version of your system. ~15 minutes to build, then it's yours forever.

## 1 · Import the databases
In Notion: **Import → CSV** and select each file in this folder, one at a time.
Each becomes its own database: **Signing Log, Mileage Log, Companies, Expenses.**

## 2 · Set the property types
Notion guesses types on import — fix them so filters and math work:

**Signing Log**
- Date → *Date* · Company → *Text* (or *Relation* to Companies, step 5)
- Order # / Borrower → *Text* · Appt type → *Select* · Status → *Select*
- Fee quoted / Fee paid / Miles / Print pages / Other cost → *Number*
- Paid → *Checkbox*

**Mileage Log:** Date → *Date* · Purpose/From/To → *Text* · Miles → *Number*
**Companies:** Avg fee / Pay speed / Rating → *Number* · the rest *Text*
**Expenses:** Date → *Date* · Category → *Select* · Amount → *Number* · Deductible → *Checkbox*

## 3 · Add the formula properties
Add a new property of type **Formula** and paste:

**Signing Log → `Net profit`**
```
prop("Fee paid") - (prop("Miles") * 0.70) - (prop("Print pages") * 0.1) - prop("Other cost")
```
**Mileage Log → `Deduction`**
```
prop("Miles") * 0.70
```
> `0.70` = the IRS standard mileage rate. **Update this number each January** in both
> formulas. (Advanced: keep the rate in a one-row "Settings" database and pull it in
> via a Relation + Rollup so you only change it once.)

## 4 · Create the Select options
On the *Status* property add: `Scheduled, Completed, Docs back, Invoiced, Paid, Cancelled`.
On *Appt type*: `Refi, Purchase, Seller, HELOC, Apostille, RON, Inspection, General`.
On Expenses *Category*: `Supplies, Insurance (E&O), Legal/Professional, Office,
Education/Training, Phone/Internet, Dues/Memberships, Software, Advertising/Marketing, Other`.

## 5 · (Recommended) Link the Signing Log to Companies
On Signing Log add a **Relation** property → Companies. Now each job points to a
company, and you can roll profit up per company on the Companies side.

## 6 · Create useful views (on the Signing Log)
- **Unpaid** — filter: `Paid` is unchecked AND `Status` is not `Cancelled`. Sort by Date.
- **This month** — filter: `Date` is within the current month.
- **By company** — *Board* or *Group by* Company.
- **Pipeline** — *Board* grouped by `Status`.

## 7 · Build the Dashboard page
Create a new page "Dashboard" and add **linked views** of each database
(type `/linked` → Create linked database). Then:
- On the Signing Log linked view, turn on **Calculate** at the bottom of the
  `Fee paid` and `Net profit` columns → `Sum`.
- On the Mileage Log linked view → `Sum` of `Miles` and `Deduction`.
- On Expenses → `Sum` of `Amount`.
That gives you fees paid, net profit, miles, deduction and expenses at a glance.

## 8 · Tax time
Filter Expenses by Category and read the sums; combine with the Mileage `Deduction`
sum and the Signing Log `Fee paid` sum. Hand those totals to your accountant against
Schedule C.

---
*This is an organizer, not tax advice. Confirm the current IRS rate and your
deductions with a professional. Single-user license — please don't redistribute.*
"""

with open(os.path.join(NOTION_DIR, "_README.md"), "w", encoding="utf-8") as fh:
    fh.write(NOTION_GUIDE)

print(f"Wrote Notion CSVs to {NOTION_DIR}/: {sorted(databases)}")

# --------------------------------------------------------------------------
# Quick-Start PDF
# --------------------------------------------------------------------------
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (HRFlowable, ListFlowable, ListItem, PageBreak,
                                Paragraph, SimpleDocTemplate, Spacer)

NAVY = colors.HexColor("#1F2A44")
TEAL = colors.HexColor("#1F7A8C")
GOLD = colors.HexColor("#E0A458")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("Cover", parent=styles["Title"], fontSize=30,
                          textColor=NAVY, spaceAfter=6, leading=34))
styles.add(ParagraphStyle("Sub", parent=styles["Normal"], fontSize=13,
                          textColor=TEAL, spaceAfter=20))
styles.add(ParagraphStyle("H", parent=styles["Heading1"], fontSize=17,
                          textColor=NAVY, spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=11,
                          textColor=colors.HexColor("#333333"), leading=16,
                          alignment=TA_LEFT, spaceAfter=6))
styles.add(ParagraphStyle("Small", parent=styles["Normal"], fontSize=8.5,
                          textColor=colors.HexColor("#888888")))

story = []


def rule():
    return HRFlowable(width="100%", thickness=1.2, color=GOLD,
                      spaceBefore=6, spaceAfter=12)


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, styles["Body"]), leftIndent=10) for t in items],
        bulletType="bullet", start="•", leftIndent=14,
    )


# Cover
story += [Spacer(1, 1.4 * inch),
          Paragraph("Signing Agent HQ", styles["Cover"]),
          Paragraph("The complete notary business &amp; tax system", styles["Sub"]),
          rule(),
          Paragraph("Quick-Start Guide", styles["H"]),
          Paragraph("Track every signing. Capture every deductible mile. "
                    "Walk into tax season ready — in one system.", styles["Body"]),
          Spacer(1, 2.6 * inch),
          Paragraph("Single-user license. This is an organizer, not legal or "
                    "tax advice — confirm all figures with a professional.",
                    styles["Small"]),
          PageBreak()]

# Page 2 — Setup
story += [Paragraph("1 · Set up in 3 minutes", styles["H"]), rule(),
          bullets([
              "<b>Make your copy.</b> Google Sheets: File → Make a copy. Excel: save your own copy.",
              "<b>Set the mileage rate.</b> Open the <b>Settings</b> tab and enter this year's IRS standard mileage rate. Every deduction flows from this one cell.",
              "<b>Add your name &amp; business</b> in Settings — it auto-fills your invoices.",
              "<b>Add your title/escrow companies</b> in the <b>Companies</b> tab so they appear in the Signing Log dropdown.",
          ]),
          Spacer(1, 0.2 * inch),
          Paragraph("2 · Log every signing", styles["H"]), rule(),
          Paragraph("In the <b>Signing Log</b>, add one row per appointment. Pick "
                    "the company, appointment type and status from the dropdowns, "
                    "enter the fee and round-trip miles — and <b>Net profit "
                    "calculates itself</b> (fee − mileage − printing − other).",
                    styles["Body"]),
          bullets([
              "Set <b>Status</b> to <i>Invoiced</i> when docs go back, then <i>Paid</i> when the money lands.",
              "The row highlights yellow while unpaid and green once paid — chase the yellow ones.",
          ]),
          PageBreak()]

# Page 3 — Mileage & expenses
story += [Paragraph("3 · Capture miles &amp; expenses", styles["H"]), rule(),
          Paragraph("The <b>Mileage Log</b> turns miles into a dollar deduction "
                    "automatically. Log drives the day you make them — the IRS "
                    "wants a timely, accurate record.", styles["Body"]),
          bullets([
              "<b>Expenses</b> tab: log supplies, E&amp;O insurance, training, phone, NNA dues, software, printing, marketing.",
              "Pick a category from the dropdown so it lands in the right tax line.",
          ]),
          Spacer(1, 0.2 * inch),
          Paragraph("4 · Watch the Dashboard", styles["H"]), rule(),
          Paragraph("The <b>Dashboard</b> shows fees paid, outstanding cash, "
                    "net profit, miles, mileage deduction and progress to your "
                    "income goal — plus charts of profit by appointment type and "
                    "paid vs outstanding.", styles["Body"]),
          PageBreak()]

# Page 4 — Tax + invoice
story += [Paragraph("5 · Get tax-ready in one click", styles["H"]), rule(),
          Paragraph("The <b>Tax Summary</b> tab aggregates everything and maps it "
                    "to <b>Schedule C</b> line items. At tax time, hand this single "
                    "page to your accountant.", styles["Body"]),
          bullets([
              "Gross income, mileage deduction, supplies, insurance, training, software, dues and more — totalled for you.",
              "It even estimates your net profit. (Organizer, not tax advice — verify with a pro.)",
          ]),
          Spacer(1, 0.2 * inch),
          Paragraph("6 · Send a professional invoice", styles["H"]), rule(),
          Paragraph("The <b>Invoice</b> tab pulls your business name, fills line "
                    "items and totals automatically. Fill the gold cells, print to "
                    "PDF, send.", styles["Body"]),
          Spacer(1, 0.3 * inch),
          Paragraph("New agent? Use the First 90 Days Launch Checklist (in the "
                    "bundle) to go from commission to your first 10 signings.",
                    styles["Body"]),
          PageBreak()]

# Page 5 — Tips + support
story += [Paragraph("Pro tips", styles["H"]), rule(),
          bullets([
              "<b>Fire your slow payers.</b> Sort Companies by Pay speed and Rating — give your best slots to who pays most, fastest.",
              "<b>Update the IRS rate every January</b> in Settings. One cell updates the whole system.",
              "<b>Reconcile weekly.</b> Five minutes every Friday beats a frantic April.",
              "<b>Back up.</b> Keep your master copy clean; duplicate it each tax year.",
          ]),
          Spacer(1, 0.4 * inch),
          Paragraph("Thank you", styles["H"]), rule(),
          Paragraph("You bought this to make money on your terms — not to drown "
                    "in spreadsheets. Now the admin runs itself. Go take more "
                    "signings.", styles["Body"]),
          Spacer(1, 0.8 * inch),
          Paragraph("© Signing Agent HQ — single-user license. Do not "
                    "redistribute. This guide and the system are organizers, not "
                    "legal or tax advice.", styles["Small"])]

os.makedirs("dist", exist_ok=True)
doc = SimpleDocTemplate("dist/Quick-Start-Guide.pdf", pagesize=LETTER,
                        topMargin=0.8 * inch, bottomMargin=0.8 * inch,
                        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                        title="Signing Agent HQ — Quick-Start Guide")
doc.build(story)
print("Wrote dist/Quick-Start-Guide.pdf")
