# Role Intake Guide — <Role Title> at <Company Name>

**Purpose:** Capture what you're actually looking for in this hire — beyond the boilerplate JD. This recording becomes the rubric, the personas, the JD, and the interview kit. Get this right and every candidate gets evaluated against *your* standard, not a generic one.

**Time:** 20–25 minutes for a full recording. Shorter is fine for a first pass.

---

## Mode

| Mode | How |
|---|---|
| **Self-record** | Hit record on Loom, Zoom (alone), Granola, your phone's voice memo. Talk through each question. |
| **Teammate interview** | Hand this guide to a chief of staff, operator, or co-founder. They run the conversation as an interviewer — same questions, but probing where you wave your hands. Recorded on Zoom or similar. |

## How to do this well

- **Talk in stories.** When you describe the ideal hire, tell me about a real person — the last great person you hired, or the one you wish you could clone. Stories beat adjectives.
- **Name the anti-pattern.** When asked about dealbreakers, picture the candidate you'd reject in the first 5 minutes. What did they say? What did they do?
- **Surface your tensions.** "I want speed *and* quality" is fine — but say so. The skill catches tensions, doesn't paper over them.
- **Pause before you answer.** A 4-second pause produces a more honest answer than a 1-second pause.
- **Skip what doesn't apply.** Don't manufacture answers to fit the structure.

---

## Block 1 — Why this hire (3 min)

**Why this block exists:** Anchor the role to a business problem. If the founder can't say why now, the rubric won't have direction.

1. **What problem does this hire solve for the business?**
   *Be specific — what's broken right now that this person fixes?*

2. **If you don't fill this role in 90 days, what breaks?**
   *Forces honesty about urgency. A role that doesn't break anything in 90 days is a role you don't need yet.*

---

## Block 2 — What success looks like (5 min)

**Why this block exists:** Concrete time-bound outcomes become the rubric's scoring anchors.

3. **Day 30 — what should this person be doing? What does a good first week look like?**
   *Onboarding-shaped. Specific, not abstract. ("Building rapport with the team" doesn't count — "Owning the candidate-side outreach for our top 3 reqs" does.)*

4. **Month 6 — what's different about the business because they're here?**
   *The contribution. Not their personal growth — what changed in the company.*

5. **Month 12 — what does this person own end-to-end?**
   *Scope at full ramp. What's the surface area they're accountable for?*

---

## Block 3 — Profile and must-haves (6 min)

**Why this block exists:** Pulls the *human* out of the JD. The shape of person who fits — and the patterns that don't.

6. **Describe the ideal person — not the resume, the human.**
   *Background. Energy. What motivates them. What do they get out of bed excited about?*

7. **What 2–3 must-haves? The non-negotiables.**
   *Credentials, experiences, certifications. If a candidate doesn't have these, they don't pass the resume read.*

8. **What 2–3 dealbreakers? Things you'd reject for even if everything else looked great.**
   *Picture the candidate you'd walk out on in the first 5 minutes. What did they do? What did they say?*

9. **Past hires that come to mind — yours or someone else's.**
   *The model person (even if you couldn't hire them). The anti-pattern (the hire that didn't work). Past hires are the highest-signal data you have.*

---

## Block 4 — How you'll know (5 min)

**Why this block exists:** Translates your intuition into interview probes. The signal you'd notice in the room becomes the listening cue in the rubric.

10. **The *one signal* in an interview that would tell you this is the right person.**
    *If you had to make the call on one piece of evidence, what would it be?*

11. **The *one signal* that would tell you to walk away — even if everything else looked great.**
    *Highest-leverage question in the block. The pattern you've been burned by before.*

12. **Behaviors or stories you want to probe for.**
    *E.g., "I want to hear how they handle a missed quarter." Or, "I want to see if they push back on me during the interview." Specific scenarios, not generic competencies.*

---

## Block 5 — Comp, location, logistics (3 min)

**Why this block exists:** Boring but load-bearing. If the rubric scores someone "Advance — strong" but they're outside the comp band, we wasted everyone's time.

13. **Comp band — low and high, plus structure.**
    *Base, variable, equity. Be honest about both ends. Are you firm on the high end, or flexible for the right person?*

14. **Location — remote, hybrid, in-office?**
    *If hybrid or in-office, which city. If there's a nearby market that someone might confuse this for (e.g., this is a Bay Area role, not Sacramento) — say so explicitly.*

15. **Reports to whom, manages whom?**
    *And any cross-functional partners they'll work closely with.*

---

## After you stop recording

1. **Export the transcript.**
   - **Loom / Zoom / Granola / Fireflies / Otter:** copy the auto-transcript.
   - **Phone voice memo:** upload to Otter or Whisper and export.
2. **Save it as `role_intake_transcript.txt`** (or `.md` or `.vtt`).
3. **Drop it at:**
   ```
   <workspace>/talentcollyde-hire/roles/<slug>/.intake/role_intake_transcript.txt
   ```
4. **Re-invoke** `/talentcollyde-hire:intake` for this role. Claude reads the transcript, cross-references it against your `company.md`, and writes:
   - `STATUS.md`
   - `job_description.md`
   - `personas.md`
   - `interview_rubric.md` (with pass/fail gates + weighted scoring dimensions)

Then run `/talentcollyde-hire:questions` to generate the interview kit from the rubric.

---

*Generated by [TalentCollyde Hire](https://talentcollyde.com/hire). When you're hiring 3+ roles concurrently and running this process for each one becomes the bottleneck → [talentcollyde.com](https://talentcollyde.com)*
