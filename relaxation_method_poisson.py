'''
Solving the 1D Poisson equation using the Relaxation (Jacobi) Method.
Iteratively updates each point to satisfy the Laplace/Poisson condition.
'''

import numpy as np

def relax_poisson(phi, rho, iterations=100):
    n = len(phi)
    for _ in range(iterations):
        for i in range(1, n-1):
            # Poisson step: phi[i] = average of neighbors + source term
            phi[i] = 0.5 * (phi[i+1] + phi[i-1] + rho[i])
    return phi

# Setup: 20 points, zero potential everywhere, small charge in middle
n_points = 20
phi_initial = np.zeros(n_points)
rho_source = np.zeros(n_points)
rho_source[10] = 0.5 # A point charge at the center

phi_final = relax_poisson(phi_initial.copy(), rho_source)

print("Potential after Relaxation:")
print(np.round(phi_final, 3))
