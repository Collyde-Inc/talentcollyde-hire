---
name: intake-role
description: Use this skill when a founder wants to define a specific role they're hiring for. Triggers include "intake a role", "tc-intake", "I want to hire a [role]", "define the [role] role", "set up the rubric for [role]", "intake the [role]", "what should I look for in a [role]", "build the JD for [role]". Three modes — generate a role intake guide for the founder to record (or be interviewed) against, synthesize a recorded transcript into the four role artifacts, or run a chat fallback when no recording is available. Skill auto-detects mode from folder state. Writes job_description, personas, interview_rubric, STATUS to roles/<role-slug>/. Requires onboard-company to have run first (reads company.md as foundation). NOT for company-level work (use onboard-company), interview question generation (use interview-kit), or candidate scoring (use scorecard).
---

# intake-role

Per-role scaffolding. Captures what the founder is actually looking for in this hire — beyond the boilerplate JD — and produces the rubric every downstream skill scores against.

## Why transcript-first

A founder talking through what they want in a role gives more signal than the same founder typing terse answers to a form. They hesitate on the dealbreakers. They tell stories about the last hire who failed at the role. They contradict themselves between Q3 and Q9 — and the contradiction is the most useful thing in the file. Typed answers get edited; recorded answers are honest. Exec-search firms always interview the hiring manager; this skill works the same way.

## Three modes — auto-detected

| Mode | When | What happens |
|---|---|---|
| **A — Generate guide** | First invocation for this role. No role folder. No transcript at the contracted path. | Skill writes `roles/<slug>/role_intake_guide.md` and exits. Founder records (solo or with a teammate as interviewer). Drops transcript at the contracted path. Re-invokes this skill. |
| **B — Synthesize from transcript** | Transcript exists at `roles/<slug>/.intake/role_intake_transcript.txt` (or `.md`, `.vtt`) and is > 1KB. | Skill reads the transcript, maps content to the four role artifacts (STATUS, JD, personas, rubric), writes them. |
| **C — Chat fallback** | Founder explicitly opts in. | Skill drives the 15-question intake live in chat. Lower fidelity — use only if recording isn't possible. |

## Phase routing

1. Read the user's request (role title required).
2. Resolve slug. Check workspace state for the role:
   - Role artifacts (job_description.md, interview_rubric.md, etc.) already exist with content → ask before doing anything else.
   - Transcript exists at `.intake/role_intake_transcript.txt`, > 1KB → run **Mode B**.
   - Role folder doesn't exist or only has the guide → ask the founder which mode (A or C). Recommend A.
3. If the founder says they want C ("chat now", "can't record"), confirm once and proceed.
4. Never run multiple modes in one invocation.

## Hard rules

These override anything else in this doc.

1. **Founder intent overrides JDs.** If the corporate JD says one thing and the founder said another in the intake recording, the founder wins. Cite the founder + transcript timestamp.
2. **Pass/fail gates are gates, not scored dimensions.** Once a candidate clears a gate, they don't lose points for it elsewhere.
3. **Insufficient Data — never estimate.** If the founder didn't surface signal for a rubric dimension, mark it "Insufficient Data — calibrate after first interview." Do not invent.
4. **No fabrication.** Every persona, weight, and gate traces to a founder quote (transcript timestamp), a company.md value, or an explicit JD line.
5. **Transcript fidelity (Mode B specific).** Every claim in the role artifacts traces to a transcript line or timestamp. If a line is paraphrased, mark it `(paraphrased — see line X)`. Do not pull from external context the founder didn't speak to.
6. **Brand voice.** Calm, confident, grounded. Customer-as-hero. Short sentences. No hype.
7. **Never overwrite without asking.** If role artifacts exist with content, stop and ask.

## Preconditions

The skill runs these checks at the start. Any fail = stop and report.

- [ ] `<workspace>/talentcollyde-hire/company.md` exists with > 1KB of content (run `/talentcollyde-hire:onboard` first if not).
- [ ] Role slug doesn't collide with an existing `roles/<slug>/`. If it does, append MMYY suffix (e.g., `recruiter-0526`) or ask.

