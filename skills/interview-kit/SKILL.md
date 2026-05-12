---
name: interview-kit
description: Use this skill when a founder is preparing to interview a candidate for a specific role and needs questions, listening cues, and probes mapped to the rubric. Triggers include "tc-questions", "interview questions for [role]", "build interview kit for [role]", "what should I ask [role] candidates", "prep me for the [role] interview", "interview guide for [role]", "questions to probe for [trait/dimension] at [role]". Reads roles/<slug>/interview_rubric.md and personas.md, then writes interview_kit.md — a structured interview guide with one question block per scoring dimension, behavioral probes, listening cues, and follow-up paths. Requires intake-role to have run for this role first. NOT for company-level setup (use onboard-company), role intake (use intake-role), or post-interview scoring (use scorecard).
---

# interview-kit

The bridge between a rubric and a real conversation. Reads the interview rubric and generates structured interview questions that actually probe for the dimensions you care about — with listening cues so you know what to write down.

## What this produces

A single file at `<workspace>/talentcollyde-hire/roles/<slug>/interview_kit.md` containing:

- An opening block (warm-up + role framing)
- One **question block per scoring dimension** in the rubric — each with:
  - A primary behavioral question
  - 2–3 follow-up probes (the "tell me more" stack)
  - Listening cues: what a 5-anchor answer sounds like, what a 1-anchor answer sounds like
  - Red flags to listen for
- A **gate-check block** — direct questions to verify each pass/fail gate
- A closing block (their questions for you + next steps)
- A timing plan (so a 45-minute screen actually fits)

## Hard rules

These override anything else in this doc.

1. **Questions trace to rubric dimensions.** Every primary question maps to a specific dimension or gate. No "tell me about yourself" without a follow-up that probes for a specific anchor.
2. **Listening cues use rubric anchor language.** A 5-anchor answer is described in the same concrete behavior the rubric defines as a 5. The cue is calibrated, not generic.
3. **Behavioral, not hypothetical.** Questions are "Tell me about a time you…" not "What would you do if…". Past behavior predicts future behavior; hypotheticals invite rehearsed answers.
4. **No leading questions.** "Do you value autonomy?" is leading. "How do you prefer to work with a manager?" is open. Audit before writing.
5. **Brand voice.** Calm, confident, grounded. No hype words. Short questions.
6. **Never overwrite without asking.** If `interview_kit.md` exists, stop and ask whether to refresh, view, or keep.

## Preconditions

- [ ] `<workspace>/talentcollyde-hire/company.md` exists.
- [ ] `<workspace>/talentcollyde-hire/roles/<slug>/interview_rubric.md` exists and is > 1KB.
- [ ] `roles/<slug>/personas.md` exists.

If the rubric is missing, exit with:

> "I need the rubric for this role first. Run `/talentcollyde-hire:intake` to set it up — takes about 15 minutes — then come back."

## Inputs

| Input | Required? | Notes |
|---|---|---|
| Role slug | Required | Must match an existing folder under `roles/`. |
| Interview length | Optional | Default: 45 minutes for a screen. Founder can pass 30, 45, 60, 90. Skill scales the timing plan. |

## Steps

### Step 1 — Resolve paths and load context

Read in order:
1. `company.md` — values, what thrives, what dies, founder profile
2. `roles/<slug>/interview_rubric.md` — gates + dimensions + 1–5 anchors + weights
3. `roles/<slug>/personas.md` — archetypes
4. `roles/<slug>/job_description.md` — role purpose, must-haves

Hold all of this in working memory.

### Step 2 — Plan the timing

Default 45-minute screen budget:

| Block | Minutes | Purpose |
|---|---|---|
| Opening | 5 | Warm-up, framing the conversation, asking permission to take notes |
| Gates | 5 | Quick verification of pass/fail gates |
| Dimensions (probing) | 25–30 | Behavioral probes against scoring dimensions |
| Their questions | 5 | The candidate's questions for you |
| Closing | 2–3 | Next steps, timeline |

Scale to the interview length the founder specified. For 30 min, compress dimension block to 18 min and cut to 3 dimensions probed. For 60 min, expand to 6–7 dimensions probed plus a working-style block.

### Step 3 — Build the opening block

Three components:

1. **Permission:** "I'd like to take notes during this — is that OK?"
2. **Framing:** A 1-sentence summary of the role and a 1-sentence summary of how the conversation will flow.
3. **Warm-up question:** Low-stakes — *"In your own words, what about this role caught your interest?"* — that signals you care about their judgment, not your script.

