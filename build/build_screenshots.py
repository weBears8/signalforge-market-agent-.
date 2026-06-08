#!/usr/bin/env python3
"""
Signing Agent HQ — product screenshots (Pillow).

Branded, realistic "app screenshots" of the actual product, using the verified
sample-quarter numbers (fees $1,385 · net $1,154.40 · miles 343 · deduction
$240.10 · 16 signings). Used in the storefront's screenshots gallery in place
of placeholder boxes.

Outputs (dist/marketing/screenshots/):
  dashboard.png · signing-log.png · tax-summary.png   (1600x1000)
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"
BOLD = f"{FONTS}/BricolageGrotesque-Bold.ttf"
REG = f"{FONTS}/InstrumentSans-Regular.ttf"
SEMI = f"{FONTS}/InstrumentSans-Bold.ttf"

NAVY = (31, 42, 68)
TEAL = (31, 122, 140)
TEAL_T = (224, 238, 240)
GOLD = (224, 164, 88)
GOLD_T = (250, 240, 224)
WHITE = (255, 255, 255)
PAPER = (247, 249, 252)
LINE = (224, 231, 238)
SLATE = (120, 134, 156)
INK = (26, 35, 58)
GREEN = (46, 125, 50)
GREEN_T = (224, 240, 226)
RED = (181, 64, 64)

W, H = 1600, 1000


def font(p, s):
    return ImageFont.truetype(p, s)


def rounded(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def topbar(d, title):
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.ellipse([40, 34, 64, 58], fill=GOLD)
    d.text((78, 32), "Signing Agent HQ", font=font(SEMI, 30), fill=WHITE)
    tw = d.textlength(title, font=font(REG, 26))
    d.text((W - tw - 44, 36), title, font=font(REG, 26), fill=(170, 182, 205))


def base():
    img = Image.new("RGB", (W, H), PAPER)
    return img, ImageDraw.Draw(img)


def save(img, name):
    os.makedirs("dist/marketing/screenshots", exist_ok=True)
    out = f"dist/marketing/screenshots/{name}"
    img.save(out)
    print("Wrote", out)


# ---------------------------------------------------------------- dashboard
def build_dashboard():
    img, d = base()
    topbar(d, "Dashboard")
    kpis = [
        ("Net profit YTD", "$1,154.40", GREEN),
        ("Fees paid", "$1,385.00", TEAL),
        ("Outstanding", "$230.00", GOLD),
        ("Miles YTD", "343", NAVY),
    ]
    pad = 44
    cw = (W - pad * 2 - 3 * 24) // 4
    cy = 132
    ch = 150
    for i, (lab, val, col) in enumerate(kpis):
        x = pad + i * (cw + 24)
        rounded(d, [x, cy, x + cw, cy + ch], 16, WHITE, outline=LINE, width=2)
        d.rectangle([x, cy + 16, x + 8, cy + ch - 16], fill=col)
        d.text((x + 26, cy + 26), lab, font=font(REG, 24), fill=SLATE)
        d.text((x + 26, cy + 64), val, font=font(BOLD, 50), fill=INK)

    # bar chart card: net profit by month
    bx, by = pad, cy + ch + 32
    bw, bh = 880, 430
    rounded(d, [bx, by, bx + bw, by + bh], 16, WHITE, outline=LINE, width=2)
    d.text((bx + 28, by + 22), "Net profit by month", font=font(SEMI, 28), fill=INK)
    months = [("Jan", 0.74), ("Feb", 1.0), ("Mar", 0.32)]  # relative heights
    vals = ["$556", "$559", "$298"]
    inner_x = bx + 60
    base_y = by + bh - 70
    chart_h = bh - 150
    slot = (bw - 120) // len(months)
    for i, ((m, hgt), v) in enumerate(zip(months, vals)):
        cxx = inner_x + i * slot + 30
        bw2 = slot - 90
        top = base_y - int(chart_h * hgt)
        rounded(d, [cxx, top, cxx + bw2, base_y], 8, TEAL if i % 2 == 0 else GOLD)
        d.text((cxx + bw2 / 2 - d.textlength(v, font=font(SEMI, 24)) / 2, top - 34),
               v, font=font(SEMI, 24), fill=INK)
        d.text((cxx + bw2 / 2 - d.textlength(m, font=font(REG, 24)) / 2, base_y + 14),
               m, font=font(REG, 24), fill=SLATE)

    # right column: mileage deduction + income goal
    rx = pad + bw + 24
    rw = W - rx - pad
    rounded(d, [rx, by, rx + rw, by + 150], 16, TEAL, outline=None)
    d.text((rx + 26, by + 26), "Mileage deduction", font=font(REG, 24), fill=(214, 236, 240))
    d.text((rx + 26, by + 62), "$240.10", font=font(BOLD, 56), fill=WHITE)
    d.text((rx + 26, by + 124), "343 mi × $0.70 (IRS)", font=font(REG, 20), fill=(206, 230, 236))

    gy = by + 174
    rounded(d, [rx, gy, rx + rw, by + bh], 16, WHITE, outline=LINE, width=2)
    d.text((rx + 26, gy + 22), "Income goal", font=font(SEMI, 28), fill=INK)
    d.text((rx + 26, gy + 64), "$1,385 of $5,000", font=font(REG, 24), fill=SLATE)
    # progress bar
    pbx, pby = rx + 26, gy + 110
    pbw = rw - 52
    rounded(d, [pbx, pby, pbx + pbw, pby + 30], 15, PAPER, outline=LINE, width=1)
    rounded(d, [pbx, pby, pbx + int(pbw * 0.277), pby + 30], 15, GOLD)
    d.text((rx + 26, gy + 158), "28% — 16 signings logged", font=font(SEMI, 24), fill=TEAL)
    save(img, "dashboard.png")


# --------------------------------------------------------------- signing log
def build_signing_log():
    img, d = base()
    topbar(d, "Signing Log")
    rows = [
        ("Jan 08", "Coastal Signings", "Refi", "$150", "Paid", "$120.20"),
        ("Jan 11", "Summit Title", "Purchase", "$125", "Paid", "$101.40"),
        ("Jan 14", "BlueRock Escrow", "HELOC", "$100", "Invoiced", "-$28.40"),
        ("Jan 16", "Coastal Signings", "Seller", "$150", "Paid", "$137.60"),
        ("Jan 24", "Coastal Signings", "Refi", "$160", "Paid", "$120.90"),
        ("Jan 28", "BlueRock Escrow", "Purchase", "$110", "Paid", "$85.30"),
        ("Feb 02", "Summit Title", "HELOC", "$120", "Paid", "$101.80"),
        ("Feb 09", "BlueRock Escrow", "Refi", "$105", "Paid", "$62.70"),
        ("Feb 18", "Coastal Signings", "Purchase", "$165", "Paid", "$127.40"),
        ("Feb 27", "Summit Title", "Refi", "$135", "Paid", "$99.90"),
    ]
    cols = [("Date", 60), ("Company", 200), ("Appt", 560), ("Fee", 800),
            ("Status", 960), ("Net profit", 1240)]
    ty = 140
    # header
    rounded(d, [44, ty, W - 44, ty + 54], 10, NAVY)
    for name, cx in cols:
        d.text((cx, ty + 14), name, font=font(SEMI, 24), fill=WHITE)
    ry = ty + 54
    rh = 70
    for i, (dt, comp, appt, fee, status, net) in enumerate(rows):
        if i % 2 == 0:
            d.rectangle([44, ry, W - 44, ry + rh], fill=WHITE)
        else:
            d.rectangle([44, ry, W - 44, ry + rh], fill=(243, 246, 250))
        d.line([44, ry + rh, W - 44, ry + rh], fill=LINE, width=1)
        d.text((60, ry + 22), dt, font=font(REG, 24), fill=INK)
        d.text((200, ry + 22), comp, font=font(REG, 24), fill=INK)
        d.text((560, ry + 22), appt, font=font(REG, 24), fill=SLATE)
        d.text((800, ry + 22), fee, font=font(SEMI, 24), fill=INK)
        # status pill
        paid = status == "Paid"
        pill_c = GREEN_T if paid else GOLD_T
        txt_c = GREEN if paid else (170, 120, 40)
        pw = d.textlength(status, font=font(SEMI, 22)) + 36
        rounded(d, [960, ry + 18, 960 + pw, ry + 18 + 34], 17, pill_c)
        d.text((960 + 18, ry + 24), status, font=font(SEMI, 22), fill=txt_c)
        # net profit
        nc = RED if net.startswith("-") else GREEN
        d.text((1240, ry + 22), net, font=font(SEMI, 24), fill=nc)
        ry += rh
    # footer note
    d.text((60, ry + 22), "Net profit per signing = fee paid − mileage − print pages − other.  "
           "Auto-calculated for every row.", font=font(REG, 22), fill=SLATE)
    save(img, "signing-log.png")


# --------------------------------------------------------------- tax summary
def build_tax_summary():
    img, d = base()
    topbar(d, "Tax Summary")
    d.text((44, 124), "Schedule C — ready for your accountant", font=font(SEMI, 30), fill=INK)

    # left: income + expenses breakdown
    lx, ly = 44, 184
    lw, lh = 880, 720
    rounded(d, [lx, ly, lx + lw, ly + lh], 16, WHITE, outline=LINE, width=2)
    d.text((lx + 28, ly + 22), "Expense categories (deductible)", font=font(SEMI, 26), fill=INK)
    cats = [
        ("Car / truck — mileage (343 mi)", "$240.10"),
        ("Training / education", "$120.00"),
        ("Supplies", "$90.50"),
        ("Insurance (E&O)", "$75.00"),
        ("NNA membership / dues", "$65.00"),
        ("Printing", "$60.00"),
        ("Phone / internet (business %)", "$45.00"),
        ("Advertising / marketing", "$30.00"),
        ("Software / subscriptions", "$19.00"),
    ]
    yy = ly + 78
    for name, amt in cats:
        d.text((lx + 28, yy), name, font=font(REG, 24), fill=INK)
        d.text((lx + lw - 28 - d.textlength(amt, font=font(SEMI, 24)), yy),
               amt, font=font(SEMI, 24), fill=INK)
        d.line([lx + 28, yy + 42, lx + lw - 28, yy + 42], fill=LINE, width=1)
        yy += 56
    d.text((lx + 28, yy + 12), "Total deductions", font=font(SEMI, 26), fill=TEAL)
    tot = "$744.60"
    d.text((lx + lw - 28 - d.textlength(tot, font=font(BOLD, 28)), yy + 8),
           tot, font=font(BOLD, 28), fill=TEAL)

    # right: summary figures
    rx = lx + lw + 24
    rw = W - rx - 44
    cards = [
        ("Gross receipts", "$1,385.00", TEAL, WHITE),
        ("Total deductions", "$744.60", GOLD, WHITE),
    ]
    cy = ly
    for lab, val, col, tc in cards:
        rounded(d, [rx, cy, rx + rw, cy + 150], 16, WHITE, outline=LINE, width=2)
        d.rectangle([rx, cy + 16, rx + 8, cy + 134], fill=col)
        d.text((rx + 26, cy + 26), lab, font=font(REG, 24), fill=SLATE)
        d.text((rx + 26, cy + 64), val, font=font(BOLD, 52), fill=INK)
        cy += 174
    # net profit highlight
    rounded(d, [rx, cy, rx + rw, cy + 222], 16, NAVY)
    d.text((rx + 26, cy + 28), "Net profit (Schedule C)", font=font(REG, 26), fill=(180, 195, 218))
    d.text((rx + 26, cy + 74), "$640.40", font=font(BOLD, 84), fill=GOLD)
    d.text((rx + 26, cy + 174), "Gross − deductions, one click.", font=font(REG, 22), fill=(170, 185, 210))
    save(img, "tax-summary.png")


if __name__ == "__main__":
    build_dashboard()
    build_signing_log()
    build_tax_summary()
