# Founder Interview Guide — <Company Name>

**Purpose:** Capture *who you are as a company* in your own words. Everything downstream — interview rubrics, candidate scorecards, the bar you hold the hiring process to — is anchored in what comes out of this conversation.

**Time:** 25–30 minutes total. Don't rush, don't pad.

**Mode:** Pick one before you start.

| Mode | How |
|---|---|
| **Self-record** | Hit record on Loom, Zoom (alone), Granola, your phone's voice memo — anything that produces a transcript. Read each question, then answer like you're explaining your company to a smart friend. Pause between blocks if you need to. |
| **Teammate interview** | Hand this guide to a chief of staff, co-founder, or operator on your team. They run the conversation as an interviewer — same questions, but they're listening, probing, and following up on the spots where you wave your hands. Recorded on Zoom or similar. |

**When you're done:**
1. Get the transcript out of your recording tool (most do this automatically; if not, paste the auto-transcription into a `.txt` file).
2. Drop the transcript at `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt`.
3. Re-invoke `/talentcollyde-hire:onboard`. Claude will synthesize the recording into your `company.md`.

---

## How to do this well

A few things that separate a useful recording from a wasted half hour:

- **Talk in stories.** When a question asks about a value, don't list the value — tell the story of the hire, fire, or decision that made it real. Stories carry the signal.
- **Don't perform.** If your value is "honesty," don't lecture about honesty. Tell me about the time you had to be honest and it cost you something.
- **Pause before you answer.** A 4-second pause produces a more honest answer than a 1-second pause. The recording captures the pause; it's signal too.
- **Skip what doesn't fit.** If a question genuinely doesn't apply to your company, say so out loud and move on. Don't manufacture answers.
- **You can repeat yourself.** The synthesizer reads the whole transcript and pulls themes — you don't have to rehearse.

---

## Block 1 — The company (3 min)

**Why this block exists:** Set the table. Tell me what you do, who pays you for it, and where you are in the company's life.

1. **In plain language, what does your company do — and who pays you for it?**
   *Skip the elevator pitch. Pretend you're talking to a friend who's never heard of your industry.*

2. **What stage are you at?**
   *Pre-revenue / finding fit / scaling / profitable / something else. Be specific — "we're at $2M ARR and adding 50K/month" beats "we're growing."*

---

## Block 2 — Mission and values (8 min)

**Why this block exists:** Hiring decisions trace back to what you actually believe — not what's on your About page. We need the real ones.

3. **What's the underlying problem you're trying to solve in the world?**
   *Not the product. The deeper why. The thing that would make you mad if no one ever fixed it.*

4. **What are 3–5 values that actually shape how you operate?**
   *Not aspirational ones — the ones you'd fire someone over. The ones that show up in your day-to-day decisions whether you mean them to or not.*

5. **For each value: give me one moment — a hire, a fire, a decision — that made that value real.**
   *Take a minute per value. Tell the story. The story is the value.*

---

## Block 3 — What thrives, what dies (6 min)

**Why this block exists:** Every company has a shape — patterns where some people fit and others don't. Naming the shape is what makes hiring repeatable.

6. **Describe the last person who absolutely thrived on your team.**
   *Not a job title or a resume. The human. What was it about how they showed up that made them work here? What did you notice in the first 90 days?*

7. **Describe someone who didn't make it — even if they were talented. What didn't fit?**
   *This is the highest-signal question in the whole guide. Be honest. The shape of "doesn't fit" is more useful than the shape of "fits."*

---

## Block 4 — Hiring philosophy (5 min)

**Why this block exists:** Every founder has a stated approach to hiring and a *real* approach. We need the real one.

8. **When you hire, what matters more — speed (get a seat filled) or fit (wait for the right person)?**
   *Be honest about the tradeoff you actually make. Most founders say "fit" and act on "speed." That's fine — but tell me which is true for you.*

9. **Do you tend to hire from your network, or cast wide?**
   *And what's your gut on that approach — do you trust it, or have you been burned?*

10. **Who's involved in the decision — just you, a co-founder, the team?**
    *Walk me through how a "yes" actually happens. Not the org chart — the real flow.*

---

## Block 5 — Founder profile and brand (8 min)

**Why this block exists:** You are part of the hiring criteria — what you respond to, what you ignore, what you want candidates to walk away feeling. The rubric needs to know.

11. **When you've made a great hire, what tipped you to 'yes'?**
    *What did you see in the room that others might have missed?*

12. **When you've made a bad hire, what did you ignore?**
    *What was the signal you talked yourself past? Don't soften this — it's the most valuable thing you'll say all hour.*

13. **How do you want candidates to feel after they interview with you — even the ones you don't hire?**
    *This is the standard the whole process will be held to.*

14. **What's your brand's primary accent color?**
    *Hex code if you know it (`#1a1a2e` style). Otherwise just describe it: "forest green," "navy," "burnt orange." We'll match it on your scorecards.*

15. **Anything else about your company I should know before I start writing role rubrics?**
    *Free space. The thing you almost forgot.*

---

## After you stop recording

1. **Export the transcript.**
   - **Loom:** auto-generates a transcript in the video page. Copy it.
   - **Zoom:** Cloud recordings auto-transcribe. Download as `.vtt` or `.txt`.
   - **Granola:** copy the meeting notes / transcript.
   - **Fireflies / Otter:** copy the transcript text.
   - **Phone voice memo:** upload the audio to Otter, Whisper, or a similar tool and export the text.
2. **Save it as `onboarding_transcript.txt`** (or `.md` or `.vtt`).
3. **Drop it at** `<workspace>/talentcollyde-hire/.intake/onboarding_transcript.txt`.
4. **Re-invoke** `/talentcollyde-hire:onboard`. Claude will read the transcript, map it to the 7 sections of `company.md`, quote you back to yourself, and flag anything you didn't cover.

---

*Generated by [TalentCollyde Hire](https://talentcollyde.com/hire). When you're hiring 3+ roles concurrently and running this process yourself becomes the bottleneck → [talentcollyde.com](https://talentcollyde.com)*
