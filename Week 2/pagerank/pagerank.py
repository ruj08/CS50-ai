import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    for filename in os.listdir(directory):  # Take the links from the html files and put them in a dictionary
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename)) as f:
                contents = f.read()
                links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
                pages[filename] = set(links) - {filename}

    for filename in pages:  # Limit the links that redirect to other pages in the corpus
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages)
    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    n = len(corpus)
    distribution = {p: 0 for p in corpus}

    links = corpus.get(page, set())
    if len(links) == 0:  # If page has no outgoing links, treat it as linking to all pages
        links = set(corpus.keys())

    random_part = (1 - damping_factor) / n
    link_part = damping_factor / len(links)

    for p in corpus:
        distribution[p] = random_part
        if p in links:
            distribution[p] += link_part

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = {page: 0 for page in corpus}  # Initialize PageRank values
    current_page = random.choice(list(corpus.keys()))  # Start with a random page
    for i in range(n):
        ranks[current_page] += 1
        distribution = transition_model(corpus, current_page, damping_factor)  # Sample the next page using the transition model
        current_page = random.choices(list(distribution.keys()), weights=distribution.values())[0]
    total = sum(ranks.values())  # Normalize the PageRank values
    for page in ranks:
        ranks[page] = ranks[page] / total
    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n = len(corpus)
    ranks = {page: 1 / n for page in corpus}

    converged = False
    while not converged:
        converged = True
        new_ranks = {}
        for page in corpus:
            total = 0
            for other in corpus:  # If other has no outgoing links, treat it as linking to all pages
                if len(corpus[other]) == 0:
                    total += ranks[other] / n 
                elif page in corpus[other]: 
                    total += ranks[other] / len(corpus[other]) 
            random_part = (1 - damping_factor) / n 
            link_part = damping_factor * total
            new_rank = random_part + link_part # Calculate the new PageRank value using the formula
            new_ranks[page] = new_rank
            if abs(new_rank - ranks[page]) >= 0.001: # Check for convergence
                converged = False
        ranks = new_ranks # Update the PageRank values for the next iteration
    return ranks

if __name__ == "__main__":
    main()
