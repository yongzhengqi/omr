from sympy import symbols, pi
from sympy.physics.units import millimeter, minute, second, newton

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

f_o = describe_variable("f_o", newton * (second ** (4 / 3.0) / (millimeter ** (10/3.0))),
                        "Factor to Calculation Torque Due to Lubrication Viscous Friction",
                        Source(ECBT, 186), 0.7, Source(ECBT, 186))

RPM = 1 / minute
n_i = describe_variable("n_i", RPM, "Inner Race Speed", Source(ECBT, 181), 700_000, Design)
n_o = describe_variable("n_o", RPM, "Outer Race Speed", Source(ECBT, 181), -300_000, Design)

degree = pi / 180.0
alpha = describe_variable("alpha", degree, "Contact Angle", Source(ECBT, 181), 15,
                          "https://www.bardenbearings.co.uk/C30X1701H")
