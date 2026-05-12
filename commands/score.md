---
description: Score a candidate from interview notes — produces evidence brief, scorecard, and branded PDF
argument-hint: "<candidate name> for <role>"
---

Load the `scorecard` skill and follow its instructions for the candidate and role in $ARGUMENTS.

Read `roles/<role-slug>/candidates/<candidate-slug>/interview_notes.md`, the `interview_rubric.md`, and `company.md` for cross-artifact context. Produce `evidence_brief.md`, `scorecard.md`, and `scorecard.pdf`. Apply the hard rules from `references/hard_rules.md`: evidence first then score, 0.1 precision (round numbers require anchor justification), IDQ never estimated (redistribute weight pro-rata), gates are gates not dimensions. Include 1–2 Observations on the internal evidence brief per `references/observations.md`; keep them off the client-facing PDF.
