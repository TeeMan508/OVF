from math import *
import numpy as np
import matplotlib.pyplot as plt

#Начальные условия
a0 = 1
cn = 10

def f(x):
    return sin(x)

n = 200
x1 = 0
x2 = 2*pi
x = np.linspace(x1, x2, n + 1)

a = [a0]
for i in range(1, n):
    a.append(1.)

b = []
for i in range(0, n):
    b.append(-2.)

c = []
for i in range(0, n - 1):
    c.append(1.)
c.append(cn)

h = x[1] - x[0]
d = []
for i in range(0, n):
    d.append(h ** 2 * f(x[i + 1]))


def PrOgOnKa(a, b, c, d, n):
    y = [0]
    er =[0]
    for i in range(0, n):
        y.append(0)
        er.append(0)
    for i in range(1, n):
        xi = a[i] / b[i - 1]
        a[i] = 0
        b[i] -= xi * c[i - 1]
        d[i] -= xi * d[i - 1]
    y[n - 1] = d[n - 1] / b[n - 1]
    for i in range(n - 2, -1, -1):
        y[i] = 1 / b[i] * (d[i] - c[i] * y[i + 1])
        er[i] =1 / b[i] * (d[i] - c[i] * y[i + 1]) + sin(x[i])
    return [y, er]


plt.subplot(2, 1, 1)
plt.plot(x, PrOgOnKa(a, b, c, d, 200)[0], color='g')
plt.title('Result')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(x, PrOgOnKa(a, b, c, d, 200)[1], color='r')
plt.title('Error')
plt.grid()
plt.show()




