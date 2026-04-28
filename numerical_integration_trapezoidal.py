'''
Numerical integration using the Trapezoidal Rule.
Crucial for solving integral forms of Maxwell's equations 
and Poisson systems.
'''

import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    f: function to integrate
    a, b: interval [a, b]
    n: number of trapezoids
    """
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    integration = (dx/2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integration

# Example: Integrating a simple charge density function
def charge_density_fn(x):
    return x**2  # Simple quadratic distribution

result = trapezoidal_rule(charge_density_fn, 0, 1, 100)

print(f"The integral of charge density from 0 to 1 is: {result:.4f}")
