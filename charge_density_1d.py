'''
Modeling a Linear Charge Distribution for a 1D space.
Helps to understand how the source term (rho) behaves 
under different physical conditions.
'''

import numpy as np

def linear_charge_density(x, slope, intercept):
    return slope * x + intercept

# Domain setup
x_axis = np.linspace(0, 1, 10) # 1 meter domain
rho_linear = linear_charge_density(x_axis, 2e-9, 0.5e-9)

print("Position (m) | Charge Density (C/m)")
print("-" * 35)
for pos, den in zip(x_axis, rho_linear):
    print(f"{pos:.2f}         | {den:.2e}")
