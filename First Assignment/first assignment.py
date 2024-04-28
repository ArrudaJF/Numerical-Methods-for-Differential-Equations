import numpy as np
import matplotlib.pyplot as plt
import timeit

def iteration(u, n, h, mi): 
    const = (mi*h/2)*(u[n]**2-1)
    u[n+1] = (2-h**2)*u[n]/(1+const) + (const -1)*u[n-1]/(1+const)
    return u[n+1]

num = 1000
h = 3*np.pi/num
x = np.zeros(num)
x[0] = 0
x[1] = h
x[-1] = (x[-2] - h)/(1+h)
mi = [0, 1/16, 1/8, 1/4, 1/2, 1, 6/5]

for i in range(2, num):
    x[i] = iteration(x, i-1, h, mi[0])

plt.plot(np.linspace(0, np.pi*3, num), x)
plt.show()