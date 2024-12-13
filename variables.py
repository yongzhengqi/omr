from sympy import symbols
from sympy.physics.units import millimeter

from source import *

variable_values = {}
variable_descriptions = {}
variable_definition_source = {}
variable_value_source = {}


def describe_variable(name, unit, description, description_source, value, value_source):
    variable = globals()[f"_{name}"] = (symbols(name) * unit if unit is not None else symbols(name))
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

