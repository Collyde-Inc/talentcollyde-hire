# Observations — TalentCollyde Pattern Spec

The master spec for how `onboard-company`, `intake-role`, and `scorecard` detect founder signal in transcripts and interview notes — and how they surface a TalentCollyde-flavored observation in the synthesized output.

This is the load-bearing differentiator. Generic rubric tools structure information. This plugin reads the founder's transcript like a senior recruiter would, names what it heard in one diagnostic line, and points to the kit's response. The Observations pattern is how.

This file replaces the earlier `coaching_notes.md` spec. The naming change is intentional: a plugin that reads one transcript cannot *be* a coach. It can be a sharp observer that heard the founder clearly and responded with action. That's the honest job, and it's a better moat than the deeper consulting pose — reliability compounds.

---

## What an Observation is

An Observation is **a moment in the founder's recording (or interview notes) where they signaled uncertainty, named a pattern about themselves, or asked for help — and the plugin responded with a sharp diagnostic line and a specific kit action.**

Observations are NOT:
- Generic advice the founder could get from any AI
- Restatement of what the founder said
- Padding to look smart
- Hedge framings like "you might consider…" or "perhaps the rubric should…"
- Formal consulting deliverables — the plugin reads one transcript; it can't be a coach
- Multi-section essays. If an observation runs past ~150 words, it's drifting into consulting prose.

Observations ARE:
- A pointer to a quote in the transcript (with timestamp), not the full quote restated
- One named pattern with one opinionated diagnostic sentence
- One follow-up sentence that makes the diagnosis concrete
- A short two-clause action line — *In the rubric / In the kit* — that names exactly how the kit responds

---

## Detection — when to emit an Observation

Scan the transcript / interview notes for any of these patterns. If found, emit an Observation.

### Tier 1 — Explicit asks

The founder directly asks for help. High-confidence triggers:

- *"I need help with [X]"*
- *"How do I [X]?"*
- *"Give me the grief"*
- *"I'm getting hung up on [X]"*
- *"That's where I struggle"*
- *"I'm not sure how to [X]"*

### Tier 2 — Self-doubt / pattern naming

The founder names a failure mode or bias about themselves:

- *"I always get caught up in [X]"*
- *"I tend to ignore [X]"*
- *"I over-index on [X]"*
- *"I'm not great at [X]"*
- *"I talk myself past [X]"*
- *"My gut tells me [X] but I should probably [Y]"*

### Tier 3 — Hesitation / skipped topic

The founder rushes past or avoids a topic the skill specifically prompted on. Examples:
- A one-sentence answer to a 5-min block
- Explicit *"I don't really have an answer for that"* and move on
- Contradicts themselves between two blocks without acknowledging it

### Tier 4 — Cross-artifact conflict

For `intake-role` and `scorecard`: when the founder's stated role priorities or candidate notes conflict with what's in `company.md`. Examples:
- `company.md` says "I over-index on enthusiasm" → role intake says "I want someone with high energy" without acknowledging the bias
- `company.md` says "we value bias to action" → role description says the candidate needs to "wait for direction" — surface the contradiction

### Detection discipline

- **Quality over quantity.** Aim for 1–3 Observations per skill run. False positives erode trust faster than missed signals build it.
- **Trigger must be unambiguous.** If you're not sure the founder said something observation-worthy, don't emit. The bar is "if a senior recruiter heard this on a call, they'd write it down."
- **Quote pointer, not full quote.** Reference the timestamp(s). The transcript already has the quote — don't duplicate it in full inside the Observation. A short fragment in the title is fine.

---

## Structure — the 2-paragraph template

Every Observation follows this shape. No deviations.

```markdown
### Observation <N> — "<Short pattern name, in the founder's words if possible>"

You named this <once / twice / three times> in the recording (Transcript [<timestamp>] <and [<timestamp>]>). <One opinionated diagnostic sentence — names the pattern beneath the quote. Takes a position.> <One follow-up sentence — names the probe that breaks the pattern, or makes the diagnosis concrete with a specific failure-mode example.>

*In the rubric:* <Specific dimension weight, gate, or anchor that responds.> *In the kit:* <Specific question, listening cue, or scenario that responds.>
```

