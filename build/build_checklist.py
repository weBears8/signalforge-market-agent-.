#!/usr/bin/env python3
"""
Signing Agent HQ — bundle bonus generator.

Builds the "First 90 Days Launch Checklist" — the new-agent magnet promised
by the landing page, sales listing and product spec (module 9). A branded,
printable, actually-checkable PDF that takes a brand-new notary from
commission to their first 10 signings, wired to the Signing Agent HQ system.

Output:
  dist/bundle/First-90-Days-Launch-Checklist.pdf

Usage:  python3 build/build_checklist.py
"""

from __future__ import annotations

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle)

NAVY = colors.HexColor("#1F2A44")
TEAL = colors.HexColor("#1F7A8C")
GOLD = colors.HexColor("#E0A458")
GREY = colors.HexColor("#566173")
LINE = colors.HexColor("#C7D0DA")

CONTENT_W = LETTER[0] - 1.4 * inch  # matches L/R margins below

styles = getSampleStyleSheet()
H_TITLE = ParagraphStyle("ct", parent=styles["Title"], fontSize=25, textColor=NAVY,
                         leading=28, spaceAfter=2, alignment=TA_LEFT)
SUB = ParagraphStyle("cs", parent=styles["Normal"], fontSize=12.5, textColor=TEAL,
                     spaceAfter=10)
INTRO = ParagraphStyle("ci", parent=styles["Normal"], fontSize=10.5, textColor=GREY,
                       leading=15, spaceAfter=4)
SECTION = ParagraphStyle("sec", parent=styles["Heading2"], fontSize=14, textColor=NAVY,
                         spaceBefore=14, spaceAfter=2)
ITEM = ParagraphStyle("it", parent=styles["Normal"], fontSize=10.5, textColor=colors.HexColor("#222b3a"),
                      leading=14)
NOTE = ParagraphStyle("nt", parent=styles["Normal"], fontSize=8.5, textColor=GREY,
                      leading=12, spaceBefore=4)
UP = ParagraphStyle("up", parent=styles["Normal"], fontSize=10.5, textColor=NAVY,
                    leading=14)


def rule():
    return HRFlowable(width="100%", thickness=1.2, color=GOLD, spaceBefore=4, spaceAfter=8)


def check_item(text):
    """A single checklist row: a drawn checkbox + the item text."""
    box_w = 15
    t = Table([["", Paragraph(text, ITEM)]], colWidths=[box_w, CONTENT_W - box_w])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (0, 0), 0.9, NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        # shrink the checkbox cell to a ~11pt square at the top of the row
        ("TOPPADDING", (0, 0), (0, 0), 1),
        ("BOTTOMPADDING", (0, 0), (0, 0), 11),
    ]))
    return t


def section(story, heading, items):
    story.append(Paragraph(heading, SECTION))
    story.append(rule())
    for it in items:
        story.append(check_item(it))


def build():
    story = [
        Paragraph("First 90 Days — Notary Launch Checklist", H_TITLE),
        Paragraph("From commission to your first 10 signings.", SUB),
        Paragraph("Work top to bottom. Check a box as you finish each step — and set up "
                  "<b>Signing Agent HQ</b> early so your income, miles and taxes track "
                  "themselves from day one.", INTRO),
        Spacer(1, 4),
    ]

    section(story, "Week 1 — Get legally set up", [
        "Apply for your notary commission with your state (pass the exam if required).",
        "Order your notary stamp and a bonded journal.",
        "Buy Errors &amp; Omissions (E&amp;O) insurance — $25k–$100k coverage is typical.",
        "Complete the NNA background screening.",
        "Separate your money: a dedicated business account or payment method.",
        "Set up Signing Agent HQ and enter this year's IRS standard mileage rate in Settings.",
    ])

    section(story, "Weeks 2–4 — Become a loan signing agent", [
        "Take a signing agent certification course (e.g. NNA or Loan Signing System).",
        "Pass the signing agent exam and certified background check.",
        "Get a dual-tray laser printer that handles letter <i>and</i> legal paper.",
        "Create profiles on the signing databases: Snapdocs, SigningOrder, BNC, etc.",
        "Set your service area, availability, and base fees per appointment type.",
        "Add your first title/escrow companies to the Companies tab.",
        "Order business cards and set up a free Google Business profile.",
    ])

    section(story, "Months 2–3 — Land your first 10 signings", [
        "Apply to 15–20 signing services and title companies.",
        "Accept your first signings — log each one in the Signing Log as you go.",
        "Record every business mile the same day in the Mileage Log.",
        "Ask every happy client and company for a review or star rating.",
        "Follow up weekly with the companies that pay best and fastest.",
        "Check your Dashboard: net profit per job — stop accepting the money-losers.",
        "Set aside taxes and reconcile your Tax Summary monthly, not in April.",
    ])

    story += [
        Spacer(1, 10),
        HRFlowable(width="100%", thickness=0.8, color=LINE, spaceAfter=8),
        Paragraph("This is an organizer and general guidance, not legal or tax advice. "
                  "Requirements vary by state — confirm yours with the appropriate authority.",
                  NOTE),
        Spacer(1, 6),
        Paragraph("<b>Run all of this from one place.</b> Signing Agent HQ turns this "
                  "checklist into a working business: signing CRM, net profit per job, "
                  "IRS mileage log, invoices, and a one-click Schedule&nbsp;C tax summary. "
                  "&rarr; Get it at founder price <b>$19</b>.", UP),
    ]

    os.makedirs("dist/bundle", exist_ok=True)
    out = "dist/bundle/First-90-Days-Launch-Checklist.pdf"
    doc = SimpleDocTemplate(out, pagesize=LETTER, topMargin=0.7 * inch,
                            bottomMargin=0.6 * inch, leftMargin=0.7 * inch,
                            rightMargin=0.7 * inch,
                            title="First 90 Days — Notary Launch Checklist")
    doc.build(story)
    print("Wrote", out)


if __name__ == "__main__":
    build()
