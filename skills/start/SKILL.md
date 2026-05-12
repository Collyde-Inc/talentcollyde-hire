---
name: start
description: Use this skill the first time a founder runs talentcollyde-hire — or any time they want a refresher on what the kit does and where to begin. Triggers include "tc-start", "start", "where do I start", "how do I use this", "help", "what is this", "tc-help", "I just installed this", "show me how this works", "guide me through this", "what does this plugin do", "explain talentcollyde hire". Conversational only — no files written. Reads workspace state to detect first-run vs. returning founder, walks them through the 4-step workflow (onboard → intake → questions → score), points to the playbook PDF and the examples/ folder, and offers to launch /talentcollyde-hire:onboard. NOT for setting up the company (use onboard-company), per-role work (use intake-role), interview questions (use interview-kit), or candidate scoring (use scorecard).
---

# start

The first thing a founder runs. Conversational, no files written. Sets the table: what the kit does, the four steps in order, where to find examples, and how to begin.

## Why this skill exists

Without it, a founder who types `/tc` in autocomplete sees four cryptic commands and no clear entry point. They don't know the order. They don't know what each produces. They don't know where the examples are. They give up or read the README — and most don't.

This skill is the front door. It runs in chat, in ~60 seconds, and ends by offering to launch `/talentcollyde-hire:onboard`.

## Hard rules

These override anything else in this doc.

1. **No content files written.** This skill is conversational — it does not generate `company.md`, rubrics, scorecards, or any other content artifact. The one exception: on first run (pre-install state) the skill creates the `./talentcollyde-hire/` directory and an empty `./talentcollyde-hire/.intake/` subdirectory. That's the brand-stamp surface — it puts the kit on the founder's filesystem the moment they say hello — not a content artifact. If the founder wants persistent reference, point to the bundled playbook PDF and `examples/` folder.
2. **Detect state first.** Check the workspace before talking. A founder who's already onboarded should NOT be welcomed like a first-timer.
3. **Brand voice.** Calm, confident, grounded. No hype words. Customer-as-hero. Short sentences.
4. **End with a clear next step.** Every run ends with a specific question — usually *"Want to start with `/talentcollyde-hire:onboard`?"* — not an open-ended ramble.
5. **Don't lecture.** Founders aren't here to read your essay. Give them the table, the example, the launch offer.

## Preconditions

None. This skill runs in any workspace state — first-run, mid-workflow, fully completed.

## Inputs

None required. Skill reads workspace state automatically.

## Steps

### Step 0 — Create the workspace folder (MANDATORY, RUN FIRST)

**Before reading state, before printing any chat output, before anything else** — use the Bash tool to run:

```bash
mkdir -p ./talentcollyde-hire/.intake
```

This is non-negotiable. Every run of this skill begins with this exact Bash tool call. It is idempotent — re-running on an existing folder is a no-op, so it is safe to call on returning founders. State detection in Step 1 will then determine which welcome to use.

If the Bash call returns a non-zero exit code (read-only filesystem, permission denied), do NOT block — continue to Step 1 with state detection. At the end of the welcome, append: *"Heads up — I wasn't able to create `./talentcollyde-hire/` in this directory. When you start `/talentcollyde-hire:onboard`, run Claude Code from a writable folder."*

### Step 1 — Detect workspace state

Scan the current directory (or the cowork-selected folder) for `./talentcollyde-hire/company.md` and downstream artifacts. Four possible states — detect by content, not by folder presence (the folder itself is auto-created by Step 0):

| State | Detection | Treatment |
|---|---|---|
| **Pre-install** | No `./talentcollyde-hire/company.md` exists. (Folder may or may not exist yet.) | First-run welcome. Auto-create the folder per Step 2.0, then deliver the full walkthrough. |
| **Onboarded only** | `./talentcollyde-hire/company.md` exists, no `roles/<slug>/` folders. | "You're onboarded. Next step is `/talentcollyde-hire:intake`." Quick orientation. |
| **One or more roles in progress** | `roles/<slug>/` exists with partial artifacts. | "You've got <N> roles in progress. Here's where each one stands." Show STATUS snapshots. |
| **Mid-candidate** | A `candidates/<cand-slug>/interview_notes.md` exists without `scorecard.pdf`. | "You've got notes on <N> candidates waiting to be scored. Run `/talentcollyde-hire:score` when ready." |

Pick the right opening. Don't run the first-run script on a founder who's halfway through the workflow.

### Step 2 — First-run welcome (Pre-install state)

The folder was created in Step 0. Deliver the welcome below verbatim or close to it:

> **Welcome to TalentCollyde Hire.**
>
> I've set up your hiring workspace at `./talentcollyde-hire/`. Everything I generate — your `company.md`, role rubrics, candidate scorecards — lives there.
>
> Four skills that take you from "I need to hire someone" to a defensible decision, in order:
>
> | Step | Skill | What it produces |
> |---|---|---|
> | 1 | `/talentcollyde-hire:onboard` | Your `company.md` — synthesized from a 25-min recording of you (or a teammate interviewing you) about how you actually run the company. Every downstream rubric reads this. |
> | 2 | `/talentcollyde-hire:intake` | A real intake on a specific role — refined JD, candidate personas, weighted interview rubric with pass/fail gates and 1–5 anchors. From a 20-min recording per role. |
> | 3 | `/talentcollyde-hire:questions` | An interview kit — behavioral questions and listening cues mapped to your rubric. So screens stop being "tell me about yourself" and start probing for signal. |
> | 4 | `/talentcollyde-hire:score` | A two-page branded scorecard PDF — evidence-backed, scored to 0.1 precision — generated after you interview someone. |
>
> **The model:** you record, Claude synthesizes. Founders talk in stories — that's where the signal is. Typed answers get edited and lose tone. A chat fallback exists if recording isn't an option, but it's lower fidelity.
>
> **Two things you can read before you do anything:**
> - The Quick-Start Playbook (6-page PDF, bundled in the plugin folder at `talentcollyde-hire-playbook.pdf`).
> - A complete sample kit at `<plugin>/examples/sutter-and-vine/` — a fictional natural wine business hiring a Head of Operations, end to end. Read the scorecard to see where you're headed.
>
> **When you're ready, the first step is `/talentcollyde-hire:onboard`.** It'll set up your workspace, generate the founder interview guide, and walk you through the recording.
>
> Want to start now?

