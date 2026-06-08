#!/usr/bin/env python3
"""
Signing Agent HQ — workbook generator.

Builds a working .xlsx (importable into Google Sheets / Excel) for mobile
notaries and loan signing agents: signing CRM, IRS-ready mileage log, net
profit per job, title-company rolodex, expenses, invoice, dashboard and a
Schedule C tax summary. Live formulas, dropdowns, conditional formatting,
charts and sample data included.

Usage:
    python3 build/build_workbook.py
Output:
    dist/Signing-Agent-HQ.xlsx
"""

from __future__ import annotations

import os

from openpyxl import Workbook
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------
NAVY = "1F2A44"
TEAL = "1F7A8C"
GOLD = "E0A458"
LIGHT = "EEF2F6"
GREEN = "2E7D32"
RED = "C62828"
WHITE = "FFFFFF"

H1 = Font(name="Calibri", size=20, bold=True, color=WHITE)
H2 = Font(name="Calibri", size=13, bold=True, color=WHITE)
HDR = Font(name="Calibri", size=11, bold=True, color=WHITE)
BOLD = Font(name="Calibri", size=11, bold=True, color=NAVY)
NOTE = Font(name="Calibri", size=10, italic=True, color="566173")
BIG = Font(name="Calibri", size=22, bold=True, color=NAVY)

CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)
RIGHT = Alignment(horizontal="right", vertical="center")

thin = Side(style="thin", color="C7D0DA")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

CURRENCY = '"$"#,##0.00'
MILES = "#,##0.0"


def fill(hexcolor: str) -> PatternFill:
    return PatternFill("solid", fgColor=hexcolor)


def banner(ws, title: str, subtitle: str, span: int) -> None:
    last = get_column_letter(span)
    ws.merge_cells(f"A1:{last}1")
    ws["A1"] = title
    ws["A1"].fill = fill(NAVY)
    ws["A1"].font = H1
    ws["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 38
    ws.merge_cells(f"A2:{last}2")
    ws["A2"] = subtitle
    ws["A2"].fill = fill(TEAL)
    ws["A2"].font = H2
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[2].height = 22


def header_row(ws, row: int, headers: list[str]) -> None:
    for c, text in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=c, value=text)
        cell.fill = fill(TEAL)
        cell.font = HDR
        cell.alignment = CENTER
        cell.border = BORDER


# ---------------------------------------------------------------------------
wb = Workbook()

# === Settings (lists + IRS rate) ===========================================
sett = wb.active
sett.title = "Settings"
banner(sett, "⚙️  Settings", "Update once a year. Everything else flows from here.", 6)

sett["A4"] = "IRS standard mileage rate (this year)"
sett["A4"].font = BOLD
sett["B4"] = 0.70  # placeholder — user updates with the official annual rate
sett["B4"].number_format = '"$"#,##0.000'
sett["B4"].fill = fill(GOLD)
sett["B4"].font = Font(bold=True, color=NAVY)
sett["B4"].alignment = CENTER
sett["B4"].border = BORDER
sett["C4"] = "← enter the official IRS rate for the current tax year"
sett["C4"].font = NOTE

sett["A6"] = "Business name"
sett["A6"].font = BOLD
sett["B6"] = "Your Notary Business, LLC"
sett["A7"] = "Your name"
sett["A7"].font = BOLD
sett["B7"] = "Your Name"

# list columns used by dropdowns
lists = {
    "E": ("Appt types", ["Refi", "Purchase", "Seller", "HELOC", "Reverse",
                          "Apostille", "RON", "Inspection", "General Notary"]),
    "F": ("Status", ["Scheduled", "Completed", "Docs back", "Invoiced",
                     "Paid", "Cancelled"]),
    "G": ("Expense categories", ["Mileage", "Supplies", "E&O Insurance",
                                 "Training/Education", "Phone/Internet",
                                 "NNA Membership", "Software", "Marketing",
                                 "Printing", "Other"]),
}
for col, (title, values) in lists.items():
    sett[f"{col}3"] = title
    sett[f"{col}3"].font = BOLD
    for i, v in enumerate(values, start=4):
        sett[f"{col}{i}"] = v
