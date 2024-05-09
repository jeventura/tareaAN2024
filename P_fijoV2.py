from math import *
import numpy as np
import sympy as sp


def puntoFijo():
    x=sp.symbols('x')
    g=input('Digite la funcion ')
    g=sp.lambdify(x,g)
    x0=input('Digite el valor inicial ')
    x0=float(x0)
    n=input('Digite el número de iteraciones a realizar ')
    n=int(n)
    tol=input('Digite el error máximo permitido ')
    tol=float(tol)
    for k in range(n):
        x1=g(x0)
        if(abs(x1-x0)<tol):
            print('x',k+1,'=',x1,'es un punto fijo')
            return
        x0=x1
        print('x',k+1,'=',x1)
puntoFijo()