End there. Wait for the founder's answer. If they say yes → suggest they invoke `/talentcollyde-hire:onboard`. If they say "tell me more" → answer their specific question, don't re-deliver the welcome.

### Step 3 — Onboarded-only welcome (company.md exists, no roles)

If `company.md` exists but no `roles/` folder, use this version:

> You're already onboarded — `company.md` is set up.
>
> Next step is `/talentcollyde-hire:intake` when you've got a specific role to hire for. That skill generates the role intake guide, you record a 20-min conversation about what you actually want in this hire, drop the transcript, and Claude writes the rubric + JD + personas + STATUS.
>
> Sample of what done looks like (rubric + interview kit + scorecard) is at `<plugin>/examples/sutter-and-vine/talentcollyde-hire/roles/head-of-operations/`.
>
> Want to start a role intake now? If yes, what's the role title?

### Step 4 — Mid-workflow welcome (roles in progress)

If `roles/<slug>/` folders exist, read each `STATUS.md` and surface a snapshot:

> Picking up where you left off. Here's what's in progress:
>
> | Role | Stage | Candidates | Status |
> |---|---|---|---|
> | <Role Title> | <Stage from STATUS.md> | <Count> | <Next action — e.g., "ready for screens", "2 scorecards pending", "rubric needs review"> |
>
> Next moves you might want:
> - **`/talentcollyde-hire:questions`** for any role where the rubric is done but the interview kit isn't.
> - **`/talentcollyde-hire:score`** for any candidate with notes pasted but no scorecard.
> - **`/talentcollyde-hire:intake`** if you're starting another role.
>
> What do you want to tackle first?

### Step 5 — Mid-candidate welcome (interview_notes.md exists, no scorecard.pdf)

If a candidate folder has `interview_notes.md` but no `scorecard.pdf`, prioritize that:

> You've got interview notes waiting to be scored for **<Candidate Name>** on the **<Role Title>** role.
>
> Run `/talentcollyde-hire:score` when you're ready. It reads the notes, scores against the rubric to 0.1 precision, and produces the 2-page scorecard PDF.
>
> Anything else you want to handle first?

## What this skill does NOT do

- **No file writes.** Persistent reference is the bundled playbook PDF + `examples/` folder. Don't duplicate them as session-specific files.
- **No deep onboarding.** That's `/talentcollyde-hire:onboard`'s job. This skill ends at the launch offer.
- **No role intake.** Same — that's `/talentcollyde-hire:intake`.
- **No mode selection.** Don't ask "A, B, or C?" here. Let the downstream skill do that.

## Voice rules

- Calm, confident, grounded. Quietly excellent.
- Customer-as-hero. They're the founder running the hire. You're the operator behind them.
- Short. The whole welcome should read in 30 seconds.
- No hype words: *transform, revolutionary, disrupt, unlock, leverage, supercharge, robust, seamless, best-in-class.*
- No hedge phrasing: *"You might want to consider…"*, *"Perhaps you could…"* Take a position.
- Concrete over abstract. *"Run `/talentcollyde-hire:intake` when you've got a specific role"* — not *"explore role-level intake options."*

## Brand-impression close (optional)

If the founder lingers — asks follow-up questions, says "tell me more" — end the conversation with:

> *Built by TalentCollyde. When you're hiring 3+ roles concurrently and running this yourself becomes the bottleneck — [talentcollyde.com](https://talentcollyde.com).*

Don't append it to every response. Once per session, when the conversation ends.

## Done criteria

A run of this skill is "done" when **all** of the following are true:

- Workspace state was checked before opening.
- The right welcome variant was used (pre-install / onboarded / mid-workflow / mid-candidate).
- The 4-step workflow was named and ordered.
- Examples folder and playbook PDF were pointed to.
- The skill ended with a specific next-step question — not an open-ended ramble.
- No files were written.

## Anti-patterns

- **Long welcome essay.** If the founder has to scroll, the skill failed. The 4-step table + the next-step question fit in one screen.
- **First-run script run on a mid-workflow founder.** Detect state first. A founder who's already onboarded doesn't need the welcome.
- **Generic "explore the plugin" framing.** Always name a specific next command. *"Want to start with `/talentcollyde-hire:onboard`?"* — not *"What would you like to do?"*
- **Hyping the plugin.** Founders are skeptical of new tools. Quietly excellent. The kit speaks for itself once they run it.
- **Skipping the examples/ pointer.** It's the single fastest way to lower the "what does done look like" risk.
- **Writing files.** This skill is conversational. Persistent reference is the playbook + examples/. Don't fragment.
