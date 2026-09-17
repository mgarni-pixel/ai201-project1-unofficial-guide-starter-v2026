# The Unofficial Guide

Manuel Garnica | Corpus: `campus_life`

---

# Unit 1

## What This Does

This system answers questions about student life using the `campus_life`
corpus, a collection of 88 short forum-style posts covering housing, dining,
courses, admin processes, and campus services. You ask a plain question like
"Is the housing lottery random?" and get back an answer drawn from the
documents, with the source file named. If the question isn't covered by the
corpus, the system says so instead of making something up.

## Chunking Strategy

**Chunk size:** paragraph-based (no fixed character count)
**Overlap:** none (splits on blank lines, so boundaries are natural)

The campus_life documents are short forum posts, mostly 180 to 550 characters.
The starter's 800-character window never split anything because nothing reached
800. But some posts pack two or three unrelated facts into separate paragraphs
(e.g. housing_innisfree_hall.txt has room layout, AC, laundry prices, and noise
in one chunk). Splitting on paragraph breaks and merging paragraphs under 150
characters keeps each chunk focused on one thought without producing fragments.
This took the corpus from 88 chunks to 105.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_210.txt#0` — produced by: `chunker.py::split_documents`

```
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Expect 8 to 10 hours a week outside class.

The one piece of advice: do the labs even though they're only 10% — the exams reuse the lab problems.
```

**Chunk 3** — source: `course_math_220_exams.txt#0` — produced by: `chunker.py::split_documents`

```
MATH 220 Linear Algebra — assessment

Two midterms and a cumulative final. Curved to a b- median.

The problem sets are the course; the lectures make sense afterwards rather than during.
```

**Chunk 4** — source: `dining_verrill_street_grill_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Verrill Street Grill

Adding to what people have said about Verrill Street Grill. The wait figure of up to 30 minutes on Friday evenings matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_morrow_house_laundry.txt#0` — produced by: `chunker.py::split_documents`

```
Laundry in Morrow House

Machines take $1.50 wash, $1.25 dry, coin or card. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

## Sample Answer

**Question:** What determines priority for juniors and seniors in the housing lottery?

**Answer:**

```
(best distance 0.220, cutoff 0.6)

For juniors and seniors, priority in the housing lottery is determined by
accumulated credit hours first, with a random tie-break used if needed
(admin_housing_lottery.txt).

Sources retrieved: admin_grade_appeals.txt, admin_housing_lottery.txt,
advising_registration.txt, course_stat_150_exams.txt,
dining_the_atrium_followup.txt
```

**My relevance cutoff:** 0.6

In-scope questions landed between 0.15 and 0.34. Out-of-scope questions landed
between 0.80 and 0.93. The gap between the two groups is wide (0.34 to 0.80),
so 0.6 sits comfortably in the middle with no risk of cutting into either
group.

| Question | In corpus? | Best distance |
|---|---|---|
| What determines priority in the housing lottery? | Yes | 0.220 |
| When do unused dining dollars expire? | Yes | 0.284 |
| How quickly do west lot parking permits sell out? | Yes | 0.199 |
| What is the main advantage of declaring a major early? | Yes | 0.337 |
| How long does a library hold take to arrive? | Yes | 0.147 |
| What is the capital of Mongolia? | No | 0.825 |
| How do I change the oil in a diesel engine? | No | 0.934 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen? | No | 0.803 |
| How do I write a for loop in Rust? | No | 0.877 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I used AI to help setup the repo for commits and help me follow instructions. I got full help from AI on following instructions while it helped me follow along the activities by helping me understand what instructions mean and what I should do to follow along and complete milestones. AI contributed towards brainstorming and helping fill out task work while I corrected it on the scope.

**2.** Another moment was github commits. Claude handled it automatically alongside helping me understand what was needed for the milestone before moving on. I got commits that were successful based on milestone progress. I just made sure to change that it double checked with me to ensure I am understanding the progress alongside having me double check the work it does.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
