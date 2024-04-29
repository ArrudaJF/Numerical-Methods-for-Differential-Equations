import numpy as np
import matplotlib.pyplot as plt
import timeit

def func_1(x):
    return 0

def func_2(x):
    return np.sin(x)**3/16

def iteration(u, x, n, h, mi, callback): 
    const = (mi*h/2)*(u[n]**2-1)
    u[n+1] = (2-h**2)*u[n]/(1+const) + (const -1)*u[n-1]/(1+const) + callback(x[n])
    return u[n+1]

