#!/usr/bin/env python3
"""
Signing Agent HQ — marketing cover/thumbnail generator (Pillow).

Outputs:
  dist/marketing/cover-2000.png    Etsy square thumbnail 2000x2000
  dist/marketing/hero-1600x900.png Wide hero for Gumroad/Shopify/social

Brand palette: navy #1F2A44, teal #1F7A8C, gold #E0A458.
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw, ImageFont

FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"
BOLD = f"{FONTS}/BricolageGrotesque-Bold.ttf"
REG = f"{FONTS}/InstrumentSans-Regular.ttf"
SEMI = f"{FONTS}/InstrumentSans-Bold.ttf"

NAVY = (31, 42, 68)
NAVY2 = (26, 35, 58)
TEAL = (31, 122, 140)
GOLD = (224, 164, 88)
WHITE = (255, 255, 255)
MIST = (224, 232, 240)
GREEN = (95, 197, 123)
SLATE = (140, 152, 170)
CARD = (40, 52, 80)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def center_text(d, cx, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text((cx - w / 2, y), text, font=f, fill=fill)
    return w


def rounded(d, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def vgrad(size, top, bottom):
    """Vertical gradient background."""
    w, h = size
    base = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(h - 1, 1)
        base.putpixel((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return base.resize((w, h))


def mock_dashboard(width, height):
    """A small mock of the product dashboard to show 'real product'."""
    img = Image.new("RGB", (width, height), (247, 249, 252))
    d = ImageDraw.Draw(img)
    # top bar
    d.rectangle([0, 0, width, int(height * 0.13)], fill=NAVY)
    d.text((24, int(height * 0.04)), "Signing Agent HQ — Dashboard",
           font=font(SEMI, max(14, height // 26)), fill=WHITE)
    # KPI cards
    labels = [("Fees paid", "$12,450", TEAL), ("Net profit", "$9,180", GREEN),
              ("Miles (YTD)", "3,240", GOLD)]
    pad = 24
    cw = (width - pad * 4) // 3
    cy = int(height * 0.17)
    ch = int(height * 0.28)
    for i, (lab, val, col) in enumerate(labels):
        x = pad + i * (cw + pad)
        rounded(d, [x, cy, x + cw, cy + ch], 14, (255, 255, 255), outline=(225, 231, 238), width=2)
        d.rectangle([x, cy, x + 8, cy + ch], fill=col)
        d.text((x + 22, cy + 16), lab, font=font(REG, max(12, height // 34)), fill=SLATE)
        d.text((x + 22, cy + ch // 2 - 2), val, font=font(BOLD, max(20, height // 18)), fill=NAVY)
    # bar chart
    bx, by = pad, cy + ch + pad
    bw, bh = width - pad * 2, int(height * 0.40)
    rounded(d, [bx, by, bx + bw, by + bh], 14, (255, 255, 255), outline=(225, 231, 238), width=2)
    d.text((bx + 18, by + 12), "Net profit by appt type",
           font=font(SEMI, max(12, height // 34)), fill=NAVY)
    bars = [0.55, 0.8, 0.45, 0.65, 0.3, 0.5, 0.7]
    cols = [TEAL, GOLD, TEAL, GOLD, TEAL, GOLD, TEAL]
    n = len(bars)
    inner_x = bx + 28
    inner_w = bw - 56
    base_y = by + bh - 26
    slot = inner_w // n
    for i, (v, c) in enumerate(zip(bars, cols)):
        bxx = inner_x + i * slot + 10
        top = base_y - int((bh - 70) * v)
        rounded(d, [bxx, top, bxx + slot - 24, base_y], 6, c)
    return img


# ---------------------------------------------------------------------------
def build_square():
    W = H = 2000
    img = vgrad((W, H), NAVY, NAVY2).convert("RGB")
    d = ImageDraw.Draw(img)

    # top accent line
    d.rectangle([0, 0, W, 14], fill=GOLD)

    # eyebrow
    center_text(d, W / 2, 150, "GOOGLE SHEETS  +  NOTION  ·  ONE-TIME", font(SEMI, 46), GOLD)

    # title
    center_text(d, W / 2, 250, "Signing Agent HQ", font(BOLD, 150), WHITE)

    # subtitle (two lines)
    center_text(d, W / 2, 440, "The complete notary business", font(REG, 70), MIST)
    center_text(d, W / 2, 525, "& tax system", font(REG, 70), MIST)

    # dashboard mock card
    mock = mock_dashboard(1500, 760)
    mx = (W - 1500) // 2
    my = 680
    # shadow
    rounded(d, [mx - 6, my - 6, mx + 1500 + 6, my + 760 + 6], 22, (18, 25, 42))
    img.paste(mock, (mx, my))
    d.rounded_rectangle([mx, my, mx + 1500, my + 760], radius=18, outline=GOLD, width=4)

    # benefit chips
    chips = ["Net profit per signing", "IRS mileage auto-calc", "1-click Schedule C"]
    cy = 1560
    fchip = font(SEMI, 44)
    gap = 40
    widths = [d.textlength(c, font=fchip) + 80 for c in chips]
    total = sum(widths) + gap * (len(chips) - 1)
    x = (W - total) / 2
    for c, w in zip(chips, widths):
        rounded(d, [x, cy, x + w, cy + 86], 43, TEAL)
        d.text((x + 40, cy + 18), c, font=fchip, fill=WHITE)
        x += w + gap

    # bottom strip
    d.rectangle([0, H - 120, W, H], fill=GOLD)
    center_text(d, W / 2, H - 92, "Track every signing · capture every mile · walk into tax season ready",
                font(SEMI, 40), NAVY)

    os.makedirs("dist/marketing", exist_ok=True)
    img.save("dist/marketing/cover-2000.png")
    print("Wrote dist/marketing/cover-2000.png")


def build_hero():
    W, H = 1600, 900
    img = vgrad((W, H), NAVY, NAVY2).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=GOLD)

    # --- left text column lives in x = 90 .. 790 (card starts at 840) ---
    d.text((90, 120), "GOOGLE SHEETS + NOTION · NO SUBSCRIPTION",
           font=font(SEMI, 26), fill=GOLD)
    d.text((86, 168), "Signing", font=font(BOLD, 96), fill=WHITE)
    d.text((86, 272), "Agent HQ", font=font(BOLD, 96), fill=WHITE)

    d.text((90, 408), "Run your whole notary", font=font(REG, 44), fill=MIST)
    d.text((90, 460), "business from one sheet.", font=font(REG, 44), fill=MIST)

    bullets = ["Net profit per signing, auto",
               "IRS mileage log does the math",
               "1-click, tax-ready Schedule C"]
    by = 560
    fb = font(REG, 36)
    for b in bullets:
        d.ellipse([92, by + 12, 110, by + 30], fill=GREEN)
        d.text((128, by), b, font=fb, fill=WHITE)
        by += 60

    # CTA — pill auto-sized to the text, navy text on gold
    cta = "Founder price — $19"
    fc = font(BOLD, 38)
    tw = d.textlength(cta, font=fc)
    px0, py0 = 90, 772
    pill_w = tw + 80
    rounded(d, [px0, py0, px0 + pill_w, py0 + 78], 39, GOLD)
    d.text((px0 + 40, py0 + 18), cta, font=fc, fill=NAVY)

    # --- mock dashboard on the right (x = 840 .. 1540) ---
    mock = mock_dashboard(700, 520)
    img.paste(mock, (840, 190))
    d.rounded_rectangle([840, 190, 1540, 710], radius=16, outline=GOLD, width=4)

    os.makedirs("dist/marketing", exist_ok=True)
    img.save("dist/marketing/hero-1600x900.png")
    print("Wrote dist/marketing/hero-1600x900.png")


if __name__ == "__main__":
    build_square()
    build_hero()
