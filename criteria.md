# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The dining-dollars question expects "May," a single common word that could
match the wrong chunk. The other four have multi-word expects strings, so I
expect those to retrieve cleanly. One miss out of five is realistic.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The prompt template already passes source filenames to the model with the
chunks. If an answer still omits a source, something in the pipeline is broken.
That should not happen on any of the five, so the bar is all five.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
The out-of-scope questions (Mongolia, diesel oil, World Cup, ibuprofen, Rust)
have nothing to do with campus life, so their distances should be large. I
allow one miss because "ibuprofen" might land close to the health-center
document. More than one leak means the threshold needs moving.

---

## 4. Chunks preserve complete thoughts

At least 4 of 5 sampled chunks read as a complete thought, with no sentence
cut in half at either end.

**Why this target:**
Every campus_life document is under 560 characters and CHUNK_SIZE is 800, so
nothing should need splitting. A cut sentence at that size means the chunker
did something wrong. I leave room for one edge case where a header or metadata
line pushes a doc just over.

---

## 5. Cited source matches the correct document

For at least 4 of 5 test questions, the source document cited in the answer is
the document that actually contains the fact, not just any source.

**Why this target:**
Each question maps to one specific admin file (e.g. the parking question to
admin_parking_permits.txt). Criterion 2 only checks that *a* source appears;
this checks it is the *right* one. I expect one miss because "departmental
adviser" shows up in both admin_declaring_a_major.txt and
advising_registration.txt, so retrieval could reasonably pick either.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
