from math import *    # JALAMOS LO MATEMATICO
import numpy as np    # USAMOS LA LIBRERIA NUMPY
import matplotlib.pyplot as plt  # USAMOS LA LIBRERIA DE PLOT O GRAFICAS

def g(x):
    return 0.4 * exp(pow(x,2)) #PARA LA ECUACION 2*EXP(POW(X,2))-5*X

def puntoFijo(x,N):
    n=0
    while (n<N):
        x=g(x)
        n=n+1
        print(x)

puntoFijo(1,20)
