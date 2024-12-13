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
plt.figure(figsize=(8, 6))
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
             xytext=(closest_x, closest_y + 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             ha='center')

plt.show()

# Choose ranges for n_i and n_o (in RPM)
n_i_values = np.linspace(500000, 1000000, 50)  # 50 points for inner race speed
n_o_values = np.linspace(-600000, -300000, 50)  # 50 points for outer race speed (just an example range)
standard_value = 2.4962

# Prepare arrays to hold H_tot ratios
H_tot_ratio = np.zeros((len(n_i_values), len(n_o_values)))

# Evaluate H_tot on the (n_i, n_o) grid
for i, n_i_val in enumerate(tqdm(n_i_values, desc="Computing H_tot surface")):
    for j, n_o_val in enumerate(n_o_values):
        current_values = variable_values.copy()
        # Update n_i and n_o in current_values
        current_values[n_i] = n_i_val * RPM
        current_values[n_o] = n_o_val * RPM

        # Substitute and evaluate H_tot
        res = H_tot.subs(current_values).evalf()

        # Convert to SI base units first
        res = convert_to(res, [meter, second, kilogram])
        # Convert to watts
        res = convert_to(res, watt)
        res = simplify(res)

        # Extract numeric value in watts
        numeric_value = (res / watt).evalf()

        # Store normalized value
        try:
            H_tot_ratio[i, j] = float(numeric_value) / standard_value
        except:
            H_tot_ratio[i, j] = np.nan

# Create a meshgrid for plotting
N_i_mesh, N_o_mesh = np.meshgrid(n_i_values, n_o_values, indexing='xy')

# Plot the 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Transpose H_tot_ratio if needed, depending on the indexing above
# We used indexing='xy', so N_i_mesh[i,j] corresponds to n_i_values[i], n_o_values[j].
# H_tot_ratio[i,j] is consistent since i -> n_i, j -> n_o.
# If the axes seem flipped, you can swap them in the plot call.
surf = ax.plot_surface(N_i_mesh, N_o_mesh, H_tot_ratio, cmap='viridis', edgecolor='none')

# Label axes
ax.set_xlabel('Inner Race Speed (RPM)')
ax.set_ylabel('Outer Race Speed (RPM))')
ax.set_zlabel('Normalized Heat Generation Rate')

ax.set_title('Normalized Total Friction Heat Generation Rate as a Function of Inner and Outer Race Speed ')

fig.colorbar(surf, shrink=0.5, aspect=5, label='H_tot/Benchmark')
plt.tight_layout()
plt.show()


n_i_values = np.linspace(500000, 1000000, 500)  # 50 points for inner race speed
n_o_values = np.linspace(-600000, -100000, 500)  # 50 points for outer race speed (just an example range)
standard_value = 2.4962

# Prepare arrays to hold H_tot ratios
H_tot_ratio = np.zeros((len(n_i_values), len(n_o_values)))

for i, n_i_val in enumerate(tqdm(n_i_values, desc="Computing H_tot surface")):
    for j, n_o_val in enumerate(n_o_values):
        current_values = variable_values.copy()
        current_values[n_i] = n_i_val * RPM
        current_values[n_o] = n_o_val * RPM

        try:
            res = H_tot.subs(current_values).evalf()
            # Convert to SI units, then watts
            res = convert_to(res, [meter, second, kilogram])
            res = convert_to(res, watt)
            res = simplify(res)
            numeric_value = (res / watt).evalf()
            # Store normalized value
            H_tot_ratio[i, j] = float(numeric_value) / standard_value
        except:
            H_tot_ratio[i, j] = np.nan

chosen_n_i = []
chosen_n_o = []

for i, n_i_val in enumerate(n_i_values):
    row = H_tot_ratio[i, :]
    # Ignore NaNs
    valid_indices = ~np.isnan(row)
    if not np.any(valid_indices):
        # If no valid data for this n_i, skip
        continue

    # Among valid values, find the one closest to 1
    valid_n_o = n_o_values[valid_indices]
    valid_row = row[valid_indices]

    differences = np.abs(valid_row - 1)
    if min(differences) < 0.01:
        min_idx = np.argmin(differences)
        closest_n_o = valid_n_o[min_idx]
        closest_val = valid_row[min_idx]

        # Check if there's a realistic "close" value (optional)
        # If you just want the closest regardless:
        chosen_n_i.append(n_i_val)
        chosen_n_o.append(closest_n_o)

# Plot the (n_i, n_o) pairs in 2D
plt.figure(figsize=(8, 6))
plt.plot(chosen_n_i, chosen_n_o, marker='o')
plt.xlabel('Inner Race Speed (RPM)')
plt.ylabel('Outer Race Speed (RPM)')
plt.title('Inner and Outer Speed Pairs that Generate Standard Heat')
plt.grid(True)
plt.show()

