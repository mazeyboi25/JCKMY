import time
import random
from multiprocessing import Pool, cpu_count

def generate_papers(num_papers, num_questions):
    return [
        [random.randint(0, 1) for _ in range(num_questions)]
        for _ in range(num_papers)
    ]

def grade_paper(paper):
    total = 0
    for answer in paper:
        total += answer
    return total

def sequential_grading(papers):
    results = []
    for paper in papers:
        results.append(grade_paper(paper))
    return results

def parallel_grading(papers):
    with Pool(cpu_count()) as pool:
        results = pool.map(grade_paper, papers)
    return results

if __name__ == "__main__":
    NUM_PAPERS = 200000
    NUM_QUESTIONS = 50

    print("Generating papers...")
    papers = generate_papers(NUM_PAPERS, NUM_QUESTIONS)

    print("\nRunning Sequential Version...")
    start = time.time()
    seq_results = sequential_grading(papers)
    seq_time = time.time() - start
    print(f"Sequential Time: {seq_time:.4f} seconds")

    print("\nRunning Parallel Version...")
    start = time.time()
    par_results = parallel_grading(papers)
    par_time = time.time() - start
    print(f"Parallel Time: {par_time:.4f} seconds")

    if seq_results == par_results:
        print("\nResults are identical ")
    else:
        print("\nResults do NOT match ")

    speedup = seq_time / par_time
    print(f"\nSpeedup: {speedup:.2f}x")