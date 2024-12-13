from variables import *

equation_source = {}
equation_descriptions = {}

def describe_equation(name, description, description_source, value):
    equation = globals()[f"_{name}"] = value
    equation_descriptions[equation] = description
    equation_source[equation] = description_source

    return equation

d_e = describe_equation("d_e", "Pitch Diameter", Source(BBL, 331), (d_i + d_o) / 2)