If `company.md` is missing, exit with:

> "I need your company DNA first. Run `/talentcollyde-hire:onboard` to set that up, then come back."

## Workspace structure (after Mode B or C runs)

```
<workspace>/talentcollyde-hire/roles/<slug>/
├── STATUS.md
├── job_description.md
├── personas.md
├── interview_rubric.md
├── role_intake_guide.md          # written by Mode A
├── .intake/
│   └── role_intake_transcript.txt  # founder drops transcript here for Mode B
└── candidates/                    # populated later by scorecard
```

## Inputs

| Input | Required? | Notes |
|---|---|---|
| Role title | Required | Converted to kebab-case slug (e.g., "Head of Sales" → `head-of-sales`). |
| Founder mode choice | Required at first invocation only | Skill recommends A if state is ambiguous. |
| Transcript (Mode B) | Required for Mode B | Dropped at the contracted path. Skill auto-detects. |
| Raw JD (optional) | Optional | Path or pasted text. Used as scaffolding — founder quotes override. |

---

## Mode A — Generate the role intake guide

### A.1 Resolve role slug

Convert role title to kebab-case, lowercase, ASCII. Strip filler words. Examples:
- "Recruiter" → `recruiter`
- "Head of Sales" → `head-of-sales`
- "VP, Operations (East)" → `vp-operations-east`

Collision check: if `roles/<slug>/` exists, ask whether to append MMYY suffix or abort.

### A.2 Load company context

Read `company.md`. Hold the founder's values, what-thrives, what-dies, hiring philosophy, and founder profile in working memory. The guide questions get *lightly* customized with this context — e.g., a question can reference a specific value the founder named.

### A.3 Ask the founder which mode

Show all three options. Recommend A. Use this exact framing (or close to it):

> "Three ways to set this up for the <Role Title> role:
> **A. Record yourself.** I generate a role intake guide tailored to this role — 15 questions across 5 blocks, ~20-25 minutes of recording. You record yourself answering, drop the transcript, re-run this skill, and I'll write the rubric, JD, personas, and STATUS.
> **B. Have a teammate interview you.** Same guide, but a teammate runs the conversation. Same transcript drop.
> **C. Chat through it now.** I drive the 15-question intake right here in chat. Faster, lower fidelity.
> Recommend A. Which one?"

### A.4 If A or B — write the guide

Create the role folder structure:

```
roles/<slug>/
└── .intake/   (empty, ready for transcript)
```

Write `roles/<slug>/role_intake_guide.md` using `templates/role_intake_guide.md` as the scaffold. Customize:
- Role title in the header
- A reference to the founder's #1 hiring tell from `company.md` (Block 4 framing)
- A reference to the "what dies here" pattern from `company.md` (Block 3 framing)
- The contracted transcript drop path

### A.5 Exit with instructions

Tell the founder:

> "Role intake guide written to `<workspace>/talentcollyde-hire/roles/<slug>/role_intake_guide.md`.
> Three steps when you're ready:
> 1. Open the guide. Skim the 5 blocks.
> 2. Record yourself (or your teammate interviewing you) talking through it. Aim for 20-25 min.
> 3. Drop the transcript at `roles/<slug>/.intake/role_intake_transcript.txt` and re-invoke `/talentcollyde-hire:intake` for the <Role> role. I'll synthesize the four role artifacts."

Don't proceed further. The skill ends here for Mode A.

### A.6 If C — proceed to Mode C (chat fallback)

---

## Mode B — Synthesize from transcript

### B.1 Resolve transcript path

Auto-detect. Accept any of:
- `roles/<slug>/.intake/role_intake_transcript.txt`
- `roles/<slug>/.intake/role_intake_transcript.md`
- `roles/<slug>/.intake/role_intake_transcript.vtt`

If the transcript is < 1KB, exit: *"Transcript too short to synthesize — drop a fuller recording (~15-25 min) and re-invoke."*

