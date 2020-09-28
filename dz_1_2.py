import math
import cmath
import numpy as np


def solve_quad(b, c):
    if b == 0 and c == 0:
        x1 = 0
        x2 = 0
        return x1, x2
    if c >= 0:

        if (1 - (2 / b) * math.sqrt(c)) * math.sqrt(
                1 + (2 / b) * math.sqrt(c)) >= 0:
            x1 = - (b / 2) * (
                    1 + math.sqrt((1 - (2 / b) * math.sqrt(c))) * math.sqrt(
                1 + (2 / b) * math.sqrt(c)))
            x2 = c / x1
            return x1, x2
        else:
            x1 = - (b / 2) * (
                    1 + cmath.sqrt((1 - (2 / b) * math.sqrt(c))) * math.sqrt(
                1 + (2 / b) * math.sqrt(c)))
            x2 = c / x1
            return x1, x2
    else:

        if (1 - (2 / b) * math.sqrt(c)) * math.sqrt(
                1 + (2 / b) * math.sqrt(c)) >= 0:
            x1 = - (b / 2) * (
                    1 + math.sqrt((1 - (2 / b) * cmath.sqrt(c))) * math.sqrt(
                1 + (2 / b) * cmath.sqrt(c)))
            x2 = c / x1
            return x1, x2

        else:
            x1 = - (b / 2) * (1 + cmath.sqrt(
                (1 - (2 / b) * cmath.sqrt(c))) * math.sqrt(
                1 + (2 / b) * cmath.sqrt(c)))
            x2 = c / x1
            return x1, x2


variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
            {'b': -1e10, 'c': 4.0}, ]

for var in variants:
    x1, x2 = solve_quad(**var)
    print(np.allclose(x1 * x2, var['c']))
