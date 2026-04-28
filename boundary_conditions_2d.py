'''
Applying Dirichlet Boundary Conditions for a 2D Grid.
In a Poisson solver, we must define the potential at the edges 
(e.g., keeping the walls of a box at 0V).
'''

import numpy as np

def apply_boundary_conditions(grid_size):
    # Create a grid of zeros
    phi = np.zeros((grid_size, grid_size))
    
    # Setting boundary values (Dirichlet)
    phi[0, :] = 10.0   # Top wall at 10V
    phi[-1, :] = 0.0  # Bottom wall at 0V
    phi[:, 0] = 5.0   # Left wall at 5V
    phi[:, -1] = 5.0  # Right wall at 5V
    
    return phi

# Initialize a 5x5 grid
initial_phi = apply_boundary_conditions(5)

print("Initial Potential Grid with Boundary Conditions:")
print(initial_phi)
