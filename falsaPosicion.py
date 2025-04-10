from math import *    # JALAMOS LO MATEMATICO
import numpy as np    # USAMOS LA LIBRERIA NUMPY
import matplotlib.pyplot as plt  # USAMOS LA LIBRERIA DE PLOT O GRAFICAS

# DEFINIMOS LA FUNCION F(X)
def f(x):
    return pow(x/2 ,2) - 1

def falsaposicion(a,b,i):
    n=0
    while (n <i):
        n=n+1
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if (f(a)*f(c) <0):
            b=c
        else:
            a=c
        print(c)

  falsaposicion(0,6,3)