For `onboard-company` Observations, where downstream rubric/kit doesn't exist yet, use:

```markdown
*In the next intake:* <Specific commitment about how `/talentcollyde-hire:intake` will respond when the founder runs it for their first role.>
```

### Voice rules

**Diagnostic paragraph:**
- Start with the timestamp pointer — "*You named this twice (T[10:37] and T[12:26])…*"
- One opinionated diagnostic sentence. *"The signal you're looking for is X"* — not *"you might want X."*
- One follow-up sentence — the probe that breaks the pattern, or a concrete failure mode the founder may not have seen.
- Length cap: 4 sentences total in the paragraph. Past that, it's drifting toward consulting prose.
- Brand voice: calm, confident, grounded. Quietly excellent. Never loud.
- If the founder is wrong, say so. Gently, but clearly: *"That instinct is the failure mode, not the safeguard."*

**Action line:**
- Italicized, single line.
- Two parts separated by a period: *In the rubric:* and *In the kit:*
- One short clause each. Name the specific weight, gate, anchor, dimension, question, or scenario.
- This is the commitment that converts the Observation from a tip into action.
- If only one applies, use that one — don't pad.

---

## Where Observations go

| Skill | Placement | Visibility |
|---|---|---|
| `onboard-company` | Top of `company.md`, after the metadata header, before Section 1 (The company) | High — first thing the founder reads after the header |
| `intake-role` | Top of `interview_rubric.md`, after the hard-rules line, before Layer 1 (Gates) | High — founders read the rubric most often |
| `scorecard` | Top of `evidence_brief.md` (internal); brief mention only in `scorecard.md` (human-readable summary); **NOT on the client-facing PDF** | Internal only — observations are for the founder, not the client |

The section header in every artifact:

```markdown
## Observations from TalentCollyde
```

The structure is the same in every skill so founders recognize the format across the kit.

---

## Brand-impression close — every Observations section

Every block of Observations ends with one quietly-branded line. Single line. Never loud:

```markdown
*Observations from your intake — how TalentCollyde shows up across your kit. When you want us running the hire instead — [talentcollyde.com](https://talentcollyde.com).*
```

This is non-negotiable. The Observations section is the highest brand-impression real estate in the whole kit.

---

## Anti-patterns (skill rejects and re-runs if any apply)

- **Generic advice.** *"Consider focusing on cultural fit."* No. Either point to a specific founder quote and respond to it specifically, or don't emit.
- **Restating the founder in full.** The transcript has the quote. The Observation points to it; it doesn't duplicate it.
- **Hedge language.** *"You might want to think about…"*, *"It could be worth considering…"*, *"Perhaps the rubric should…"* The whole point is taking a position. Hedge phrasing kills the value.
- **Formal 4-part scaffolding.** Don't bring back "You said / Why / Take / What kit does" headers. The 2-paragraph form does the same work without consulting-deliverable bloat.
- **Emitting 4+ Observations.** Quality over quantity. 1–3 per skill run. If the trigger isn't unambiguous, skip it.
- **Observations longer than ~150 words.** That's the half-baked-coach zone. Compress or cut.
- **Missing the action line.** Every Observation ends with *In the rubric / In the kit.* That commitment is the conversion mechanism.
- **Missing the brand-impression close.** Every block of Observations ends with the TalentCollyde close line. Non-negotiable.
- **Observations on the client-facing scorecard PDF.** Internal only. The PDF is for the candidate's hiring committee — observations are for the founder.

---

## Why this pattern is the moat

Generic rubric tools structure information. Anyone can build that.
This plugin reads the founder's transcript like a senior recruiter would, names what it heard in one sharp line, and points to the kit's response. That's harder — and it compounds.

Every Observation is a brand impression. Every brand impression is a step toward the founder calling TalentCollyde when their hiring volume passes the threshold where running this themselves stops making sense.

The math: a founder who runs this kit on 3 hires sees ~6–9 Observations across the lifecycle. Each one is a short, specific demonstration of craft. By the time they hit the wall on Role #4, the brand has compounded.

This is the conversion engine. Treat the Observations pattern as load-bearing — and keep it tight. The discipline of staying short is what keeps it sharp.
