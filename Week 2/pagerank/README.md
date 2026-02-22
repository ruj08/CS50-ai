# SDLC For PageRank Problem

## Planning:

### Goal:
Have 3 functions with the following functionalities:
1. Transition Model:
   - This should be capable of giving each page in the corpus a probability of being accessed from the current page.
2. Sample PageRank:
    - This should sample n pages according to the transition model starting at a random page and give each page a ranking based on how often they were accessed.
3. Iterative PageRank
    - This should give every page a PageRank iteratively until the values stop changing, at which point those will be the final page ranks.

### Success Criteria:
Success is identified when the code is able to evaluate any given corpus and obtain a probability distribution, sample page rank and iterative page rank.

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
