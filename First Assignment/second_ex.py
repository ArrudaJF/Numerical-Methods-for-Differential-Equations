from utils import *

num = 10000
h = 3*np.pi/num
u = np.zeros(num)
x = np.linspace(0, np.pi*3, num)
u[0] = 1
u[1] = 1+h

mi = [0, 1/16, 1/8, 1/4, 1/2, 1, 6/5]

for i in range(2, num-1):
    u[i] = iteration(u, x, i-1, h, mi[1], func_2)


plt.plot(x, u)
plt.show()