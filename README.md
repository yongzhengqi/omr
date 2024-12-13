# Bearing Heat Generation Analysis

This project calculates and visualizes parameters related to the friction torque, viscous drag, and resulting heat generation in high-speed bearings. It uses **Sympy** for symbolic mathematics, **Sympy’s unit system** for unit conversions, and **Matplotlib** for plotting the results.

## Overview

The code defines a set of variables and equations from engineering references (such as BBL, ECBT, and others) to model the behavior of a bearing under given loads, speeds, and geometric parameters. It then computes derived quantities like:

- Pitch Diameter (d_m)
- Cage Speed (n_m)
- Viscous Friction Torque (M_v)
- Total Friction Heat Generation Rate (H_tot)

And more.

The user can vary input parameters such as the inner race speed (`n_i`) and outer race speed (`n_o`) and plot how the resulting heat generation or torque changes. Additionally, the code supports:

- Normalizing results against a standard reference value.
- Interpolating and plotting 3D surfaces of results.
- Identifying operating points that yield results closest to a desired ratio.

## Project Structure

- **variables.py**:  
  Defines and describes variables (e.g., bearing dimensions, speeds, load factors) and associates them with units and reference values.
  
- **equations.py**:  
  Defines symbolic equations that compute various quantities based on the variables.

- **main.py**:  
  - Substitutes values into equations.
  - Converts units to a consistent system.
  - Evaluates expressions numerically.
  - Plots results in 2D and 3D (e.g., showing how H_tot changes with n_i and n_o).
  - Identifies points on the plot that correspond to a desired ratio.

## Requirements

- Python 3.8+
- [Sympy](https://www.sympy.org/) for symbolic mathematics and units.
- [NumPy](https://numpy.org/) for numerical arrays.
- [Matplotlib](https://matplotlib.org/) for plotting.
- [tqdm](https://github.com/tqdm/tqdm) for progress bars (optional).

Install these packages using:
```bash
pip install sympy numpy matplotlib tqdm
```

If you use Anaconda or a virtual environment, ensure they are activated before installing.

## Running the Code

1. **Set up your environment**:
   ```bash
   conda create -n bearing_env python=3.10
   conda activate bearing_env
   pip install sympy numpy matplotlib tqdm
   ```

2. **Run main.py**:
   ```bash
   python main.py
   ```
   
   The script will:
   - Print computed values of defined equations.
   - Generate and display plots (2D and/or 3D) depending on the code you have enabled.

## Plotting Features

- **Normalized Plot (H_tot ratio)**:  
  The main script demonstrates how to compute `H_tot` for a range of `n_i` values and then normalize it by a standard reference. It plots the normalized values and highlights the point closest to a ratio of 1.

- **3D Surface Plot**:  
  By varying both `n_i` and `n_o`, the code can create a surface plot showing how the normalized heat generation changes. Invalid or unrealistic data points are handled by setting them to `NaN`, which will not be plotted.

- **2D Plot of Selected Points**:  
  After identifying, for each `n_i`, the `n_o` that yields a ratio closest to 1, the code plots these `(n_i, n_o)` pairs in a separate 2D plot.

## Customization

- You can change the ranges of `n_i` and `n_o` in the code to explore different operating conditions.
- You can modify the standard reference value or the variables defined in `variables.py` to simulate different bearing designs or environmental conditions.
- Unit conversions and rational exponents are used to maintain numerical stability and ensure clean simplifications.


## References

- Hamrock, Bernard J., and Duncan Dowson. "Ball bearing lubrication: the elastohydrodynamics of elliptical contacts." (1981).
- Harnoy, Avraham. Bearing design in machinery: engineering tribology and lubrication. CRC press, 2002.
- Harris Tedric, A., and N. KotzalasMicheal. "Rolling bearing analysis essential concepts of bearing technology." Taylor and Francis (2007).
- Harris Tedric, A., and N. KotzalasMicheal. "Rolling bearing analysis advanced concepts of bearing technology." Taylor and Francis (2007).
