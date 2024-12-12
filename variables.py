from sympy import symbols
from sympy.physics.units import meter, second

t = symbols('t', positive=True)*second
x = symbols('x', positive=True)*meter

variable_descriptions = {
    x: "text",
    t: "text"
}