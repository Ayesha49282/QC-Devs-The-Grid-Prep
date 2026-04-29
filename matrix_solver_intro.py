'''
Solving a linear system A*phi = b.
In a Poisson solver, 'A' is the Laplacian matrix, 
'b' is the charge density, and 'phi' is the potential we seek.
'''

import numpy as np

# A: 3x3 Laplacian-like matrix (simplified)
A = np.array([[ 2, -1,  0],
              [-1,  2, -1],
              [ 0, -1,  2]])

# b: Source term (Charge density)
b = np.array([1, 0, 1])

# Solving for phi (Potential)
try:
    phi = np.linalg.solve(A, b)
    print("Solved Potential (phi):")
    print(phi)
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be solved.")
