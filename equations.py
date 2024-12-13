from sympy import cos, cot, Max
from sympy.physics.units import watt, radian

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

omega_i = describe_equation("omega_i", "Rotational Speed of Inner Race", Source(ECBT, 192),
                            n_i * 2 * pi, radian/second)

n_m = describe_equation("n_m", "Cage Speed", Source(ECBT, 183),
                        0.5 * (n_i * (1 - gamma) + n_o * (1 + gamma)), RPM)

M_v = describe_equation("M_v", "Torque Due to Viscous Friction", Source(ECBT, 186),
                        1e-7 * f_o * ((v_o * n_m) ** Rational(2, 3)) * (d_m ** 3), newton * millimeter)

F_c = describe_equation("F_c", "Centrifugal Force on Each Ball", Source(ACBT, 68),
                        (pi ** 3) * rho * (d_b ** 3) * (n_m ** 2) * d_m / 3, newton)

F_rnc = describe_equation("F_rnc", "Radial Load including Centrifugal Force", None,
                          F_r + Z * F_c, newton)

F_beta = describe_equation("F_beta", "Equivalent Load for Moment Calculation", Source(ECBT, 185),
                           Max(0.9 * F_a * cot(alpha) - 0.1 * F_rnc, F_rnc), newton)

F_s = describe_equation("F_s", "Static Equivalent Load", Source(ECBT, 176),
                        Max(F_rnc, X_s * F_rnc + Y_s * F_a), newton)

f_l = describe_equation("f_l", "Load Factor for Moment Calculation", Source(ECBT, 185),
                        z * ((F_s / C_s) ** y), None)

M_load = describe_equation("M_load", "Torque Due to Applied Load", Source(ECBT, 185),
                           f_l * F_beta * d_m, newton * millimeter)

M_tot = describe_equation("M_tot", "Total Friction Torque", Source(ECBT, 186),
                          M_load + M_v, newton * millimeter)

H_tot = describe_equation("H_tot", "Total Friction Heat Generation Rate", Source(ACBT, 194),
                          M_tot * omega_i, watt)