sett.column_dimensions["A"].width = 34
for col in "BCDEFG":
    sett.column_dimensions[col].width = 20

APPT_REF = "=Settings!$E$4:$E$12"
STATUS_REF = "=Settings!$F$4:$F$9"
CAT_REF = "=Settings!$G$4:$G$13"
RATE = "Settings!$B$4"

# === Companies (Rolodex) ===================================================
comp = wb.create_sheet("Companies")
banner(comp, "🏢  Title / Escrow Companies", "Rate who pays best and fastest — fire the slow payers.", 7)
comp_headers = ["Company", "Contact", "Phone / Email", "Avg fee", "Pay speed (days)", "Rating ★ (1-5)", "Notes"]
header_row(comp, 4, comp_headers)
comp_sample = [
    ["Summit Title", "Dana R.", "dana@summit.com", 125, 14, 5, "Reliable, books weekly"],
    ["BlueRock Escrow", "Marcus", "ops@bluerock.com", 100, 30, 3, "Slow pay, chase invoices"],
    ["Coastal Signings", "Priya", "555-0142", 150, 10, 5, "Best payer — prioritize"],
]
for r, row in enumerate(comp_sample, start=5):
    for c, val in enumerate(row, start=1):
        cell = comp.cell(row=r, column=c, value=val)
        cell.border = BORDER
        cell.alignment = LEFT if c in (1, 2, 3, 7) else CENTER
        if c == 4:
            cell.number_format = CURRENCY
for r in range(8, 60):
    for c in range(1, 8):
        comp.cell(row=r, column=c).border = BORDER
widths = [20, 16, 22, 12, 16, 14, 30]
for c, w in enumerate(widths, start=1):
    comp.column_dimensions[get_column_letter(c)].width = w
COMPANY_REF = "=Companies!$A$5:$A$59"

# === Signing Log (CRM) =====================================================
log = wb.create_sheet("Signing Log")
banner(log, "🖊️  Signing Log + CRM", "One row per appointment. Net profit calculates itself.", 13)
log_headers = ["Date", "Company", "Order #", "Borrower", "Appt type",
               "Fee quoted", "Fee paid", "Status", "Miles (round-trip)",
               "Print pages", "Other cost", "Net profit", "Paid?"]
header_row(log, 4, log_headers)

LAST = 304  # rows 5..304 = 300 signings
for r in range(5, LAST + 1):
    # F=fee quoted, G=fee paid, I=miles, J=pages, K=other
    log.cell(row=r, column=12,
             value=(f"=IF(G{r}=\"\",\"\",G{r}-(I{r}*{RATE})-(J{r}*0.1)-K{r})"))
    log.cell(row=r, column=13, value=f'=IF(H{r}="Paid","✔","")')
    for c in range(1, 14):
        cell = log.cell(row=r, column=c)
        cell.border = BORDER
        cell.alignment = CENTER
    log.cell(row=r, column=1).number_format = "yyyy-mm-dd"
    for c in (6, 7, 11, 12):
        log.cell(row=r, column=c).number_format = CURRENCY
    log.cell(row=r, column=9).number_format = MILES

sample = [
    ["2026-01-08", "Coastal Signings", "CS-1042", "J. Alvarez", "Refi", 150, 150, "Paid", 24, 130, 0],
    ["2026-01-11", "Summit Title", "ST-9981", "M. Chen", "Purchase", 125, 125, "Paid", 18, 110, 0],
    ["2026-01-14", "BlueRock Escrow", "BR-204", "T. Okafor", "HELOC", 100, 0, "Invoiced", 32, 60, 0],
    ["2026-01-16", "Coastal Signings", "CS-1051", "R. Patel", "Seller", 150, 150, "Paid", 12, 40, 0],
    ["2026-01-21", "Summit Title", "ST-1007", "K. Wallace", "Refi", 125, 0, "Docs back", 27, 120, 0],
]
for i, row in enumerate(sample, start=5):
    for c, val in enumerate(row, start=1):
        cell = log.cell(row=i, column=c, value=val)
        if c in (6, 7, 11):
            cell.number_format = CURRENCY
        if c == 9:
            cell.number_format = MILES

