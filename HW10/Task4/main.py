from pi_approx import approximate_pi  # Import optimized function
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    """
    Runs Pi approximation and plots results.
    """
    nums = [1_822_725, 22_059_421, 32_374_695, 88_754_320, 97_162_662, 200_745_654]
    true_pi = 3.141592653589793  # Actual value of Pi

    # Compute approximations
    start = time.time()
    approximations = [approximate_pi(n) for n in nums]
    execution_time = time.time() - start

    # Print Results
    print("Pi Approximations:")
    for n, pi_value in zip(nums, approximations):
        print(f"Approximation for {n}: {pi_value}")

    print(f"\nTotal Time Taken: {execution_time:.2f} seconds")

    # Plot Results
    plt.figure(figsize=(10, 6))
    plt.plot(nums, approximations, marker='o', linestyle='', label="Approximated Pi")
    plt.axhline(y=true_pi, color='r', linestyle='--', label="True π (3.141592653589793)")
    
    # Labels and Title
    plt.title("Pi Approximations vs. True Value", fontsize=14)
    plt.xlabel("Number of Iterations (n)", fontsize=12)
    plt.ylabel("Approximated Pi Value", fontsize=12)
    plt.legend()
    plt.grid(True)

    # Save the plot
    #plt.savefig("pi_approximation_plot.png")  # Save as an image file
    plt.show()  # Display the plot

if __name__ == "__main__":
    main()
