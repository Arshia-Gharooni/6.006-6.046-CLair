import numpy as np

def matrix_product_checker(A, B, C):
    n = len(A)
    
    # Frievald's Algorithm
    def frievald_algorithm(A, B, C):
        r = np.random.randint(2, size=n)  # Generate random binary vector
        Br = np.dot(B, r) % 2
        ABr = np.dot(A, Br) % 2
        Cr = C % 2
        return ABr, Cr
    
    # Check if A × B = C using random trials
    for _ in range(n**2):
        ABr, Cr = frievald_algorithm(A, B, C)
        if not np.array_equal(ABr, Cr):
            return "NO"
    
    return "YES"