log_widths = [12, 18, 11, 14, 13, 12, 11, 12, 15, 12, 11, 13, 8]
for c, w in enumerate(log_widths, start=1):
    log.column_dimensions[get_column_letter(c)].width = w
log.freeze_panes = "A5"

# dropdowns
dv_company = DataValidation(type="list", formula1=COMPANY_REF, allow_blank=True)
dv_appt = DataValidation(type="list", formula1=APPT_REF, allow_blank=True)
dv_status = DataValidation(type="list", formula1=STATUS_REF, allow_blank=True)
log.add_data_validation(dv_company); dv_company.add(f"B5:B{LAST}")
log.add_data_validation(dv_appt); dv_appt.add(f"E5:E{LAST}")
log.add_data_validation(dv_status); dv_status.add(f"H5:H{LAST}")

# highlight unpaid/invoiced rows on Status column
log.conditional_formatting.add(
    f"H5:H{LAST}",
    CellIsRule(operator="equal", formula=['"Invoiced"'], fill=fill("FFF3CD")))
log.conditional_formatting.add(
    f"H5:H{LAST}",
    CellIsRule(operator="equal", formula=['"Paid"'], fill=fill("D7F0DB")))

# === Mileage Log ===========================================================
mil = wb.create_sheet("Mileage Log")
banner(mil, "🚗  IRS Mileage Log", "Track every business mile — deduction calculates automatically.", 6)
mil_headers = ["Date", "Order # / Purpose", "From", "To", "Round-trip miles", "Deduction ($)"]
header_row(mil, 4, mil_headers)
MLAST = 254
for r in range(5, MLAST + 1):
    mil.cell(row=r, column=6, value=f"=IF(E{r}=\"\",\"\",E{r}*{RATE})")
    for c in range(1, 7):
        cell = mil.cell(row=r, column=c)
        cell.border = BORDER
        cell.alignment = CENTER
    mil.cell(row=r, column=1).number_format = "yyyy-mm-dd"
    mil.cell(row=r, column=5).number_format = MILES
    mil.cell(row=r, column=6).number_format = CURRENCY
mil_sample = [
    ["2026-01-08", "CS-1042 signing", "Home", "Riverside", 24],
    ["2026-01-11", "ST-9981 signing", "Home", "Downtown", 18],
]
for i, row in enumerate(mil_sample, start=5):
    for c, val in enumerate(row, start=1):
        cell = mil.cell(row=i, column=c, value=val)
        if c == 5:
            cell.number_format = MILES
for c, w in enumerate([12, 26, 16, 16, 16, 14], start=1):
    mil.column_dimensions[get_column_letter(c)].width = w
mil.freeze_panes = "A5"

# === Expenses ==============================================================
exp = wb.create_sheet("Expenses")
banner(exp, "🧾  Expenses & Supplies", "Every deductible dollar, categorized for tax time.", 5)
exp_headers = ["Date", "Category", "Vendor", "Amount", "Deductible?"]
header_row(exp, 4, exp_headers)
ELAST = 204
for r in range(5, ELAST + 1):
    for c in range(1, 6):
        cell = exp.cell(row=r, column=c)
        cell.border = BORDER
        cell.alignment = CENTER
    exp.cell(row=r, column=1).number_format = "yyyy-mm-dd"
    exp.cell(row=r, column=4).number_format = CURRENCY
