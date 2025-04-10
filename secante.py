from math import *    # JALAMOS LO MATEMATICO
import numpy as np    # USAMOS LA LIBRERIA NUMPY
import matplotlib.pyplot as plt  # USAMOS LA LIBRERIA DE PLOT O GRAFICAS

# DEFINIMOS LA FUNCION F(X)
def f(x):
    return pow(x/2 ,2) - 1

def secante(a, b, i):
    k = 0
    print ('El valor aproximado es: [',b,']')
    
    while (k<i):
        x = b - (f(b) * (b-a))/(f(b) - f(a))
        a = b
        b = x
        print ('El valor aproximado es: [',x,']')
        k = k + 1

    print ('x',k,'=',x,'es una buena aproximacion')

secante(5, 10 , 3)
