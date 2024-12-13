import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from sympy.physics.units import convert_to
from sympy import simplify

from equations import *

for equation, name in equations.items():
    result = equation.subs(variable_values).evalf()
    result = convert_to(result, [meter, second, kilogram])
    if equation_unit[equation] is not None:
        result = convert_to(result, equation_unit[equation])
    result = simplify(result)
    print(f"{equation_descriptions[equation]} ({name}) = {simplify(result)}")

# Create a range for n_i values (in RPM)
n_i_values = np.linspace(770_000, 1_000_000, 500)  # 100 points from 500k to 1,000k RPM
H_tot_values = []
standard_value = 2.4962

# Evaluate H_tot for each n_i in the specified range
for val in tqdm(n_i_values):
    # Create a copy of variable_values so we don't overwrite the original
    current_values = variable_values.copy()
    # Update n_i in current_values. n_i is defined with unit RPM, so multiply val by RPM
    current_values[n_i] = val * RPM
    # Substitute and evaluate H_tot
    res = H_tot.subs(current_values).evalf()
    res = convert_to(res, [meter, second, kilogram])
    # Convert units if needed (assuming H_tot is in watts after the calculation)
    # If H_tot needs simplification:
    res = convert_to(res, watt)
    res = simplify(res)
    # Extract the numeric value from the expression if it's something like X*watt
    # The numeric part can be obtained by dividing by the unit:
    numeric_value = (res / watt).evalf()
    H_tot_values.append(float(numeric_value) / standard_value)

# Plot using Matplotlib
plt.figure(figsize=(8,6))
plt.plot(n_i_values, H_tot_values, marker='o')
plt.xlabel('Inner Race Speed (RPM)')
plt.ylabel('Normalized Total Friction Heat Generation Rate')
plt.title('Normalized Total Friction Heat Generation Rate vs Inner Race Speed')
plt.grid(True)

# Draw a horizontal line at y = 1
plt.axhline(y=1, color='r', linestyle='--', label='y=1')

# Find the data point closest to y = 1
differences = np.abs(np.array(H_tot_values) - 1)
closest_index = np.argmin(differences)
closest_x = n_i_values[closest_index]
closest_y = H_tot_values[closest_index]

# Highlight this point
plt.scatter(closest_x, closest_y, color='red', zorder=5)

# Annotate the point with coordinates
plt.annotate(f"({closest_x:.0f} RPM, {closest_y:.3f})",
             xy=(closest_x, closest_y),
             xytext=(closest_x, closest_y+0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             ha='center')

plt.show()