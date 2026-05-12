---
name: onboard-company
description: Use this skill the first time a founder runs talentcollyde-hire — before any role intake. Triggers include "onboard my company", "set up TalentCollyde Hire", "tc-onboard", "let's start hiring", "I want to hire", "set up hiring", "build my company DNA", "describe my company". Three modes — generate a founder interview guide for the founder to record (or be interviewed) against, synthesize a recorded transcript into company.md, or run a chat fallback when no recording is available. Skill auto-detects mode from folder state. Every downstream skill (intake-role, interview-kit, scorecard) reads company.md as foundation. NOT for per-role work (use intake-role) or candidate scoring (use scorecard).
---

# onboard-company

The foundation skill. Captures *who you are as a company* so every downstream rubric, persona, and scorecard is anchored in the same context — not invented from scratch each time.

## Why transcript-first

Talking out loud for 25 minutes gives ~10x the signal of typing terse answers to a form. Founders hesitate on what matters. They correct themselves mid-sentence. They emphasize without realizing. Typed answers get edited; recorded answers are honest. Exec-search firms always interview — they never survey. This skill works the same way.

## Three modes — auto-detected

| Mode | When | What happens |
|---|---|---|
| **A — Generate guide** | First invocation. No `company.md`. No transcript at the contracted path. | Skill writes `founder_interview_guide.md` and exits. Founder records (solo or with a teammate as interviewer). Drops transcript at the contracted path. Re-invokes this skill. |
| **B — Synthesize from transcript** | Transcript exists at `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt` (or `.md`, `.vtt`) and is > 1KB. | Skill reads the transcript, maps content to the seven `company.md` sections, writes `company.md`. |
| **C — Chat fallback** | Founder explicitly opts in (says "do this in chat", "I can't record right now", "let's just talk it through"). | Skill drives the 15-question intake live, conversation-style. Lower fidelity — only use if record-and-paste isn't possible. |

## Phase routing

1. Read the user's request.
2. Check the workspace state:
   - `company.md` already exists with content → ask before doing anything else (refresh, view, or skip).
   - Transcript exists at `.intake/onboarding_transcript.txt` (or `.md`, `.vtt`), > 1KB → run **Mode B**.
   - Otherwise → ask the founder which mode (A or C). Recommend A.
3. If the founder says they want C ("chat now", "can't record"), confirm once and proceed.
4. Never run multiple modes in one invocation.

## Hard rules

These override anything else in this doc.

1. **No fabrication.** If the founder didn't address a topic, the section reads "Not addressed — recommend a follow-up." Do not invent values, culture markers, or founder profile details. Do not pull from external context (LinkedIn, website) that the founder didn't speak to.
2. **Quote the founder back to themselves.** Use their exact phrases where possible. Direct quotes carry more weight than paraphrase.
3. **Transcript fidelity (Mode B specific).** Every claim in `company.md` traces to a transcript line or timestamp. If a line is heavily paraphrased, mark it `(paraphrased — see line X)`.
4. **Brand voice.** Calm, confident, grounded. No hype words. Short sentences. Customer-as-hero.
5. **Never overwrite without asking.** If `company.md` already exists with content, stop and ask.
6. **No `{{TOKEN}}` placeholders.** Write content directly. Sections without signal are explicitly flagged.

## Workspace structure

```
<workspace>/talentcollyde-hire/
├── company.md                       # final output, written by Mode B or C
├── founder_interview_guide.md       # written by Mode A, used by founder, never overwritten in Mode B/C
├── .intake/
│   └── onboarding_transcript.txt    # founder drops the transcript here for Mode B
└── roles/                           # empty for now — intake-role populates
```

## Inputs

| Input | Required? | Notes |
|---|---|---|
| Workspace folder | Required | Where to create `talentcollyde-hire/`. If running inside a folder the user selected via Cowork, use that. Otherwise ask once with a default of `./talentcollyde-hire/`. |
| Founder choice (Mode A vs C) | Required at first invocation only | Skill asks once if state is ambiguous. Recommends A. |
| Transcript file (Mode B) | Required for Mode B | Dropped by founder at `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt`. Skill auto-detects. |

---

## Mode A — Generate the founder interview guide

### A.1 Resolve workspace path

If the user has selected a folder, use that. Otherwise ask once:
> "Where should I set up your hiring workspace? Default is `./talentcollyde-hire/` in the current folder."

Create:
```
<workspace>/talentcollyde-hire/
└── .intake/   (empty — for the transcript to land in later)
```

### A.2 Ask the founder which mode

Show all three options. Recommend A. Use this exact framing (or close to it):

> "Three ways to set this up:
> **A. Record yourself.** I'll generate a founder interview guide — 15 questions across 5 blocks, ~25-30 minutes of recording. You hit record (Loom, Zoom, Granola, even your phone's voice memo), talk through the questions like you're explaining your company to a smart friend. Drop the transcript here when done, re-run this skill, and I'll write your `company.md`.
> **B. Have a teammate interview you.** Same guide, but a teammate runs the conversation as an interviewer. Same 25-30 min, recorded on Zoom or similar. Same transcript drop.
> **C. Chat through it now.** I drive a 15-question intake right here in chat. Faster, lower fidelity — typed answers get edited, talked answers are honest. Use this if recording isn't an option.
> Recommend A. Which one?"

