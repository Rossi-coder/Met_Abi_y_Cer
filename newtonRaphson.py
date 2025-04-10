from math import *    # JALAMOS LO MATEMATICO
import numpy as np    # USAMOS LA LIBRERIA NUMPY
import matplotlib.pyplot as plt  # USAMOS LA LIBRERIA DE PLOT O GRAFICAS

# DEFINIMOS LA FUNCION F(X)
def f(x):
    return pow(x/2 ,2) - 1
  
# DEFINIMOS LA FUNCION DERIVADA F(X)
def F(x):
    return 1/2*x

def newtonRaphson(x, i):
    k = 0
    print('El intervalo es [',x,']')
    while (k<i):
        x = x - (f(x))/(F(x))
        print('El intervalo es [',x,']')
        k = k + 1

    print('x', k, '=', x, 'es una buena aproximacion ')

newtonRaphson(5,3)
