import multiprocessing
from pi_approx_new import approximate_pi  # Import function from pi_calculator.py

def calculate_parallel(nums):
    """
    Uses multiprocessing to approximate Pi for multiple values of n.

    Args:
        nums (list): List of values for n.

    Returns:
        list: List of Pi approximations.
    """
    with multiprocessing.Pool() as pool:
        results = pool.map(approximate_pi, nums)  # Parallel execution
    return results