### A.3 If A or B — write the guide

Write `founder_interview_guide.md` using `templates/founder_interview_guide.md` as the scaffold. The guide is mode-agnostic — it works for self-record and teammate-interview without rewrites, just with a small mode toggle at the top.

### A.4 Exit with instructions

Tell the founder:

> "Guide written to `<workspace>/talentcollyde-hire/founder_interview_guide.md`.
> Three steps when you're ready:
> 1. Open the guide. Skim the 5 blocks.
> 2. Record yourself (or your teammate interviewing you) talking through it. Aim for 25–30 min.
> 3. Drop the transcript at `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt` and re-invoke `/talentcollyde-hire:onboard`. I'll synthesize the recording into your `company.md`."

Don't proceed further. The skill ends here for Mode A.

### A.5 If C — proceed to Mode C (chat fallback)

---

## Mode B — Synthesize from transcript

### B.1 Resolve transcript path

Auto-detect. Accept any of:
- `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt`
- `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.md`
- `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.vtt`

If multiple exist, use the most recent. If none exist, route to Mode A.

### B.2 Read the transcript

Read the whole file into working memory. Identify:
- Speakers (one founder, or founder + interviewer)
- Rough length (word count, estimated minutes)
- Sections the founder addressed vs. skipped

If the transcript is < 1KB, exit: *"Transcript is too short to synthesize — drop a fuller recording (~25–30 min) and re-invoke."*

### B.3 Map to the seven company.md sections

For each section of `templates/company.md`, scan the transcript for relevant content. **By theme, not by question order.** A founder talking about their values might do it in block 2 of the guide — or they might wander into it in block 4. Pull the content wherever it lives.

The seven sections:

1. **The company** — what they do, who pays them, what stage.
2. **Mission and values** — the deeper why + 3–5 values with a concrete moment per value.
3. **What thrives here** — the kind of person who succeeds.
4. **What dies here** — the kind of person who doesn't make it.
5. **Hiring philosophy** — speed vs. fit, sourcing posture, decision-making.
6. **Founder profile** — their tells for a good hire, what they've ignored on a bad one, candidate experience standard.
7. **Brand & accent** — their accent color hex if mentioned, otherwise default Gold.

### B.4 Quote-back synthesis

Write each section by quoting the founder directly where possible. Tag each block with the timestamp or line reference from the transcript:

```markdown
### Value 1 — Speed without compromise
> "We won't slow down for politeness, but we won't lower the bar either." — Transcript line 47

**Moment it was real:** <Founder's concrete example, quoted.>
```

For sections where the founder didn't address the topic:

```markdown
### What dies here

*Not addressed in this conversation — recommend a follow-up. Knowing what kind of person doesn't make it at <Company> is the highest-signal input for downstream rubrics. Worth a 10-minute focused recording before running `/talentcollyde-hire:intake` on your first role.*
```

Don't paper over. Honesty about gaps is what makes the file trustworthy.

### B.5 Observations pass — the load-bearing brand-impression step

Before writing `company.md`, scan the transcript for founder signal per the master spec in `references/observations.md`. Detection tiers:

- **Tier 1 — Explicit asks:** *"I need help with…"*, *"how do I…"*, *"give me the grief"*, *"I'm getting hung up on…"*
- **Tier 2 — Self-doubt patterns:** *"I always get caught up in…"*, *"I tend to ignore…"*, *"I over-index on…"*, *"I talk myself past…"*
- **Tier 3 — Hesitation / skipped topics** the skill specifically prompted on but the founder rushed past or avoided

Emit 1–3 Observations. Quality over quantity. Each follows the 2-paragraph template per `references/observations.md`:

- **Diagnostic paragraph** — timestamp pointer, one opinionated diagnostic sentence, one follow-up sentence that names the probe or makes the diagnosis concrete. Cap at 4 sentences total.
- **Action line** — italicized, single line: *In the rubric:* / *In the kit:* (or, for onboarding when no role exists yet, *In the next intake:*).

**Voice:** calm, confident, grounded. Take a position — no hedge phrasing. No hype words. No formal 4-part scaffolding ("You said / Why / Take / What kit does" headers). Keep it under ~150 words per Observation.

**Where they go:** at the top of `company.md`, right after the metadata header, before Section 1 (The company). Section header: `## Observations from TalentCollyde`. End the block with the brand-impression close (single line, see master spec).

### B.6 Write `company.md`

Use `templates/company.md` as the scaffold. Replace each section with synthesized content. Insert the Observations section (from B.5) at the top. No `{{TOKEN}}`. Append the TalentCollyde brand-impression footer.

### B.7 Confirm with the founder

