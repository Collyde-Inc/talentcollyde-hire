# Scorecard PDF — Input JSON Schema

This is the JSON the PDF generator (`scripts/generate_scorecard_pdf.py`) expects. The `scorecard` skill builds this from the cached stage outputs and passes it to the script.

## Top-level shape

```json
{
  "candidate": {
    "name": "string (required)",
    "current_title": "string",
    "current_company": "string",
    "current_location": "string"
  },
  "company": "string (required) — the hiring company's name",
  "role": "string (required) — the role title",
  "date": "string (required) — YYYY-MM-DD interview date",
  "overall_score": 4.3,
  "recommendation": "Advance — strong | Advance — qualified | Advance — close call | Hold — re-interview | Pass",
  "stage_1_gates": [
    {
      "gate": "string — gate description",
      "result": "cleared | failed | untested",
      "note": "string — optional context"
    }
  ],
  "stage_2_persona": {
    "primary": "string — persona archetype name",
    "secondary": "string or null"
  },
  "stage_3_dimensions": [
    {
      "name": "string — dimension name",
      "weight": 0.25,
      "score": 4.3,
      "rationale": "string — one line, evidence-anchored",
      "counter_case": "string — one sentence"
    }
  ],
  "idq_note": "string or null — redistribution math if any dimensions are IDQ",
  "evidence_brief_path": "string — relative path to evidence_brief.md (for the provenance footer)",
  "accent_hex": "string — #hex format, optional — falls back to brand Gold #c9a96e"
}
```

## Field notes

- **`overall_score`** carries to 0.1 precision. Computed from the weighted average of per-dimension scores. Never rounded.
- **`stage_3_dimensions[].score`** is either a float to 0.1 or the literal string `"Insufficient Data"`.
- **`stage_3_dimensions[].weight`** is a fraction (0.25 = 25%). The PDF displays it as a percentage.
- **`accent_hex`** is the company's brand accent from `company.md`. If absent or invalid, falls back to `#c9a96e` (TalentCollyde Gold).
- **`recommendation`** is one of the five canonical strings — the PDF renders it as a chip in the accent color.

## What renders where

- **Page 1:** Candidate snapshot + composite score chip + recommendation + Stage 1 gates + Stage 2 persona.
- **Page 2:** Stage 3 dimension table (with score bars in the accent color) + counter-cases + provenance footer + TalentCollyde brand-impression line.