exp_sample = [
    ["2026-01-03", "E&O Insurance", "NotaryInsure", 75, "Yes"],
    ["2026-01-05", "Supplies", "Amazon", 38.50, "Yes"],
    ["2026-01-09", "Software", "Signing Agent HQ", 19, "Yes"],
    ["2026-01-10", "Printing", "Office Depot", 60, "Yes"],
]
for i, row in enumerate(exp_sample, start=5):
    for c, val in enumerate(row, start=1):
        cell = exp.cell(row=i, column=c, value=val)
        if c == 4:
            cell.number_format = CURRENCY
dv_cat = DataValidation(type="list", formula1=CAT_REF, allow_blank=True)
dv_yn = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
exp.add_data_validation(dv_cat); dv_cat.add(f"B5:B{ELAST}")
exp.add_data_validation(dv_yn); dv_yn.add(f"E5:E{ELAST}")
for c, w in enumerate([12, 20, 18, 14, 14], start=1):
    exp.column_dimensions[get_column_letter(c)].width = w
exp.freeze_panes = "A5"

# === Invoice ===============================================================
inv = wb.create_sheet("Invoice")
banner(inv, "📄  Invoice", "Fill the yellow cells, print to PDF, send.", 5)
inv["A4"] = "From"; inv["A4"].font = BOLD
inv["A5"] = "=Settings!B6"; inv["A6"] = "=Settings!B7"
inv["D4"] = "Invoice #"; inv["D4"].font = BOLD
inv["E4"] = "INV-0001"; inv["E4"].fill = fill(GOLD)
inv["D5"] = "Date"; inv["D5"].font = BOLD
inv["E5"] = "2026-01-31"; inv["E5"].fill = fill(GOLD)
inv["A8"] = "Bill to"; inv["A8"].font = BOLD
inv["B8"] = "Client / Company"; inv["B8"].fill = fill(GOLD)
header_row(inv, 10, ["Description", "Qty", "Rate", "", "Amount"])
for r in range(11, 18):
    inv.cell(row=r, column=2, value=1)
    inv.cell(row=r, column=5, value=f"=IF(C{r}=\"\",\"\",B{r}*C{r})")
    for c in range(1, 6):
        inv.cell(row=r, column=c).border = BORDER
    inv.cell(row=r, column=3).number_format = CURRENCY
    inv.cell(row=r, column=5).number_format = CURRENCY
inv.cell(row=11, column=1, value="Loan signing — Refi")
inv.cell(row=11, column=3, value=150)
inv["D19"] = "TOTAL"; inv["D19"].font = BOLD
inv["E19"] = "=SUM(E11:E17)"; inv["E19"].number_format = CURRENCY
inv["E19"].font = BIG
for c, w in enumerate([28, 8, 12, 4, 14], start=1):
    inv.column_dimensions[get_column_letter(c)].width = w

# === Tax Summary (Schedule C) ==============================================
tax = wb.create_sheet("Tax Summary")
banner(tax, "📊  Tax Summary (Schedule C)", "Hand this to your accountant. Organizer — not tax advice.", 4)
tax["A4"] = "Line item"; tax["B4"] = "Schedule C"; tax["C4"] = "Amount"
for col in "ABC":
    tax[f"{col}4"].fill = fill(TEAL); tax[f"{col}4"].font = HDR
    tax[f"{col}4"].alignment = CENTER; tax[f"{col}4"].border = BORDER
