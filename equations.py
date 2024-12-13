from sympy import cos
from sympy.physics.units import newton, meter

from variables import *

equation_source = {}
equation_descriptions = {}
equation_unit = {}
equations = {}


def describe_equation(name, description, description_source, value, unit):
    equation = globals()[f"_{name}"] = value
    equation_descriptions[equation] = description
    equation_source[equation] = description_source
    equation_unit[equation] = unit
    equations[equation] = name

    return equation


d_m = describe_equation("d_m", "Pitch Diameter", Source(BBL, 47), (d_i + d_o) / 2, millimeter)

gamma = describe_equation("gamma", "A Geometric Factor", Source(ECBT, 181),
                          d_b * cos(alpha) / d_m, None)

n_m = describe_equation("n_m", "Cage Speed", Source(ECBT, 183),
                        0.5 * (n_i * (1 - gamma) + n_o * (1 + gamma)), RPM)

M_v = describe_equation("M_v", "Torque Due to Viscous Friction", Source(ECBT, 186),
                        1e-7 * f_o * ((v_o * n_m) ** (2 / 3.0)) * (d_m ** 3), newton * millimeter)

# M_load = describe_equation("M_load", "Torque Due to Applied Load", Source(ECBT, 185),
#                            f_l * F_beta * d_m)
#
# M_tot = describe_equation("M_tot", "Total Friction Torque", Source(ECBT, 186),
#                           M_load + M_v)
#
# H_tot = describe_variable("H_tot", "Total Friction Heat Generation Rate", Source(ACBT, 194),
#                           M_tot * Omega_ring / 1e3)
