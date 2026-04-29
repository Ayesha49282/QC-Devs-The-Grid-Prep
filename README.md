# ⚛️ The Grid | GSoC 2026 Preparation

This repository contains my preliminary research and numerical implementations for the **'Implementation of a Robust Poisson Solver'** project under the **QC-Devs (Theochem)** organization for GSoC 2026.

As a Physics student, my focus is on developing efficient, grid-based numerical methods for solving electrostatic potentials in complex systems.


## 🛠️ Implemented Numerical Modules

Below are the core components developed for the Poisson Solver prototype:

### 🔹 1. Field Potentials & Relaxation Methods
* `relaxation_method_poisson.py`: Implementation of the **Jacobi Relaxation** technique to solve 1D/2D Poisson equations iteratively.
* `energy_density_calculation.py`: Script to compute the total electrostatic energy density by integrating the potential gradient.

### 🔹 2. Discrete Operators & Linear Algebra
* `laplacian_operator_2d.py`: A vectorized 2D **Laplacian operator** using finite difference approximations (5-point stencil).
* `matrix_solver_intro.py`: Solving the discretized Poisson system ($A\phi = b$) using linear system inversion techniques.

### 🔹 3. Integration & Boundary Physics
* `numerical_integration_trapezoidal.py`: Core routine for numerical integration of charge densities.
* `charge_density_1d.py`: Modeling spatial charge distributions ($\rho$) for the source term.
* `boundary_conditions_2d.py`: Handling Dirichlet and Neumann boundary conditions for the potential field.
