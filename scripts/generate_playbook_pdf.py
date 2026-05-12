#!/usr/bin/env python3
"""
generate_playbook_pdf.py

Generate the TalentCollyde Hire Quick-Start Playbook PDF — the lead-magnet
walkthrough founders see after downloading the plugin.

Multi-page document format. Same Charcoal/Gold brand palette as the scorecard
so the lead magnet looks like one coherent product.

Dependencies:
  - reportlab  (pip install reportlab --break-system-packages)

Usage:
  python3 generate_playbook_pdf.py --output playbook.pdf
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        BaseDocTemplate,
        Flowable,
        Frame,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
except ImportError:
    sys.stderr.write(
        "ERROR: reportlab is not installed. Install with:\n"
        "  pip install reportlab --break-system-packages\n"
    )
    sys.exit(2)


# --- Brand ------------------------------------------------------------------

CHARCOAL = colors.HexColor("#1a1a2e")
WARM_WHITE = colors.HexColor("#faf9f7")
OFF_WHITE = colors.HexColor("#f0eeeb")
SAND = colors.HexColor("#e8e4df")
GOLD = colors.HexColor("#c9a96e")
TEXT_SECONDARY = colors.HexColor("#5a5a7a")

TC_FOOTER_LINE = (
    "TalentCollyde Hire — founder-grade hiring intelligence · talentcollyde.com"
)


# --- Flowables --------------------------------------------------------------


class HRule(Flowable):
    def __init__(self, width, color, thickness=0.6):
        super().__init__()
        self.width = width
        self.color = color
        self.thickness = thickness
        self.height = thickness

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


class SectionBanner(Flowable):
    """Gold-accented section header."""

    def __init__(self, text, width, height=28, kicker=None):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height
        self.kicker = kicker

    def draw(self):
        c = self.canv
        if self.kicker:
            c.setFillColor(GOLD)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(0, 16, self.kicker.upper())
        c.setFillColor(CHARCOAL)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(0, 0, self.text)
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(0, -4, self.width * 0.18, -4)


class StepNumber(Flowable):
    """Big charcoal step number badge."""

    def __init__(self, n, accent=GOLD):
        super().__init__()
        self.n = n
        self.accent = accent
        self.width = 60
        self.height = 60

    def draw(self):
        c = self.canv
        c.setFillColor(CHARCOAL)
        c.setStrokeColor(self.accent)
        c.setLineWidth(2)
        c.roundRect(0, 0, self.width, self.height, 8, stroke=1, fill=1)
        c.setFillColor(WARM_WHITE)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(self.width / 2, self.height - 15, "STEP")
        c.setFillColor(self.accent)
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(self.width / 2, self.height / 2 - 18, str(self.n))


# --- Styles -----------------------------------------------------------------


def build_styles():
    base = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=CHARCOAL,
        spaceAfter=5,
    )
    body_small = ParagraphStyle("BodySmall", parent=body, fontSize=9, leading=12.5)
    body_secondary = ParagraphStyle(
        "BodySecondary", parent=body, fontSize=9.5, leading=13, textColor=TEXT_SECONDARY
    )
    hero_title = ParagraphStyle(
        "HeroTitle",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=32,
        textColor=CHARCOAL,
        spaceAfter=8,
    )
    hero_sub = ParagraphStyle(
        "HeroSub",
        parent=body,
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=GOLD,
        spaceAfter=14,
    )
    h2 = ParagraphStyle(
        "H2",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=CHARCOAL,
        spaceBefore=8,
        spaceAfter=4,
    )
    h3 = ParagraphStyle(
        "H3",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=CHARCOAL,
        spaceBefore=6,
        spaceAfter=2,
    )
    kicker = ParagraphStyle(
        "Kicker",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=GOLD,
    )
    command = ParagraphStyle(
        "Command",
        parent=body,
        fontName="Courier-Bold",
        fontSize=11,
        leading=14,
        textColor=GOLD,
        backColor=CHARCOAL,
        leftIndent=8,
        rightIndent=8,
        spaceBefore=4,
        spaceAfter=8,
    )
    footer_brand = ParagraphStyle(
        "FooterBrand",
        parent=body,
        fontSize=8,
        leading=10,
        textColor=GOLD,
        fontName="Helvetica-Oblique",
    )
    return {
        "body": body,
        "body_small": body_small,
        "body_secondary": body_secondary,
        "hero_title": hero_title,
        "hero_sub": hero_sub,
        "h2": h2,
        "h3": h3,
        "kicker": kicker,
        "command": command,
        "footer_brand": footer_brand,
    }


# --- Page template ----------------------------------------------------------


def make_page_template(doc_width, doc_height):
    def on_page(canv, doc):
        canv.saveState()
        # Charcoal top strip
        canv.setFillColor(CHARCOAL)
        canv.rect(0, doc_height - 0.35 * inch, doc_width, 0.35 * inch, fill=1, stroke=0)
        # Gold accent line
        canv.setFillColor(GOLD)
        canv.rect(0, doc_height - 0.40 * inch, doc_width, 0.05 * inch, fill=1, stroke=0)
        # Top bar text
        canv.setFillColor(WARM_WHITE)
        canv.setFont("Helvetica-Bold", 10)
        canv.drawString(0.6 * inch, doc_height - 0.25 * inch, "TalentCollyde Hire — Quick-Start Playbook")
        canv.setFont("Helvetica", 9)
        canv.drawRightString(
            doc_width - 0.6 * inch,
            doc_height - 0.25 * inch,
            f"v1.0 · {datetime.now().strftime('%Y-%m-%d')}",
        )
        # Bottom: page number + tagline
        canv.setFont("Helvetica", 8)
        canv.setFillColor(TEXT_SECONDARY)
        canv.drawRightString(doc_width - 0.6 * inch, 0.55 * inch, f"Page {doc.page}")
        canv.drawString(0.6 * inch, 0.55 * inch, "Quietly excellent recruiting.")
        # Brand-impression footer
        canv.setFillColor(GOLD)
        canv.setFont("Helvetica-Oblique", 7.5)
        canv.drawString(0.6 * inch, 0.38 * inch, TC_FOOTER_LINE)
        canv.restoreState()

    frame = Frame(
        0.7 * inch,
        0.75 * inch,
        doc_width - 1.4 * inch,
        doc_height - 1.35 * inch,
        id="main",
        showBoundary=0,
    )
    return PageTemplate(id="main", frames=[frame], onPage=on_page)


# --- Helpers ---------------------------------------------------------------


def p(text, style):
    return Paragraph(text, style)


def bullet_table(items, styles, width):
    rows = []
    for it in items:
        rows.append([p("•", styles["body"]), p(it, styles["body"])])
    tbl = Table(rows, colWidths=[0.2 * inch, width - 0.2 * inch])
    tbl.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return tbl


def step_header(num, title, command, styles, width):
    """Step heading row: number badge + title + command in a tight Table.
    The badge already shows STEP / N — title block has no redundant kicker."""
    title_block = [
        Spacer(1, 6),
        p(title, styles["h2"]),
        p(f'<font face="Courier-Bold" color="#c9a96e">{command}</font>', styles["body_small"]),
    ]
    tbl = Table(
        [[StepNumber(num), title_block]],
        colWidths=[0.9 * inch, width - 0.9 * inch],
    )
    tbl.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    return tbl


# --- Content sections -------------------------------------------------------


def build_hero(styles, width):
    story = [
        Spacer(1, 18),
        p("THE LEAD MAGNET", styles["kicker"]),
        Spacer(1, 4),
        p("TalentCollyde Hire", styles["hero_title"]),
        p("Founder-grade hiring intelligence — set up in 30 minutes.", styles["hero_sub"]),
        HRule(width * 0.4, GOLD, thickness=1.5),
        Spacer(1, 14),
        p(
            "Four skills that turn a vague hiring need into a defensible decision. "
            "The same discipline TalentCollyde runs for our paying clients — "
            "gift-wrapped, free, for you to use on your next hire.",
            styles["body"],
        ),
        Spacer(1, 4),
        p(
            "This playbook gets you to your first scored candidate in about 30 minutes of work, "
            "spread across two sittings. No forms to fill out — you record, Claude listens and structures.",
            styles["body"],
        ),
        Spacer(1, 12),
    ]
    # The 4-step overview table
    overview_rows = [
        [
            p("<b>#</b>", styles["body_small"]),
            p("<b>Skill</b>", styles["body_small"]),
            p("<b>Time</b>", styles["body_small"]),
            p("<b>What you get</b>", styles["body_small"]),
        ],
        [
            p("1", styles["body_small"]),
            p('<font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:onboard</font>', styles["body_small"]),
            p("15 min, once", styles["body_small"]),
            p("Your company DNA file", styles["body_small"]),
        ],
        [
            p("2", styles["body_small"]),
            p('<font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:intake</font>', styles["body_small"]),
            p("15 min per role", styles["body_small"]),
            p("Rubric + JD + personas", styles["body_small"]),
        ],
        [
            p("3", styles["body_small"]),
            p('<font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:questions</font>', styles["body_small"]),
            p("Instant", styles["body_small"]),
            p("Interview kit with listening cues", styles["body_small"]),
        ],
        [
            p("4", styles["body_small"]),
            p('<font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:score</font>', styles["body_small"]),
            p("5 min per candidate", styles["body_small"]),
            p("2-page branded scorecard PDF", styles["body_small"]),
        ],
    ]
    overview = Table(
        overview_rows,
        colWidths=[width * 0.06, width * 0.24, width * 0.22, width * 0.48],
    )
    overview.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (0, 0), (-1, 0), OFF_WHITE),
                ("LINEBELOW", (0, 0), (-1, 0), 0.5, GOLD),
                ("LINEBELOW", (0, 1), (-1, -1), 0.25, SAND),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.append(overview)
    story.append(Spacer(1, 14))
    story.append(
        p(
            "<b>The model:</b> You talk. Claude listens, structures, scores. "
            "Steps 1 and 2 are recordings — Loom, Zoom, your phone's voice memo. "
            "Steps 3 and 4 are automatic.",
            styles["body"],
        )
    )
    return story


def build_step_1(styles, width):
    story = [
        step_header(1, "Onboard your company", "/talentcollyde-hire:onboard", styles, width),
        p(
            "Captures who you are as a company — mission, values, what thrives, what dies, your hiring philosophy. "
            "Everything downstream anchors here. One-time setup.",
            styles["body"],
        ),
        p("How to run it:", styles["h3"]),
        bullet_table(
            [
                'Run <font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:onboard</font>. Claude generates a Founder Interview Guide with 15 questions across 5 blocks.',
                "Record yourself answering them. 25–30 minutes. Loom, Zoom, Granola, your phone's voice memo — anything that produces a transcript.",
                "Drop the transcript at the path Claude tells you (typically <font face=\"Courier\">.intake/onboarding_transcript.txt</font>).",
                'Re-run <font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:onboard</font>. Claude reads the transcript and writes your <font face="Courier">company.md</font>.',
            ],
            styles,
            width,
        ),
        Spacer(1, 6),
        p("What you get:", styles["h3"]),
        p(
            'A quote-anchored <font face="Courier">company.md</font>. Every claim traces to a transcript line. '
            'Sections you didn\'t cover are flagged "Not addressed" — never fabricated.',
            styles["body"],
        ),
        Spacer(1, 4),
        p(
            "<b>Bonus — Observations.</b> Claude detects moments where you flagged uncertainty or named a pattern "
            "(e.g., \"I get caught up in personality\") and surfaces a sharp TalentCollyde take on each one — what the pattern is, "
            "and what specifically the rubric and kit do about it. Quietly excellent — not a half-baked coach.",
            styles["body"],
        ),
    ]
    return story


def build_step_2(styles, width):
    story = [
        step_header(2, "Intake the role", "/talentcollyde-hire:intake", styles, width),
        p(
            "Captures what you actually want in this specific hire — beyond the boilerplate JD. "
            "Produces the rubric every candidate gets scored against. Run once per role.",
            styles["body"],
        ),
        p("How to run it:", styles["h3"]),
        bullet_table(
            [
                'Run <font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:intake</font> and name the role.',
                "Claude generates a Role Intake Guide — 15 questions tailored to this role, informed by your company.md.",
                "Record yourself for 20–25 minutes. Same options as Step 1.",
                "Drop the transcript. Claude builds the rubric.",
            ],
            styles,
            width,
        ),
        Spacer(1, 6),
        p("What you get:", styles["h3"]),
        bullet_table(
            [
                '<font face="Courier">interview_rubric.md</font> — 3–6 pass/fail gates, 5–7 weighted scoring dimensions, 1–5 anchors',
                '<font face="Courier">job_description.md</font> — refined JD, founder-quoted',
                '<font face="Courier">personas.md</font> — 2–4 candidate archetypes',
                '<font face="Courier">STATUS.md</font> — role state, pipeline counts, comp band',
            ],
            styles,
            width,
        ),
        Spacer(1, 4),
        p(
            "Plus more Observations — TalentCollyde's take on the patterns we noticed in your intake.",
            styles["body_secondary"],
        ),
    ]
    return story


def build_step_3(styles, width):
    story = [
        step_header(3, "Generate the interview kit", "/talentcollyde-hire:questions", styles, width),
        p(
            "Reads your rubric. Builds a 45-minute interview screening kit. No founder input required — this step is automatic.",
            styles["body"],
        ),
        p("What you get:", styles["h3"]),
        p('A single file: <font face="Courier">interview_kit.md</font>. Contents:', styles["body"]),
        bullet_table(
            [
                "An opening script (warm-up + permission to take notes)",
                "Gate verification questions — direct, fast",
                "One question block per scoring dimension — primary question + follow-up probes + listening cues calibrated to your rubric's 1, 3, and 5 anchors",
                "Red flags to watch for, by dimension",
                "Anti-bias question order — execution specificity before personality",
                "Closing script you can deliver verbatim",
            ],
            styles,
            width,
        ),
        Spacer(1, 4),
        p(
            "You bring this to the interview. You take notes against it. You decide.",
            styles["body"],
        ),
    ]
    return story


def build_step_4(styles, width):
    story = [
        step_header(4, "Score the candidate", "/talentcollyde-hire:score", styles, width),
        p(
            "Turns raw interview notes into a defensible decision. Run within an hour of the interview while specifics are fresh.",
            styles["body"],
        ),
        p("How to run it:", styles["h3"]),
        bullet_table(
            [
                "Paste your raw interview notes into the candidate's folder (Claude will tell you the exact path).",
                'Run <font face="Courier-Bold" color="#c9a96e">/talentcollyde-hire:score</font>.',
            ],
            styles,
            width,
        ),
        Spacer(1, 4),
        p("What you get:", styles["h3"]),
        bullet_table(
            [
                '<font face="Courier">evidence_brief.md</font> — every dimension cited with direct quotes from your notes (the audit trail)',
                '<font face="Courier">scorecard.md</font> — text version of the scorecard',
                '<font face="Courier">scorecard.pdf</font> — 2-page branded PDF: composite score, recommendation chip, gates, persona match, weighted dimensions, counter-cases',
            ],
            styles,
            width,
        ),
        Spacer(1, 6),
        p("The discipline:", styles["h3"]),
        bullet_table(
            [
                "Scores carry to 0.1 precision. Round numbers (X.0, X.5) require explicit anchor justification.",
                "Insufficient-Data dimensions are flagged and have their weight redistributed — never estimated.",
                "Counter-case sentence on every score. If a candidate's score can't survive the counter-case, the score is wrong.",
            ],
            styles,
            width,
        ),
        Spacer(1, 4),
        p(
            "The PDF is the artifact. Branded in your accent color. Defensible to anyone you share it with.",
            styles["body"],
        ),
    ]
    return story


def build_cta_page(styles, width):
    story = [
        Spacer(1, 24),
        p("THE OFFER", styles["kicker"]),
        Spacer(1, 4),
        p("When the math stops working", styles["h2"]),
        HRule(width * 0.25, GOLD, thickness=1.5),
        Spacer(1, 14),
        p(
            "This kit handles one hire beautifully. Two becomes harder. "
            "<b>Three concurrent roles is where the math typically stops working</b> — sourcing alone eats "
            "15+ hours a week, and this kit doesn't source for you.",
            styles["body"],
        ),
        Spacer(1, 4),
        p("We do.", styles["body"]),
        Spacer(1, 10),
        p("If you hit any of these walls, that's the moment to reach out:", styles["body"]),
        bullet_table(
            [
                "You're hiring 3+ roles concurrently and the time spent running this is competing with your highest-value work.",
                "You don't have time to source — only to interview.",
                "You've made a bad hire and want to understand the pattern across all your past hires (we crystallize that signal across cycles).",
            ],
            styles,
            width,
        ),
        Spacer(1, 14),
        HRule(width, SAND),
        Spacer(1, 8),
        p('<b>Book a 20-min audit:</b> <font color="#c9a96e">talentcollyde.com/audit</font>', styles["body"]),
        p("Until then — use the kit. It's yours.", styles["body"]),
        Spacer(1, 18),
        p('"Quietly excellent recruiting."', styles["footer_brand"]),
    ]
    return story


# --- Main -------------------------------------------------------------------


def build_pdf(output_path):
    page_w, page_h = LETTER
    doc = BaseDocTemplate(
        output_path,
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.7 * inch,
        title="TalentCollyde Hire — Quick-Start Playbook",
        author="TalentCollyde",
    )
    doc.addPageTemplates([make_page_template(page_w, page_h)])
    styles = build_styles()
    content_w = page_w - 1.4 * inch

    story = []
    # Page 1: hero + overview
    story.extend(build_hero(styles, content_w))
    story.append(PageBreak())
    # Page 2: Step 1
    story.extend(build_step_1(styles, content_w))
    story.append(PageBreak())
    # Page 3: Step 2
    story.extend(build_step_2(styles, content_w))
    story.append(PageBreak())
    # Page 4: Step 3
    story.extend(build_step_3(styles, content_w))
    story.append(PageBreak())
    # Page 5: Step 4
    story.extend(build_step_4(styles, content_w))
    story.append(PageBreak())
    # Page 6: CTA
    story.extend(build_cta_page(styles, content_w))

    doc.build(story)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate the TalentCollyde Hire playbook PDF.")
    parser.add_argument(
        "--output",
        default="talentcollyde-hire-playbook.pdf",
        help="Output PDF path",
    )
    args = parser.parse_args(argv)
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    build_pdf(args.output)
    print(f"Wrote playbook to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
