---
description: Build the role rubric, JD, and personas from a recorded role intake
argument-hint: "<role title or slug>"
---

Load the `intake-role` skill and follow its instructions for the role in $ARGUMENTS.

Read the role intake transcript at `roles/<role-slug>/.intake/role_intake_transcript.txt`. Produce `job_description.md`, `personas.md`, `interview_rubric.md` (with 1–3 Observations at the top per `references/observations.md`), and `STATUS.md`. Use `company.md` for cross-artifact context. The rubric must have hard pass/fail gates and weighted dimensions with 1.0–5.0 anchors scored to 0.1 precision per `references/hard_rules.md`.
