# TalentCollyde Hire

**Founder-grade hiring intelligence. Free, open source, gift from TalentCollyde.**

Four skills that turn a vague hiring need into a defensible decision — so the next person you hire doesn't have to be a coin flip.

---

## What this is

A Claude Code plugin that walks you through the same four steps senior recruiters use, in order. Type `/talentcollyde-hire:start` first — it's a conversational welcome that figures out where you are and tells you what to run next.

| Step | Skill | What it produces |
|---|---|---|
| 0 | `/talentcollyde-hire:start` | A first-run welcome. Conversational only, no file writes. Tells you what to run first based on your current workspace state. |
| 1 | `/talentcollyde-hire:onboard` | A `company.md` that captures your mission, values, and how you actually hire — synthesized from a 25-minute recording of you (or a teammate interviewing you). |
| 2 | `/talentcollyde-hire:intake` | A real intake on a specific role: refined JD, candidate personas, a weighted **interview rubric** with pass/fail gates and 1–5 scoring anchors. |
| 3 | `/talentcollyde-hire:questions` | An **interview kit** of questions and listening cues mapped to your rubric. So you stop asking "tell me about yourself" and start probing for the signal you actually need. |
| 4 | `/talentcollyde-hire:score` | A **two-page candidate scorecard PDF** — branded, evidence-backed, scored to 0.1 precision — generated after you interview someone. |

**The model: you record, Claude synthesizes.** Onboarding and role intake are recorded conversations (Loom, Zoom, Granola, even a phone voice memo). Founders talk in stories; typed answers get edited and lose tone. Drop the transcript at the contracted path and Claude maps it to the right artifacts. A chat fallback is available if recording isn't an option, but it's a lower-fidelity path.

## What it's not

Not a sourcing tool. Not a candidate database. Not an applicant tracker. This is the **intelligence** layer — the rubric, the questions, the scoring discipline — that sits on top of whatever sourcing or ATS you already use.

## Why we're giving this away

Most founders hire on gut feel, regret the bad calls, and then spend three months unwinding them. The intelligence above is what a good staffing partner brings to the room. It's not the labor — it's the lens.

We're TalentCollyde. We run this for our clients end to end — sourcing, screening, scoring, calibration over time. If you hit three open roles at once, the unit economics of running this yourself stop making sense. That's when you call us. Until then, use the kit.

## See it first

[Sample scorecard PDF](https://github.com/Collyde-Inc/talentcollyde-hire/blob/main/examples/sutter-and-vine/roles/head-of-operations/candidates/jordan-park/scorecard.pdf) — the kit produced this end-to-end from a recorded role intake and pasted interview notes. Open it before you install.

## Install

Inside Claude Code, run two commands:

```
/plugin marketplace add https://github.com/Collyde-Inc/talentcollyde-hire.git
/plugin install talentcollyde-hire@talentcollyde
```

The first command registers TalentCollyde's marketplace (a small JSON manifest at the root of this repo). The second installs the plugin from it. Once installed, run `/talentcollyde-hire:start` to begin.

To update later, run `/plugin install talentcollyde-hire@talentcollyde` again.

## Run order

The skills are sequential. Each one reads what the previous one wrote.

```
/talentcollyde-hire:onboard      →  company.md
/talentcollyde-hire:intake       →  roles/<role-slug>/{job_description, personas, interview_rubric, STATUS}
/talentcollyde-hire:questions    →  roles/<role-slug>/interview_kit.md
/talentcollyde-hire:score        →  roles/<role-slug>/candidates/<cand-slug>/scorecard.pdf
```

You can re-run any step. The skills are idempotent and won't overwrite your work without asking.

## Folder it creates

In whatever directory you launch Claude from, the plugin creates:

```
talentcollyde-hire/
├── founder_interview_guide.md    # the guide you record against
├── company.md                    # synthesized from your recording
├── .intake/
│   └── onboarding_transcript.txt # you drop the transcript here
└── roles/
    └── <role-slug>/
        ├── STATUS.md
        ├── job_description.md
        ├── personas.md
        ├── interview_rubric.md
        ├── interview_kit.md
        ├── .intake/
        │   └── role_intake_transcript.txt   # role-level recording
        └── candidates/
            └── <cand-slug>/
                ├── interview_notes.md
                ├── scorecard.pdf
                └── scorecard.md (fallback if no reportlab)
```

The default folder is `talentcollyde-hire/` — keep it. If you're running the kit in a workspace dedicated to one company and want the folder named for that company instead, you can rename it (the Sutter & Vine example does — its workspace folder is named after the business). Skills detect by content, not name.

A worked example ships with the plugin at `examples/sutter-and-vine/` — a fictional natural wine subscription with a fictional founder, role, and candidate. Open the scorecard PDF there first to see what the kit produces.

## Requirements

- Claude Code with the plugin installed.
- Python 3.9+ and `reportlab` for the branded scorecard PDF (`pip install reportlab --break-system-packages`). The PDF is the marquee outcome of `/talentcollyde-hire:score` — install reportlab before you score your first candidate. If it's missing, the skill will pause and ask whether to install or fall back to a markdown scorecard. The markdown carries the same scoring and evidence, but you'll miss the branded leave-behind.

## The hard rules

These four skills inherit the discipline TalentCollyde uses internally. The non-negotiables, slimmed for founder use:

1. **Evidence first, score second.** No number gets assigned until the evidence brief is complete.
2. **Leadership intent overrides JDs.** What you said about the role in intake beats whatever boilerplate the JD picked up.
3. **Insufficient Data — never estimate.** If you didn't get signal on a dimension, mark it IDQ and redistribute weight. Do not assign a middle-of-the-road score to be safe.
4. **Score to 0.1 precision.** Round numbers (X.0, X.5) are suspect. The decimal forces the model to argue against the adjacent tenth.
5. **Pass/fail gates are gates, not scored dimensions.** A cleared gate doesn't also earn points elsewhere.

These show up in the scorecard. If your scorecard ever feels generic, the rules weren't applied — re-run.

## When to stop using this and call us

Three signals:

- **You're hiring 3+ roles concurrently.** The math on running this yourself flips around req #3.
- **You don't have time to source.** This plugin doesn't find candidates. We do.
- **You've made a bad hire and want to understand why.** Calibration — pattern memory across your hires — isn't in the kit. It's the part that compounds over time, and it's what we build for our retained clients.

[talentcollyde.com](https://talentcollyde.com) · [book a 20-min hiring audit](https://talentcollyde.com/audit)

## License

MIT. Use it, modify it, share it. Attribution appreciated but not required.

---

*Built by [TalentCollyde](https://talentcollyde.com). We place senior operators who actually close — three weeks, not three months.*
