from math import *    # JALAMOS LO MATEMATICO
import numpy as np    # USAMOS LA LIBRERIA NUMPY
import matplotlib.pyplot as plt  # USAMOS LA LIBRERIA DE PLOT O GRAFICAS

# DEFINIMOS LA FUNCION F(X)
def f(x):
    return pow(x/2 ,2) - 1

def F(x):
    return 1/2*x

def biseccion(a,b,i):
    n=0
    while (n<3):
        n=n+1          # SE LE AÑADE UNA UNIDAD AL N "ES EL CONTADOR"
        c=(a+b)/2      # ESTE ES EL METODO DE LA BISECCION
        if (f(a)*f(c) <0):
            b=c
        else:  
            a=c
        print(c)

biseccion(0,6,5)
