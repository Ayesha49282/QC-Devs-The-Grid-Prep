'''
Calculating the Electrostatic Energy Density from the Potential.
Energy = 0.5 * epsilon * |E|^2, where E = -grad(phi).
'''

import numpy as np

def calculate_energy(phi, dx):
    # E-field is the negative gradient of potential
    ex = -np.gradient(phi, dx)
    
    # Energy density (ignoring constants for simplicity)
    energy_density = 0.5 * ex**2
    total_energy = np.trapz(energy_density, dx=dx)
    
    return total_energy

# Sample potential (linear ramp)
phi_sample = np.linspace(0, 10, 50) 
dx = 0.2

total_e = calculate_energy(phi_sample, dx)
print(f"Total Electrostatic Energy in the domain: {total_e:.4f} units")
