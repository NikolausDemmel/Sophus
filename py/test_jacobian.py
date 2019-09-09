#!/usr/bin/env python3

import sympy

from sophus.matrix import dot, squared_norm, Vector2, Vector3, Vector6, ZeroVector2, ZeroVector3, ZeroVector6, proj, unproj

from sophus.so3 import So3
from sophus.so3m import So3m

from sophus.se3 import Se3


def R_symbol():
    return sympy.Matrix(3, 3, lambda r, c: sympy.symbols("r{}{}".format(r,c)))


if __name__ == "__main__":
    # R = R_symbol()
    # sympy.pprint(R)
    omega = sympy.Matrix(sympy.symbols('w_0, w_1, w_2', real=True))
    sympy.pprint(So3m.exp(omega))