### B.2 Read the transcript + company context

Load:
1. `company.md` — values, what thrives, what dies, founder profile
2. The role intake transcript

Identify speakers, rough length, and which blocks the founder covered vs. skipped.

### B.3 Map to the four role artifacts — by theme, not by question order

A founder talking about why they're hiring this role might cover "what success looks like" in the same breath as "must-haves." Pull content wherever it lives in the transcript.

### B.4 Cross-reference with company.md

Before writing:
- Does the role's required profile align with `company.md` → `what thrives here`? If there's a value conflict, surface it: "You said Collyde runs on bias-to-action, but this role description sounds like it needs heavy oversight. Which is true for this hire?"
- Does the founder's signal for this role align with the founder profile? E.g., if `company.md` said the founder over-indexes on enthusiasm, the rubric should explicitly weight execution-verification dimensions.

Don't smooth over conflicts. Surface them in `intake_notes` (or inline in the relevant artifact).

### B.4.5 Observations pass — the load-bearing brand-impression step

Before writing the four artifacts, scan the intake transcript for founder signal per the master spec in `references/observations.md`. Detection tiers:

- **Tier 1 — Explicit asks:** *"I need help with…"*, *"give me the grief"*, *"how do I ask good questions for [X]"*, *"I'm getting hung up on…"*
- **Tier 2 — Self-doubt patterns:** *"I always get caught up in…"*, *"I over-index on…"*, *"I talk myself past…"*, *"My gut says X but I should probably Y"*
- **Tier 3 — Hesitation / skipped topics** the skill prompted on but the founder rushed past
- **Tier 4 — Cross-artifact conflict with `company.md`:** when the role intake conflicts with the founder's stated company values, surface it

Emit 1–3 Observations per the 2-paragraph template (diagnostic paragraph + italicized action line). Each Observation ends with a concrete *In the rubric:* / *In the kit:* commitment.

**Voice:** opinionated, specific, no hedge phrasing. Pull on recruiting craft. Keep under ~150 words per Observation. No formal 4-part scaffolding.

**Where they go:** at the top of `interview_rubric.md`, after the hard-rules line, before Layer 1 (Gates). Section header: `## Observations from TalentCollyde`. End the block with the brand-impression close line (see master spec).

### B.5 Write the four artifacts

Write in this order, each using its template:

1. **`STATUS.md`** — opening date, target close, location, comp band, reports to. All pipeline counts = 0.
2. **`job_description.md`** — refined JD pulling from transcript. Source-tag every must-have with `— Founder, Intake YYYY-MM-DD, transcript line/timestamp`.
3. **`personas.md`** — 2-4 archetypes the founder named or implied. Quote-back per persona.
4. **`interview_rubric.md`** — Layer 1: pass/fail gates (3-6). Layer 2: weighted scoring dimensions (5-7, weights sum to 100%). Every gate and dimension traces to a transcript quote.

Sections without signal get "Insufficient Data — calibrate after first interview," not invented content.

### B.6 Confirm with the founder

Show the founder a summary:
- Role slug used
- Pass/fail gates list (sanity-check before interviews)
- Rubric dimensions + weights (sanity-check weighting)
- Anything marked "Insufficient Data"
- Tensions with company.md that need a call (if any)

Iterate once if asked. Then commit.

### B.7 Volume CTA check

Count existing folders under `roles/`. If this is role #3 or more:

> "**You've now intaked 3 roles.** Founders typically hit this volume when growth is accelerating — and running this process for each one starts eating real hours. If you want a 20-minute audit of your hiring stack and where TalentCollyde can take the heavy lift, book here: [talentcollyde.com/audit](https://talentcollyde.com/audit)"

### B.8 Report back

- Role slug
- Files written
- Gates + rubric summary
- IDQ dimensions (if any)
- Next step: "Run `/talentcollyde-hire:questions` for the <role> role — it'll read this rubric and generate the interview kit."

---

## Mode C — Chat fallback

