#!/usr/bin/env python3
"""
Signing Agent HQ — top-of-funnel ad creatives (Pillow).

Three static ads, distinct angles, to seed organic + paid traffic in the
validation phase (notary Facebook groups, Pinterest, IG/FB stories & Reels).
Hooks mirror the three A/B variants in video-script-60s.md.

Outputs (dist/marketing/ads/):
  ad-square-1080.png      1080x1080  Facebook feed / groups (pain -> free log)
  ad-pin-1000x1500.png    1000x1500  Pinterest pin (the free mileage log)
  ad-story-1080x1920.png  1080x1920  IG/FB story & Reel cover (POV hook)

Shares helpers + palette with build_cover.py.
Usage:  python3 build/build_ads.py
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw

from build_cover import (BOLD, GOLD, GREEN, MIST, NAVY, NAVY2, REG, SEMI, SLATE,
                         TEAL, WHITE, center_text, font, mock_dashboard, rounded,
                         vgrad)

ADS_DIR = "dist/marketing/ads"


def check(d, cx, cy, r=20, color=GREEN):
    """A filled circle with a white check mark."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    d.line([(cx - r * 0.42, cy + r * 0.02),
            (cx - r * 0.08, cy + r * 0.38),
            (cx + r * 0.46, cy - r * 0.36)],
           fill=WHITE, width=max(3, r // 5), joint="curve")


def pill(d, cx, cy, text, f, bg=GOLD, fg=NAVY, pad=46, h=92):
    """Centered rounded pill sized to its text. Returns its width."""
    tw = d.textlength(text, font=f)
    w = tw + pad * 2
    x0 = cx - w / 2
    rounded(d, [x0, cy, x0 + w, cy + h], h // 2, bg)
    d.text((x0 + pad, cy + (h - f.size) / 2 - 4), text, font=f, fill=fg)
    return w


def bullets_block(d, cx, top, items, f, gap=78, rdot=19):
    """Green-check bullets, left-aligned as a centered block."""
    widths = [d.textlength(t, font=f) for t in items]
    block_w = rdot * 2 + 26 + max(widths)
    x = cx - block_w / 2
    y = top
    for t in items:
        check(d, x + rdot, y + f.size / 2, rdot)
        d.text((x + rdot * 2 + 26, y), t, font=f, fill=WHITE)
        y += gap


def paper_mock(width, height):
    """A white 'printable' sheet mock for the free mileage log."""
    img = Image.new("RGB", (width, height), (250, 251, 253))
    d = ImageDraw.Draw(img)
    # navy title bar
    d.rectangle([0, 0, width, 70], fill=NAVY)
    d.text((24, 22), "The Notary Mileage Log", font=font(SEMI, 30), fill=WHITE)
    # rate chip
    rounded(d, [width - 250, 90, width - 24, 142], 14, GOLD)
    d.text((width - 232, 102), "IRS rate: $0.70", font=font(SEMI, 24), fill=NAVY)
    d.text((24, 100), "Date   Purpose / Order #", font=font(SEMI, 24), fill=SLATE)
    d.text((width - 360, 100), "Miles", font=font(SEMI, 24), fill=SLATE)
    # header underline
    d.line([(24, 160), (width - 24, 160)], fill=(220, 226, 234), width=2)
    rows = [("1/08", "CS-1042 — Refi", "24", "$16.80"),
            ("1/11", "ST-9981 — Purchase", "18", "$12.60"),
            ("1/16", "CS-1051 — Seller", "12", "$8.40"),
            ("1/21", "BR-204 — HELOC", "32", "$22.40"),
            ("1/26", "AN-5611 — Refi", "9", "$6.30")]
    y = 178
    for dte, purp, mi, ded in rows:
        d.text((24, y), dte, font=font(REG, 24), fill=NAVY)
        d.text((110, y), purp, font=font(REG, 24), fill=NAVY)
        d.text((width - 360, y), mi, font=font(REG, 24), fill=NAVY)
        d.text((width - 200, y), ded, font=font(SEMI, 24), fill=TEAL)
        y += 50
    # totals
    d.line([(24, y + 6), (width - 24, y + 6)], fill=(220, 226, 234), width=2)
    d.text((110, y + 18), "TOTAL deduction (YTD)", font=font(SEMI, 26), fill=NAVY)
    d.text((width - 210, y + 18), "$66.50", font=font(BOLD, 28), fill=GREEN)
    return img


# ---------------------------------------------------------------------------
def ad_square():
    W = H = 1080
    img = vgrad((W, H), NAVY, NAVY2).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GOLD)

    center_text(d, W / 2, 72, "MOBILE NOTARIES & SIGNING AGENTS", font(SEMI, 30), GOLD)
    center_text(d, W / 2, 150, "Stop losing money", font(BOLD, 92), WHITE)
    center_text(d, W / 2, 248, "at tax time.", font(BOLD, 92), WHITE)
    center_text(d, W / 2, 384, "Run your whole notary business from one sheet.",
                font(REG, 36), MIST)

    bullets_block(d, W / 2, 480,
                  ["Net profit per signing",
                   "IRS mileage that does the math",
                   "1-click, tax-ready Schedule C"],
                  font(SEMI, 40), gap=86)

    pill(d, W / 2, 800, "Comment  MILE  for the free log", font(BOLD, 38))
    center_text(d, W / 2, 922, "Free IRS mileage log · no subscription", font(REG, 30), SLATE)

    d.rectangle([0, H - 76, W, H], fill=GOLD)
    center_text(d, W / 2, H - 58, "Signing Agent HQ", font(SEMI, 36), NAVY)

    _save(img, "ad-square-1080.png")


def ad_pin():
    W, H = 1000, 1500
    img = vgrad((W, H), NAVY, NAVY2).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=GOLD)

    center_text(d, W / 2, 70, "FREE FOR NOTARIES", font(SEMI, 32), GOLD)
    center_text(d, W / 2, 140, "The Notary", font(BOLD, 104), WHITE)
    center_text(d, W / 2, 250, "Mileage Log", font(BOLD, 104), WHITE)
    center_text(d, W / 2, 392, "Never miss a deductible mile again.", font(REG, 40), MIST)

    # printable mock
    mw, mh = 820, 560
    mx = (W - mw) // 2
    my = 470
    rounded(d, [mx - 6, my - 6, mx + mw + 6, my + mh + 6], 20, (16, 23, 40))
    img.paste(paper_mock(mw, mh), (mx, my))
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=16, outline=GOLD, width=4)

    center_text(d, W / 2, 1100, "Log a trip in 10 seconds —", font(REG, 38), MIST)
    center_text(d, W / 2, 1150, "your tax deduction adds up automatically.", font(REG, 38), MIST)

    pill(d, W / 2, 1268, "Grab it free  →", font(BOLD, 44), h=104, pad=56)
    d.rectangle([0, H - 70, W, H], fill=GOLD)
    center_text(d, W / 2, H - 54, "Signing Agent HQ · Sheets + Notion", font(SEMI, 30), NAVY)

    _save(img, "ad-pin-1000x1500.png")


