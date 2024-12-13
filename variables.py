from sympy import symbols, pi, Rational
from sympy.physics.units import millimeter, second, newton, kilogram, meter

from source import *

variable_values = {}
variable_descriptions = {}
variable_definition_source = {}
variable_value_source = {}


def describe_variable(name, unit, description, description_source, value, value_source):
    variable = globals()[f"_{name}"] = symbols(name)
    variable_descriptions[variable] = description
    variable_definition_source[variable] = description_source
    variable_values[variable] = value * unit if unit is not None else value
    variable_value_source[variable] = value_source

    return variable


d_i = describe_variable("d_i", millimeter, "Inner-race Diameter", Source(BBL, 48), 3.737,
                        "https://myonic.com/optimyn-dental-bearings/ (418NA)")

d_o = describe_variable("d_o", millimeter, "Outer-race Diameter", Source(BBL, 48), 5.74,
                        "https://myonic.com/optimyn-dental-bearings/ (418NA)")

Z = describe_variable("Z", None, "Number of Balls", Source(ACBT, 194), 7,
                      "https://myonic.com/optimyn-dental-bearings/ (418NA)")

d_b = describe_variable("d_b", millimeter, "Ball Diameter", Source(BBL, 48), 1,
                        "https://myonic.com/optimyn-dental-bearings/ (418NA)")

centistoke = millimeter * millimeter / second
v_o = describe_variable("v_o", centistoke, "Viscosity of the Oil within the Grease",
                        Source(ECBT, 186), 10,
                        "https://www.skf.com/us/products/lubrication-management/lubricants/low-temperature-extremely-high-speed")

f_o = describe_variable("f_o", newton * ((second ** Rational(4, 3)) / (millimeter ** Rational(10, 3))),
                        "Factor to Calculation Torque Due to Lubrication Viscous Friction",
                        Source(ECBT, 186), 0.7, Source(ECBT, 186))

RPM = 1 / (60 * second)
n_i = describe_variable("n_i", RPM, "Inner Race Speed", Source(ECBT, 181), 700_000, Design)
n_o = describe_variable("n_o", RPM, "Outer Race Speed", Source(ECBT, 181), -300_000, Design)

degree = pi / 180.0
alpha = describe_variable("alpha", degree, "Contact Angle", Source(ECBT, 181), 15,
                          "https://www.bardenbearings.co.uk/C30X17M3HY971")

F_a = describe_variable("F_a", newton, "Axial Load", Source(ECBT, 159), 7,
                        "https://doi.org/10.1115/1.4048695")

F_r = describe_variable("F_r", newton, "Radial Load", Source(ECBT, 159), 1,
                        "https://doi.org/10.1115/1.4048695")

z = describe_variable("z", None, "Bearing Design and Load Factor", Source(ECBT, 186), 0.0007,
                      Source(ECBT, 186))

y = describe_variable("y", None, "Bearing Design Factor", Source(ECBT, 186), 0.44,
                      Source(ECBT, 186))

C_s = describe_variable("C_s", newton, "Static Load Capacity", Source(ECBT, 175), 52,
                        "https://www.bardenbearings.co.uk/C30X17M3HY971")

X_s = describe_variable("X_s", None, "Radial Load Conversion Coefficient", Source(ECBT, 176),
                        0.5, Source(ECBT, 178))

Y_s = describe_variable("Y_s", None, "Axial Load Conversion Coefficient", Source(ECBT, 176),
                        0.47, Source(ECBT, 178))

# g = describe_variable("g", millimeter/(second ** 2), "Gravitational Acceleration Constant",
#                       Source(ACBT, 63), 9806.65, "https://en.wikipedia.org/wiki/Gravitational_acceleration")

rho = describe_variable("rho", kilogram/(millimeter ** 3), "Density of Si3N4", Source(ACBT, 64),
                        3.17e-6, "https://en.wikipedia.org/wiki/Silicon_nitride")
