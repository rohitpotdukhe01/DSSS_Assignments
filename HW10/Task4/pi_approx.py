import numpy as np
from numba import njit

@njit  # JIT compilation for speed
def approximate_pi(n):
    """
    Approximates Pi using a continued fraction formula.
    
    Args:
        n (int): Number of iterations for approximation.
    
    Returns:
        float: Approximate value of Pi.
    """
    pi_2 = 1
    nom, den = 2.0, 1.0
    for i in range(n):
        pi_2 *= nom / den
        if i % 2:
            nom += 2
        else:
            den += 2
    return 2 * pi_2
