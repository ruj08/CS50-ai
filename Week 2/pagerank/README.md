# Software Development Learning Cycle: Page Rank

## 1) Planning

### Goal

The goal of this project is to build a program that ranks web pages based on how important they are.

We do this using three main parts:

1. **Transition Model**
   - Calculates the probability of moving from the current page to another page.
   - Uses a damping factor to decide whether to follow a link or jump to a random page.

2. **Sampling PageRank**
   - Simulates a “random surfer” clicking links many times.
   - Pages that are visited more often get a higher rank.

3. **Iterative PageRank**
   - Repeatedly updates the rank of every page.
   - Stops when the values no longer change.
   - The final stable values are the PageRank scores.

---

### Success Criteria
The project is successful when:

- The program prints a PageRank value for every page.
- All PageRank values add up to 1 (since they represent probabilities).
- The iterative method stops once the values become stable.
- The sampling method gives results close to the iterative method when using a large sample size (like 10,000).
---

### Project Requirements:
- All logic occurs in `pagerank.py`
- Only `transition_model`, `sample_pagerank` and `iterate_pagerank` are modified
- Python standard library modules, numpy and pandas are the only allowed Python modules.

## Analysis:

### Tools:
- `pagerank.py` was given
- Corpus folders were given

### Timeline & Steps:
- Create the transition model
  - Create a dictionary with every page inside of it and its base probability of 0 for each page.
  - If the current page has no links, then it is a random choice among all the pages in the corpus.
  - If it has links, then each page gets a base probability of the random chance plus the chance of its link being selected.
- Create the sample PageRank
  - Pick a random page to start at.
  - For every remaining page, pick a new page based on the transition model's probabilities for each page. 
    - Select a random page while considering those probabilities.
  - Tally the visits which each page gets.
  - Give each page a rank based on how many visits it got divided by the number of visits made in total.
- Create the iterate PageRank
  - Create some base values for the function to use.
    - Number of pages.
    - Starting rank of each page.
    - The random chance of selecting any one page.
  - Create the current ranks dictionary and the new ranks dictionary.
  - Create a variable to track how much the largest difference in rank was for the latest iteration and make a while loop using that as its condition.
    - Rank them based on the probability of going to the current page from any other page.
    - Find the largest change and store it.
    - Update the current rankings with the newly found rankings.
    - Exit the while loop if the largest change in ranking is small enough to be near zero. Eg. 0.001.

### Troubleshooting Techniques:
- Use print statements to identify what the code considers the probabilities as in each step.
- Go step by step through the code adding more each time to identify where it breaks.
- Check the dictionaries to see if any probabilities are unreasonably high to point yourself in the right direction of what portion of the code might be breaking.

### Flowchart:
![PageRank Flowchart.png](PageRank%20Flowchart.png)
# PageRank — CS50 AI (Week 2)

## 1) Planning

### Goal

The goal of this project is to build a program that ranks web pages based on how important they are.

We do this using three main parts:

1. **Transition Model**
   - Calculates the probability of moving from the current page to another page.
   - Uses a damping factor to decide whether to follow a link or jump to a random page.

2. **Sampling PageRank**
   - Simulates a “random surfer” clicking links many times.
   - Pages that are visited more often get a higher rank.

3. **Iterative PageRank**
   - Repeatedly updates the rank of every page.
   - Stops when the values no longer change.
   - The final stable values are the PageRank scores.

---

### Success Criteria
The project is successful when:

- The program prints a PageRank value for every page.
- All PageRank values add up to 1 (since they represent probabilities).
- The iterative method stops once the values become stable.
- The sampling method gives results close to the iterative method when using a large sample size (like 10,000).
---

### Project Requirements
- Use only Python’s standard library (no external libraries).
- The program must run from the command line.
- Pages with no outgoing links (dangling pages) must be treated as if they link to all pages.

---

## 2) Analysis
### Tools and Concepts Used

Main file: `pagerank.py` which contains all main functions.

Python modules used:
- `os` (for reading files)
- `re` (for finding links in HTML)
- `random` (for sampling)
- `sys` (for command line input)

Important definitions and ideas:

- **Transition Model:** Gives the probability of moving to the next page.
- **Sampling:** Simulates many random clicks to estimate importance.
- **Iteration:** Repeatedly updates ranks using a formula until values stop changing.

---

### Important Rules Followed

- Pages with no links are treated as linking to all pages.
- The damping factor (usually 0.85) means:
  - 85% chance of following a link.
  - 15% chance of jumping to a random page.
- All probability values must add up to 1.
---

## Timeline and Steps
### Step 1: Crawl the Corpus

Use `crawl(corpus_dir)` to:
- Read all HTML files in the folder.
- Find links inside each file.
- Store them in a dictionary (page → linked pages).
- Only count links that exist inside the corpus.

---

### Step 2: Transition Model

Create `transition_model(corpus, page, damping_factor)`.

This function:

- Returns the probability of going to each page.
- Uses the damping factor to choose between:
  - Following a link
  - Jumping to a random page

---

### Step 3: Sampling PageRank

Create `sample_pagerank(corpus, damping_factor, n)`.

This function:

- Starts on a random page.
- Simulates clicking links `n` times.
- Counts how many times each page is visited.
- Converts counts into probabilities.

---

### Step 4: Iterative PageRank

Create `iterate_pagerank(corpus, damping_factor)`.

This function:

- Starts by giving every page the same rank.
- Updates ranks using the PageRank formula.
- Repeats until changes are very small (such as 0.001).
- Returns the final ranks.

---

### Step 5: Command Line Output

Run the program using this line of bash:

```bash
python pagerank.py corpus0
```

The program prints each page and its PageRank value.

---

### Step 6: Testing
Test the program using the example corpus folders:

- `corpus0`
- `corpus1`
- `corpus2`

Run PageRank on a corpus directory:

```bash
python pagerank.py corpus0
python pagerank.py "corpus's/corpus1"
```

Example output:

```
A.html: 0.037
B.html: 0.207
...
```
Each number shows how important the page is compared to the others.
---

## 5) Files in This Folder
- `pagerank.py` — Main program file.
- `README.md` — This file.
- `corpora/` — Example test folders:
  - `corpus0/`
  - `corpus1/`
  - `corpus2/`
Each corpus contains HTML pages used as input.

---
## 6) Flowchart

---

## 7) Troubleshooting

If something goes wrong:
- Make sure only internal links are counted.
- Make sure dangling pages (pages that contain no outgoing links) are handled correctly.
- Check that probabilities add up to 1.
- If iteration does not stop, check your formula.
- If sampling looks inaccurate, increase `n`.