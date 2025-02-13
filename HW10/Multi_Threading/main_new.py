from multiThread_new import calculate_parallel
import time
from pi_approx_new import approximate_pi  # Import function from pi_calculator.py

def main():
    """
    Runs Pi approximation both sequentially and in parallel.
    """
    nums = [1_822_725, 22_059_421, 32_374_695, 88_754_320, 97_162_662, 200_745_654]

    # Sequential Execution
    print("Sequential Execution:")
    start = time.time()
    sequential_results = [approximate_pi(n) for n in nums]
    sequential_time = time.time() - start
    for n, pi_value in zip(nums, sequential_results):
        print(f"Approximation for {n}: {pi_value}")
    print(f"Total Time Taken (Sequential): {sequential_time:.2f} seconds\n")

    # Parallel Execution (Calling `calculate_parallel` from `parallel_processing.py`)
    print("Parallel Execution:")
    start = time.time()
    parallel_results = calculate_parallel(nums)  # Calls multiprocessing
    parallel_time = time.time() - start
    for n, pi_value in zip(nums, parallel_results):
        print(f"Approximation for {n}: {pi_value}")
    print(f"Total Time Taken (Parallel): {parallel_time:.2f} seconds")

    print(f"Percentage Improvement: {100 * (sequential_time - parallel_time) / sequential_time:.2f}%")

if __name__ == "__main__":
    print("Running main")
    main()