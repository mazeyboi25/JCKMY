import threading
import time

def compute_subject_gwa(grade, index, results):
    time.sleep(0.1) 
    print(f"[Thread-{index}] Subject {index + 1} grade = {grade}")
    results[index] = grade

if __name__ == "__main__":
    n = int(input("Enter number of subjects: "))
    grades = []

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)

    results = {}
    threads = []

    start_time = time.time()

    for i, grade in enumerate(grades):
        t = threading.Thread(
            target=compute_subject_gwa,
            args=(grade, i, results)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    gwa = sum(results.values()) / len(results)

    end_time = time.time()

    print("\nAll threads finished.")
    print(f"Overall GWA (all subjects): {gwa:.2f}")
    print(f"Multithreading Execution Time: {end_time - start_time:.4f} seconds")

# Each subject grade in the multithreading version is managed by an individual thread that operates separately from the others. 
# The operating system plans for all threads to run simultaneously when they are first initiated, which means that their execution 
# and completion times may differ. This results in a non-deterministic order of outcomes, with each thread printing its output as 
# soon as it finishes. Following the completion of each thread, the computer calculates and shows the overall GWA, making sure that 
# all subject grades appear in the final output.