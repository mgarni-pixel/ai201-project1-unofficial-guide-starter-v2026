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
Evidence: `results/run_2026-09-23_1859_before.md`, written by
`run_eval.py::main`. Three runs per question, cache off.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks preserve complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source matches the correct document | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

### Criterion 1

Top chunk for "When do unused dining dollars from the spring semester expire?"
(`expects`: "May"), retrieved by `store.py::search`, produced by
`chunker.py::split_documents`:

```
--- admin_dining_dollars.txt  distance 0.2838
On the dining dollars

Declining balance — what everyone calls dining dollars — rolls over from the autumn semester to the spring, but not from spring to the following autumn. Whatever is left in May disappears.
```

The `expects` phrase is in a retrieved chunk for all five questions. 5 of 5.

### Criteria 2 and 5

All five answers, run 1, from `results/run_2026-09-23_1859_before.md`, written
by `generate.py::answer_from_chunks`:

```
For juniors and seniors, priority in the housing lottery is determined by accumulated credit hours first, with ties broken randomly (admin_housing_lottery.txt).

Unused dining dollars from the spring semester disappear in May (they do not roll over to the following autumn). This information comes from `admin_dining_dollars.txt`.

Student parking permits for the west lots sell out in about three days (admin_parking_permits.txt).

The only advantage to declaring a major early is that it assigns you a departmental adviser, who is generally more useful than the general one (admin_declaring_a_major.txt).

A hold on a checked-out book usually arrives in two to three days. (Source: admin_library_holds.txt)
```

Every answer names a file, so criterion 2 is 5 of 5. Each file named is the one
that holds the fact, so criterion 5 is 5 of 5.

### Criterion 3

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6:

```
Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.825)  What is the capital of Mongolia?
  refused  (best distance 0.934)  How do I change the oil in a diesel engine?
  refused  (best distance 0.886)  Who won the 1994 World Cup?
  refused  (best distance 0.803)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.877)  How do I write a for loop in Rust?
  -> gate refused 5 of 5
```

### Criterion 4

Five chunks sampled across the 105 produced by `chunker.py::split_documents`,
showing how each ends:

```
admin_add_drop_deadline.txt   ...students find out from each other.
course_cs_340_exams.txt       ...everyone learns this the hard way.
dining_kestrel_commons.txt    ...one meal swipe, or $12.50 cash.
housing_innisfree_hall.txt    ...one bathroom between two rooms.
winter_gear.txt               ...considerably later on weekends.
```

None is cut mid-sentence. 5 of 5.


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | Target 4 of 5. Each question's `expects` phrase appears literally in one of the five chunks `store.py::search` returned, in all three runs. 5 of 5. |
| 2 | Every answer names a source | MET | Target 5 of 5. All fifteen answers contain a `.txt` filename. 5 of 5 in each run. |
| 3 | Gate stops out-of-corpus questions | MET | Target 4 of 5. The gate refused all five, the closest at 0.803 against the 0.6 cutoff. 5 of 5. |
| 4 | Chunks preserve complete thoughts | MET | Target 4 of 5. All five sampled chunks start and end on sentence boundaries. 5 of 5. |
| 5 | Cited source matches the correct document | MET | Target 4 of 5. The file each answer cited is the file that contains the `expects` phrase, in all three runs. 5 of 5. |

No criterion revised. All five were measurable, which is the only ground the
unit accepts for a revision.

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

No criterion was missed, so there is no failure to trace to a stage.

**The targets were set low.** Criterion 4 could not have failed: `CHUNK_SIZE`
is 800 and the longest document in `campus_life` is 563 characters, so
`chunker.py::split_documents` never splits anything. Criterion 2 tests an
instruction the prompt already gives the model, since
`generate.py::answer_from_chunks` is handed the filenames. Criteria 1, 3 and 5
all asked for 4 of 5 and all returned 5 of 5 with no near misses.

**Criterion 3 is the one I would tighten.** I filed it against five questions
from another world entirely: Mongolia, diesel engines, the 1994 World Cup,
ibuprofen, Rust. Refusing those is not evidence the gate works. I re-ran it
against five questions a student here might ask that the corpus does not cover.
The words tuition, gym, parking ticket, fraternity and heater appear in 0 of
the 88 documents.

Retrieved by `store.py::search`, gate decision by `gate.py::check`, cutoff 0.6:

```
  refused  0.657  admin_parking_permits.txt     How do I appeal a parking ticket?
  LET IN   0.496  health_center.txt             What are the gym's opening hours?
  refused  0.722  orientation_what_matters.txt  How do I join a fraternity?
  refused  0.760  housing_innisfree_hall.txt    Where do I report a broken heater in my dorm?
  LET IN   0.484  admin_add_drop_deadline.txt   What is the tuition payment deadline?
  gate refused 3 of 5
```

Same 4 of 5 target, harder questions, 3 of 5.

**The stage is embedding.** `gate.py` compares a distance against 0.6 and does
that correctly. The distance is wrong. "What is the tuition payment deadline?"
lands at 0.484 next to `admin_add_drop_deadline.txt` because the corpus is full
of registrar deadlines and the question sounds like them. The distance measures
whether a question sounds like the corpus, not whether the corpus contains the
answer.

