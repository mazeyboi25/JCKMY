import random

def generate_papers(num_papers, num_questions):
    return {
        (random.randint(0, 1) for i in range(num_questions))
        for i in range(num_papers)
    }
def grade_paper(paper):
    total = 0
    for answer in paper:
        total += answer
    return total