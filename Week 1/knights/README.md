# Software Development Learning Cycle: Knights and Knaves

## 1) Planning

### Goal
Create a knowledge base for each puzzle that allows the program to determine which characters are knights and which are knaves.

### Success Criteria
The program is successful when it can correctly evaluate each knowledge base and return the correct solution for every provided puzzle.

### Project Requirements
- All reasoning must be done using the provided `logic.py` (must remain unchanged).
- No additional libraries may be imported.
- The program must correctly solve and evaluate every puzzle.

---

## 2) Analysis

### Tools
This project relies on the logic operators provided in `logic.py`, including:

- `Symbol`
- `Evaluate`
- `Not`
- `And`
- `Or`
- `Implication`
- `Biconditional`
- `model_check`

It also includes symbols representing whether each character is a Knight or a Knave.

---

## Timeline and Steps 

### Step 1: Import logic tools and create symbols
First, the program imports every logic operator from `logic.py` and defines symbols for each possible role:

- `AKnight`, `AKnave`
- `BKnight`, `BKnave`
- `CKnight`, `CKnave`

These symbols can be used build each puzzle’s knowledge base.

Also, there are rules to the puzzles that are explained:
- Knights always tell the truth. 
- Knaves always lie. 
- No character can be both a knight and a knave. 
- Every character must be either a knight or a knave.

---

### Step 2: Build `knowledge0` (Puzzle 0)
Puzzle 0 is implemented first, using only character A.

1. Translate A’s statement into implications:
   - If A is a Knight, then A’s statement must be true.
   - If A is a Knave, then A’s statement must be false.

2. Combine all rules using `And(...)` to form `knowledge0`.

---

### Step 3: Build `knowledge1` (Puzzle 1)
Puzzle 1 introduces character B.

1. Translate A’s statement (“We are both knaves.”):
   - If A is a Knight, then both A and B must be knaves.
   - If A is a Knave, then the statement must be false.

2. Combine the rules and implications using `And(...)` to form `knowledge1`.

---

### Step 4: Build `knowledge2` (Puzzle 2)
Puzzle 2 contains statements from both A and B.

1. Translate A’s statement (“We are the same kind.”):
   - If A is a Knight, then A and B must match (both Knights or both Knaves).
   - If A is a Knave, then A and B must be different kinds.

2. Translate B’s statement (“We are of different kinds.”):
   - If B is a Knight, then A and B must be different kinds.
   - If B is a Knave, then A and B must be the same kind.

3. Combine the rules and implications into `knowledge2`.

---

### Step 5: Build `knowledge3` (Puzzle 3)
Puzzle 3 includes three characters (A, B, C) and multiple dependent statements.

1. Add logic for A’s unknown statement:
   - A said either “I am a knight.” or “I am a knave.”
   - Since the exact statement is unknown, the knowledge base must handle both possibilities through a logical statement. 

2. Translate B’s statements:
   - B claims: “A said ‘I am a knave.’”
   - B claims: “C is a knave.”

   These can be shown using implications for when B is a Knight and when B is a Knave.

3. Translate C’s statement:
   - C claims: “A is a knight.”

   This can be shown using implications for when C is a Knight and when C is a Knave.

4. Combine the rules and implications into `knowledge3`.

---


## 4) Flowchart
See the Flowchart PDF for a visual representation of the timeline and step-by-step process.

---

## 5) Troubleshooting Techniques
- Use a truth table (done on paper) to trace through the logic step-by-step.
- Add comments beside complex logical expressions to improve readability and help future debugging.