**Tightened criterion 3, for the next unit:** the gate refuses at least 4 of 5
questions that fit the corpus's subject but are not covered by it.


## The Improvement

**What I changed:** I added BM25 keyword search alongside the meaning-based
search in `store.py::search`. Each chunk now gets a keyword score as well as a
cosine distance, and the two are blended into the single distance
`gate.py::check` already compares against `THRESHOLD`. The keyword index is
built from the chunks Chroma already holds. Two settings in `config.py` control
it, `HYBRID_ALPHA` and `BM25_FULL_MARK`. That is the only change; chunking,
corpus, model, threshold and prompt are untouched.

**Why I picked it:** My diagnosis found the gate admitting "What is the tuition
payment deadline?" at 0.484 because the question sounds like a corpus full of
registrar deadlines. The words those questions turn on appear in 0 of the 88
documents, which a keyword score can see and a meaning score cannot.

**Choosing the settings.** I scored 20 questions in four groups of five: my
filed questions, the same reworded, the campus-shaped questions from my
diagnosis, and the filed `OUT_OF_SCOPE` set. The first ten should be answered
and the last ten refused, so each setting scores out of 20. No API calls, since
the gate decides before the model.

```
correct out of 20   columns = BM25_FULL_MARK
           15    20    25    30    40
 0.00      17    17    17    17    17
 0.10      17    17    17    17    17
 0.20      17    17    17    17    17
 0.25      17    17    17    18    17
 0.30      17    18    18    17    16
 0.35      18    18    17    15    16
 0.40      18    17    16    16    16
 0.50      17    16    17    16    15
 0.60      15    17    16    15    15
```

Meaning-only scores 17. The best is 18, and 0.5, the value that looks like a
sensible default, scores 16 — worse than making no change. I took alpha 0.3
with a mark of 20 because it sits beside two other 18s rather than alone.

### Run Log — After

Evidence: `results/run_2026-09-25_1930_after.md`, written by
`run_eval.py::main`. Three runs per question, cache off.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks preserve complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source matches the correct document | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

All five answers, run 1, written by `generate.py::answer_from_chunks`:

```
For juniors and seniors in the housing lottery, priority is determined by accumulated credit hours first, with a random tie-breaker used if needed (admin_housing_lottery.txt).

Unused dining dollars from the spring semester disappear in May (they do not roll over to the following autumn).
Source: `admin_dining_dollars.txt`

Student parking permits for the west lots sell out in about three days (admin_parking_permits.txt).

The only advantage to declaring early is that it assigns you a departmental adviser, who is generally more useful than the general one (admin_declaring_a_major.txt).

A hold on a checked-out book usually arrives in two to three days (admin_library_holds.txt).
```

### Before and after

My five filed questions, best distance:

| Question | Before | After |
|---|---|---|
| Housing lottery priority | 0.220 | 0.184 |
| Dining dollars expiry | 0.284 | 0.199 |
| Parking permits | 0.199 | 0.139 |
| Declaring a major | 0.337 | 0.236 |
| Library holds | 0.147 | 0.103 |

The campus-shaped questions from my diagnosis, which is what the change was for:

| Question | Before | After |
|---|---|---|
| How do I appeal a parking ticket? | 0.657 refused | 0.659 refused |
| What are the gym's opening hours? | 0.496 let in | 0.608 refused |
| How do I join a fraternity? | 0.722 refused | 0.797 refused |
| Where do I report a broken heater in my dorm? | 0.760 refused | 0.740 refused |
| What is the tuition payment deadline? | 0.484 let in | 0.551 let in |
| | 3 of 5 refused | 4 of 5 refused |

The same five questions reworded, which the corpus does answer:

| Question | Before | After |
|---|---|---|
| Do upperclassmen get better housing picks? | 0.524 pass | 0.582 pass |
| If I don't spend my meal money, do I lose it? | 0.498 pass | 0.558 pass |
| Should I rush to get a permit for the west lots? | 0.412 pass | 0.488 pass |
| Is there any point declaring a major sooner? | 0.630 refused | 0.654 refused |
| How long until a held book is mine? | 0.461 pass | 0.559 pass |
| | 4 of 5 answered | 4 of 5 answered |

**Did it help?** Yes, by one question in twenty. The gate refuses 4 of 5
campus-shaped questions instead of 3 of 5. "What are the gym's opening hours?"
moved from 0.496 to 0.608 and is now refused, for the reason predicted: gym
appears in none of the 88 documents, so its keyword score is low and the blend
pushed it past the cutoff. Nothing regressed. Reworded questions still answer
4 of 5 and every filed question moved closer.

Two things it did not fix. The tuition question still gets through at 0.551,
because payment and deadline do appear in the corpus even though tuition does
not. And my five criteria read 5 of 5 before and after, and also read 5 of 5 at
alpha 0.5, which measured worse than making no change. The criteria could not
tell the three systems apart.

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