Drives the 15-question intake live. Lower fidelity than Mode B — but lets the founder try the kit immediately when recording isn't possible.

### C.1 Confirm the mode

> "OK — chat mode for <Role>. 15 questions across 5 blocks. One at a time. When done, I'll write the four role artifacts. Ready?"

### C.2 Run the 15 questions

One at a time. Adapt — if a founder's answer to Q3 covers Q4, fold and move on.

**Block 1 — Why this hire** (2 Q)
1. "What problem does this hire solve? Be specific — what's broken right now?"
2. "If you don't fill this role in 90 days, what breaks?"

**Block 2 — What success looks like** (3 Q)
3. "Day 30 — what should this person be doing? What does a good first week look like?"
4. "Month 6 — what's different about the business because they're here?"
5. "Month 12 — what does this person own end-to-end?"

**Block 3 — Profile and must-haves** (4 Q)
6. "Describe the ideal person — not the resume, the human. Background, energy, motivators."
7. "2-3 must-have credentials or experiences. The non-negotiables."
8. "2-3 dealbreakers. Things you'd reject for even if everything else looked great."
9. "Any past hires — yours or someone else's — that come to mind as the model? Or the anti-pattern?"

**Block 4 — How you'll know** (3 Q)
10. "The *one signal* in an interview that would tell you this is the right person."
11. "The *one signal* that would tell you to walk away."
12. "Behaviors or stories you want to probe for? E.g., 'I want to hear how they handle a missed quarter.'"

**Block 5 — Comp, location, logistics** (3 Q)
13. "Comp band — low and high, plus structure (base / variable / equity)."
14. "Location — remote, hybrid, in-office? If hybrid/in-office, which city?"
15. "Reports to whom, manages whom?"

### C.3 Observations pass

Same detection + structure as B.4.5. In chat mode, the timestamp pointer becomes "Chat exchange Q<N>." Emit 1–3 Observations per the master spec.

### C.4 Synthesize and write the four artifacts

Same as B.5. Founder-quoted where possible. Insert Observations section at the top of `interview_rubric.md`.

### C.5 Confirm, CTA check, report back

Same as B.6-B.8.

---

## Templates and references this skill loads

- `templates/role_intake_guide.md` — Mode A guide scaffold
- `templates/role_status.md` — STATUS scaffold
- `templates/job_description.md` — JD scaffold
- `templates/personas.md` — personas scaffold
- `templates/interview_rubric.md` — rubric scaffold
- `references/observations.md` (at plugin root) — Observations detection + structure + voice rules

## Done criteria

A run of this skill is "done" when **one** of the following is true:

**Mode A done:**
- `role_intake_guide.md` exists with all 5 blocks + recording instructions + transcript drop path.
- Skill exited with the clear next-step message.

**Mode B or C done:**
- All 4 role artifacts exist at the contracted paths.
- No `{{TOKEN}}`, no `TBD`, no `[fill in]`.
- Every must-have, gate, and rubric dimension traces to a transcript quote or company.md line.
- **Observations section at the top of `interview_rubric.md`** with 1–3 Observations following the 2-paragraph template per `references/observations.md`, plus the brand-impression close line.
- Sections without signal are marked "Insufficient Data."
- Weights sum to 100%.
- Gates and dimensions are distinct.
- Volume CTA fires if this is role 3+.

## Anti-patterns

- Defaulting to chat without offering the recording path. Mode A is the recommended path — present it first.
- Inventing answers from external context (LinkedIn, the company website) in Mode B. Transcript fidelity — quote what the founder said, flag what they didn't.
- "Strong communicator" as a pass/fail gate. That's a scored dimension.
- A 5-dimension rubric with one fabricated dimension. Hard rule 3 — IDQ + redistribute.
- Weights clustered at 14-16%. Signal that the rubric isn't reflecting founder emphasis.
- Persona reading like a marketing page. Press for the *specific person* the founder named in the recording.
- Skipping the company.md cross-reference. The role intake against the company DNA is what catches the conflicts that break hires later.