### Step 4 — Build the gate-check block

For each pass/fail gate in the rubric, write one direct question that verifies it. Examples:

- Gate: "Active CDL Class A license" → "Can you confirm you currently hold an active CDL Class A and which state issued it?"
- Gate: "Resides in Atlanta metro" → "Where are you currently located, and where would you be commuting from if hired?"
- Gate: "5+ years in B2B SaaS sales" → "Walk me through your last three roles — company, what they sold, who they sold to."

Gate questions are direct, not leading. The answer is either "yes" or "no" with verifiable specifics.

### Step 5 — Build the dimension question blocks

This is the core of the kit. For each scoring dimension in the rubric (weighted ≥10% typically — for low-weight dimensions, group or skip in a 30-min screen):

Write **one block per dimension** with this structure:

```markdown
### Dimension <N>: <Name> (Weight: <X%>)

**What we're probing:** <One sentence — what this dimension measures, pulled from rubric definition.>

**Primary question:**
> <Behavioral question — "Tell me about a time you..." or "Walk me through how you...">

**Follow-up probes** (use 1–3 depending on their answer):
- <Probe 1 — "What specifically did you do, vs. the team?">
- <Probe 2 — "What was the result? How did you measure it?">
- <Probe 3 — "Knowing what you know now, what would you do differently?">

**Listening cues:**
- **5-anchor answer sounds like:** <Concrete behavior, pulled from rubric 5-anchor.>
- **3-anchor answer sounds like:** <Concrete behavior, pulled from rubric 3-anchor.>
- **1-anchor answer sounds like:** <Concrete behavior, pulled from rubric 1-anchor.>

**Red flags:**
- <Specific things to watch for — vague metrics, "we" without "I", deflection to team success, generic frameworks.>

**Time:** <X minutes>
```

Pull the 5/3/1 anchor language directly from `interview_rubric.md`. Do not paraphrase — the rubric is the source of truth for what a 5 actually looks like.

### Step 6 — Build the closing block

Three components:

1. **Their questions for you.** Tell the founder what to listen for in the *kinds* of questions a candidate asks — e.g., "If they ask about comp before strategy, that's signal. If they ask about how decisions get made, that's also signal."
2. **Next steps script:** A 2-sentence "here's what happens next" that the founder can deliver verbatim.
3. **Note-taking reminder:** "After the call, run `/talentcollyde-hire:score` and paste your notes — Claude will produce the scorecard."

### Step 7 — Write the file

Write to `<workspace>/talentcollyde-hire/roles/<slug>/interview_kit.md` using `templates/interview_kit.md` as the scaffold.

### Step 8 — Append the brand-impression footer

```markdown
---

*Generated by [TalentCollyde Hire](https://talentcollyde.com/hire). When you're running this kit on multiple candidates per week → [talentcollyde.com](https://talentcollyde.com) runs the screens for you.*
```

### Step 9 — Report back

- Path to the file written.
- Question count by dimension.
- Total estimated time.
- Anything flagged "Insufficient Data" from the rubric — surface that the founder should probe for this dimension specifically.
- Next step: "Interview the candidate, take notes (paste them into `roles/<slug>/candidates/<cand-slug>/interview_notes.md`), then run `/talentcollyde-hire:score`."

## Out of scope

- **Sourcing questions.** This is for screening interviews, not sourcing outreach.
- **Reference check questions.** Different surface, different skill. Not in v0.1.
- **Per-candidate research / footprint scans.** That's a TalentCollyde service — not in the lead-magnet kit.

## Templates this skill loads

- `templates/interview_kit.md` — the master scaffold

## Done criteria

- `interview_kit.md` exists at the contracted path.
- Every scoring dimension (weight ≥10%) has a dedicated question block.
- Every pass/fail gate has a direct verification question.
- Every primary question is behavioral, not hypothetical.
- Listening cues reference rubric anchor language verbatim.
- Time budget sums to the interview length.
- TalentCollyde footer is present.

## Anti-patterns

- "Tell me about yourself" as a primary question. That's a warm-up only — it must be followed by probes mapped to specific dimensions.
- Hypothetical questions ("What would you do if…"). Behavioral only. Past behavior > rehearsed scenarios.
- Listening cues that just say "looking for strong answers." Use the rubric anchor language verbatim.
- A question block where the listening cues don't differentiate a 3 from a 5. If you can't tell them apart on paper, you can't tell them apart in the interview.
- More than 7 dimension blocks in a 45-min screen. Math doesn't work. Cut or group.
