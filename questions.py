"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

`expects` is a word or short phrase that a correct answer should contain.
These five questions are written for the `campus_life` corpus and are based on
specific facts contained in that corpus.

`OUT_OF_SCOPE` holds five questions your documents clearly do not cover. Keep
five of them because criterion 3 uses a target of "at least 4 of 5".
"""

QUESTIONS = [
    {
        "question": "What determines priority for juniors and seniors in the housing lottery?",
        "expects": "credit hours",
    },
    {
        "question": "When do unused dining dollars from the spring semester expire?",
        "expects": "May",
    },
    {
        "question": "About how quickly do student parking permits for the west lots sell out?",
        "expects": "three days",
    },
    {
        "question": "What is the main advantage of declaring a major early?",
        "expects": "departmental adviser",
    },
    {
        "question": "How long does a hold on a checked-out library book usually take to arrive?",
        "expects": "two to three days",
    },
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
