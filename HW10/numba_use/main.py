from pi_approx import approximate_pi  # Import optimized function
import time

def main():
    """
    Runs Pi approximation sequentially and measures execution time.
    """
    nums = [1_822_725, 22_059_421, 32_374_695, 88_754_320, 97_162_662, 200_745_654]

    print("Sequential Execution with Numba Optimization:")
    
    start = time.time()
    results = [approximate_pi(n) for n in nums]  # Uses optimized function
    execution_time = time.time() - start

    for n, pi_value in zip(nums, results):
        print(f"Approximation for {n}: {pi_value}")
    
    print(f"\nTotal Time Taken (Optimized with Numba): {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()