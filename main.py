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