rows = [
    ("Gross income (fees paid)", "Part I, Line 1", '=SUMIF(\'Signing Log\'!H5:H304,"Paid",\'Signing Log\'!G5:G304)'),
    ("Car / mileage deduction", "Line 9", "=SUM('Mileage Log'!F5:F254)"),
    ("Supplies", "Line 22", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Supplies")'),
    ("Insurance (E&O)", "Line 15", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"E&O Insurance")'),
    ("Training / education", "Line 27a", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Training/Education")'),
    ("Phone / internet", "Line 25", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Phone/Internet")'),
    ("Dues / membership (NNA)", "Line 27a", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"NNA Membership")'),
    ("Software", "Line 27a", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Software")'),
    ("Marketing / advertising", "Line 8", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Marketing")'),
    ("Printing", "Line 22", '=SUMIFS(Expenses!D5:D204,Expenses!B5:B204,"Printing")'),
]
for i, (label, sched, formula) in enumerate(rows, start=5):
    tax.cell(row=i, column=1, value=label).border = BORDER
    tax.cell(row=i, column=2, value=sched).border = BORDER
    cell = tax.cell(row=i, column=3, value=formula)
    cell.number_format = CURRENCY; cell.border = BORDER
    tax.cell(row=i, column=2).alignment = CENTER
r_exp = len(rows) + 6
tax.cell(row=r_exp, column=1, value="Total expenses").font = BOLD
tax.cell(row=r_exp, column=3, value=f"=SUM(C6:C{len(rows)+4})").number_format = CURRENCY
tax.cell(row=r_exp, column=3).font = BOLD
tax.cell(row=r_exp + 1, column=1, value="NET PROFIT (est.)").font = BIG
net = tax.cell(row=r_exp + 1, column=3, value=f"=C5-C{r_exp}")
net.number_format = CURRENCY; net.font = BIG
tax.cell(row=r_exp + 3, column=1,
         value="⚠️ This is an organizer, not tax advice. Confirm figures with a tax professional.").font = NOTE
for c, w in enumerate([30, 16, 16], start=1):
    tax.column_dimensions[get_column_letter(c)].width = w

# === Dashboard =============================================================
dash = wb.create_sheet("Dashboard")
banner(dash, "📈  Dashboard", "Your business at a glance.", 8)


def kpi(anchor: str, label: str, formula: str, money: bool = True) -> None:
    col = anchor[0]
    row = int(anchor[1:])
    nextcol = chr(ord(col) + 1)
    dash.merge_cells(f"{col}{row}:{nextcol}{row}")
    lab = dash[f"{col}{row}"]
    lab.value = label; lab.fill = fill(LIGHT); lab.font = BOLD
    lab.alignment = CENTER; lab.border = BORDER
    dash.merge_cells(f"{col}{row+1}:{nextcol}{row+1}")
    val = dash[f"{col}{row+1}"]
    val.value = formula; val.font = BIG; val.alignment = CENTER; val.border = BORDER
    if money:
        val.number_format = CURRENCY
    dash.row_dimensions[row + 1].height = 30


kpi("B4", "Total fees paid", '=SUMIF(\'Signing Log\'!H5:H304,"Paid",\'Signing Log\'!G5:G304)')
kpi("D4", "Outstanding (unpaid)", '=SUMIF(\'Signing Log\'!H5:H304,"Invoiced",\'Signing Log\'!F5:F304)')
kpi("F4", "Net profit (YTD)", '=SUM(\'Signing Log\'!L5:L304)')
kpi("B7", "Signings completed", '=COUNTIF(\'Signing Log\'!H5:H304,"Paid")+COUNTIF(\'Signing Log\'!H5:H304,"Invoiced")+COUNTIF(\'Signing Log\'!H5:H304,"Completed")', money=False)
kpi("D7", "Total miles (YTD)", "=SUM('Mileage Log'!E5:E254)", money=False)
kpi("F7", "Mileage deduction", "=SUM('Mileage Log'!F5:F254)")

# income goal
dash["B11"] = "Annual income goal"; dash["B11"].font = BOLD
dash["D11"] = 40000; dash["D11"].fill = fill(GOLD); dash["D11"].number_format = CURRENCY
dash["B12"] = "Progress to goal"; dash["B12"].font = BOLD
dash["D12"] = '=IF(D11=0,0,SUM(\'Signing Log\'!L5:L304)/D11)'
dash["D12"].number_format = "0%"; dash["D12"].font = BIG

# helper table for charts (net profit by appt type)
dash["B15"] = "Net profit by appointment type"; dash["B15"].font = BOLD
types = ["Refi", "Purchase", "Seller", "HELOC", "Apostille", "RON", "General Notary"]
header_row(dash, 16, ["Appt type", "Net profit"])
for i, t in enumerate(types, start=17):
    dash.cell(row=i, column=1, value=t).border = BORDER
    cell = dash.cell(row=i, column=2,
                     value=f"=SUMIF('Signing Log'!E5:E304,A{i},'Signing Log'!L5:L304)")
    cell.number_format = CURRENCY; cell.border = BORDER

bar = BarChart(); bar.title = "Net profit by appt type"; bar.height = 7; bar.width = 14
data = Reference(dash, min_col=2, min_row=16, max_row=16 + len(types))
cats = Reference(dash, min_col=1, min_row=17, max_row=16 + len(types))
bar.add_data(data, titles_from_data=True); bar.set_categories(cats)
bar.legend = None
dash.add_chart(bar, "D15")

# pie: paid vs outstanding
dash["B26"] = "Cash status"; dash["B26"].font = BOLD
header_row(dash, 27, ["Bucket", "Amount"])
dash.cell(row=28, column=1, value="Paid").border = BORDER
dash.cell(row=28, column=2, value='=SUMIF(\'Signing Log\'!H5:H304,"Paid",\'Signing Log\'!G5:G304)').border = BORDER
dash.cell(row=29, column=1, value="Outstanding").border = BORDER
dash.cell(row=29, column=2, value='=SUMIF(\'Signing Log\'!H5:H304,"Invoiced",\'Signing Log\'!F5:F304)').border = BORDER
for r in (28, 29):
    dash.cell(row=r, column=2).number_format = CURRENCY
pie = PieChart(); pie.title = "Paid vs outstanding"; pie.height = 7; pie.width = 10
pdata = Reference(dash, min_col=2, min_row=27, max_row=29)
plabels = Reference(dash, min_col=1, min_row=28, max_row=29)
pie.add_data(pdata, titles_from_data=True); pie.set_categories(plabels)
dash.add_chart(pie, "D26")

for col, w in {"A": 4, "B": 20, "C": 14, "D": 16, "E": 14, "F": 18, "G": 14}.items():
    dash.column_dimensions[col].width = w

# === START HERE (placed first) =============================================
start = wb.create_sheet("START HERE", 0)
banner(start, "✅  Signing Agent HQ", "The complete notary business & tax system — start here.", 6)
steps = [
    ("1.", "In Google Sheets: File → Make a copy. In Excel: just save your own copy."),
    ("2.", "Open the Settings tab and enter this year's IRS standard mileage rate."),
    ("3.", "Add your title/escrow companies in the Companies tab."),
    ("4.", "Log each job in the Signing Log — Net profit calculates itself."),
    ("5.", "Log drives in the Mileage Log and costs in Expenses as you go."),
    ("6.", "Watch the Dashboard. At tax time, hand the Tax Summary to your accountant."),
]
for i, (n, text) in enumerate(steps, start=4):
    start.cell(row=i, column=1, value=n).font = BOLD
    start.merge_cells(f"B{i}:F{i}")
    cell = start.cell(row=i, column=2, value=text)
    cell.alignment = LEFT
    start.row_dimensions[i].height = 22
start.cell(row=11, column=1,
           value="Tabs: Settings · Companies · Signing Log · Mileage Log · Expenses · Invoice · Tax Summary · Dashboard").font = NOTE
start.cell(row=13, column=1,
           value="⚠️ Disclaimer: this is an organizer, not legal or tax advice. Confirm all figures with a professional.").font = NOTE
start.cell(row=15, column=1, value="© Signing Agent HQ — single-user license. Do not redistribute.").font = NOTE
start.column_dimensions["A"].width = 5
for col in "BCDEF":
    start.column_dimensions[col].width = 20

# hide the lists area visually by widening note (cosmetic only)
sett.sheet_view.showGridLines = True

# ---------------------------------------------------------------------------
os.makedirs("dist", exist_ok=True)
out = "dist/Signing-Agent-HQ.xlsx"
wb.save(out)
print(f"Wrote {out} with sheets: {wb.sheetnames}")