def ad_story():
    W, H = 1080, 1920
    img = vgrad((W, H), NAVY, NAVY2).convert("RGB")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 12, H], fill=GOLD)

    # content kept within story-safe area (y ~ 240..1680)
    center_text(d, W / 2, 250, "MOBILE NOTARIES", font(SEMI, 32), GOLD)
    center_text(d, W / 2, 322, "POV: it's tax season", font(BOLD, 82), WHITE)
    center_text(d, W / 2, 416, "and your notary books", font(BOLD, 82), WHITE)
    center_text(d, W / 2, 510, "are a mess.", font(BOLD, 82), WHITE)

    center_text(d, W / 2, 648, "Here's the fix.", font(REG, 44), MIST)

    # product mock
    mw, mh = 900, 660
    mx = (W - mw) // 2
    my = 730
    rounded(d, [mx - 6, my - 6, mx + mw + 6, my + mh + 6], 22, (16, 23, 40))
    img.paste(mock_dashboard(mw, mh), (mx, my))
    d.rounded_rectangle([mx, my, mx + mw, my + mh], radius=18, outline=GOLD, width=4)

    bullets_block(d, W / 2, 1480,
                  ["Net profit per signing",
                   "IRS mileage, auto-calculated",
                   "1-click Schedule C summary"],
                  font(SEMI, 40), gap=84)

    pill(d, W / 2, 1772, "Free mileage log — link in bio", font(BOLD, 38))

    _save(img, "ad-story-1080x1920.png")


def _save(img, name):
    os.makedirs(ADS_DIR, exist_ok=True)
    path = os.path.join(ADS_DIR, name)
    img.save(path)
    print("Wrote", path)


if __name__ == "__main__":
    ad_square()
    ad_pin()
    ad_story()