Show the founder the file (or a summary by section). Ask:

> "Two things to check:
> 1. The 'what dies here' section — does it read true? That's the one founders usually want to refine.
> 2. Anything marked 'Not addressed' — want to record a 5-min follow-up to fill those gaps, or move on?"

Iterate once if asked. Then commit.

### B.8 Report back

- Path to the file written.
- Brand accent captured.
- Sections marked "Not addressed" (with the follow-up recommendation).
- Next step: "When you're ready to hire a specific role, run `/talentcollyde-hire:intake`."

---

## Mode C — Chat fallback

Drives the 15-question intake live. Lower fidelity than Mode B — typed answers get edited and lose tone — but lets the founder try the kit immediately when recording isn't possible.

### C.1 Confirm the mode

> "OK — chat mode. I'll ask 15 questions across 5 blocks. One at a time. Keep answers short — bullet points are fine. When we're done, I'll write your `company.md`. Ready?"

### C.2 Run the 15 questions

Same 15 questions as in `templates/founder_interview_guide.md` (Mode A guide). One at a time. Adapt — if a founder's answer to Q3 covers Q4, fold and move on.

**Block 1 — The company** (2 questions)
1. "In plain language, what does your company do — and who pays you for it?"
2. "What stage are you at? Pre-revenue, finding fit, scaling, profitable?"

**Block 2 — Mission and values** (3 questions)
3. "What's the underlying problem you're trying to solve in the world? Not the product — the deeper why."
4. "What are 3–5 values that actually shape how you operate? Not aspirational — the ones you'd fire someone over."
5. For each value: "Give me one moment — a hire, a fire, a decision — that made that value real."

**Block 3 — What thrives / what dies** (2 questions)
6. "Describe the last person who absolutely thrived on your team. What made them work here?"
7. "Describe someone who didn't make it — even if talented. What about them didn't fit?"

**Block 4 — Hiring philosophy** (3 questions)
8. "When you hire, what matters more — speed or fit? Be honest about the tradeoff you actually make."
9. "Do you tend to hire from your network, or cast wide? What's your gut on that approach?"
10. "Who's involved in the decision — just you, a co-founder, the team?"

**Block 5 — Founder profile + brand** (5 questions)
11. "When you've made a great hire, what tipped you to 'yes'?"
12. "When you've made a bad hire, what did you ignore?"
13. "How do you want candidates to feel after they interview with you — even the ones you don't hire?"
14. "What's your brand's primary accent color? (Hex if you know it; otherwise describe it.)"
15. "Anything else about your company I should know before I start writing role rubrics?"

### C.3 Observations pass

Same detection + structure as B.5. Even in chat mode, the founder will surface observation triggers — *"I'm not sure how to…"*, *"I always get caught up in…"*. Emit 1–3 Observations per the master spec in `references/observations.md`.

In chat mode, the timestamp pointer becomes "Chat exchange Q<N>" — reference which question prompted the founder's answer rather than a recording timestamp.

### C.4 Synthesize and write `company.md`

Same as B.5–B.6. Quote founder back to themselves. Insert Observations section at the top. No fabrication.

### C.5 Confirm and report back

Same as B.7–B.8.

---

## Templates and references this skill loads

- `templates/company.md` — the final output scaffold (used by Modes B and C)
- `templates/founder_interview_guide.md` — the recording guide (written by Mode A)
- `references/observations.md` (at plugin root) — Observations detection + structure + voice rules

## Done criteria

A run of this skill is "done" when **one** of the following is true:

**Mode A done:**
- `founder_interview_guide.md` exists at the contracted path with all 5 blocks + recording instructions + transcript drop instructions.
- Skill exited with the clear next-step message.

**Mode B or C done:**
- `company.md` exists at the contracted path.
- All seven sections are populated OR explicitly flagged "Not addressed."
- No `{{TOKEN}}`, no `TBD`, no `[fill in]`.
- Every value has a concrete moment behind it (not aspirational text).
- **Observations section is present at the top** with 1–3 Observations following the 2-paragraph template per `references/observations.md`, plus the brand-impression close line.
- Brand accent is set (or noted as "use default Gold #c9a96e").
- TalentCollyde brand-impression footer is present.
- Founder has confirmed the "what dies here" section reads true.

If any of these fail, the skill is wrong — fix the skill, not the output.

## Anti-patterns (flag and fix)

- Defaulting to chat mode without offering the recording path. Mode A is the recommended path — present it first.
- Inventing answers from the founder's external context (LinkedIn, website) in Mode B. Transcript fidelity — quote what they said, flag what they didn't.
- Values written like a marketing page ("Excellence. Integrity. Innovation."). Always pull the *moment* behind each — that's the signal.
- "What dies here" section soft-pedaled because the founder got uncomfortable. That section is the highest-signal one — don't soften, ask again next round.
- Overwriting an existing `company.md` without asking. Hard rule 5.
- Mode B run on a transcript < 1KB. Too thin to synthesize honestly — reroute to Mode A or C.
