from sympy.physics.units import convert_to

from equations import *

for equation, name in equations.items():
    result = equation.subs(variable_values).evalf()
    if equation_unit[equation] is not None:
        result = convert_to(result, [newton, meter, second])#equation_unit[equation])
    print(f"{equation_descriptions[equation]} ({name}) = {result}")

