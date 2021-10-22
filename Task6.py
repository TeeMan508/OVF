from math import *
import numpy as np
import matplotlib.pyplot as plt

N = 10
y0 = 1


def f(x, y):
    return -y


# Да, я не знаю как пишется Эйлер на буржуйском и че?
def Euler(f, a, b):
    y = [y0]
    x = np.linspace(a, b, N + 1)
    h = x[1] - x[0]
    for i in range(0, N):
        y.append(y[i] + h * f(x[i], y[i]))
    return [x, y]


plt.plot(Euler(f, 0, 3)[0], Euler(f, 0, 3)[1], color='r')
plt.plot([x for x in np.linspace(0, 3, N + 1)], [exp(-x) for x in np.linspace(0, 3, N + 1)], color='g')


# Рунге и его лучший друг Кутта(2-ой порядок)

def R_K_2(f, a, b):
    alpha = 3. / 4
    y = [y0]
    x = np.linspace(a, b, N + 1)
    h = x[1] - x[0]
    for i in range(0, N):
        y.append(y[i] + h * ((1 - alpha) * f(x[i], y[i]) + alpha * f(x[i] + h / (2 * alpha), y[i] + f(x[i], y[i]) * h / (2 * alpha))))
    return [x, y]


plt.plot(R_K_2(f, 0, 3)[0], R_K_2(f, 0, 3)[1], color='y', label ='Runge 2')


# Кутта и его лучший друг Рунге(4-ый порядок)

def R_K_4(f, a, b):
    y = [y0]
    x = np.linspace(a, b, N + 1)
    h = x[1] - x[0]
    for i in range(0, N):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + k1 * h / 2)
        k3 = f(x[i] + h / 2, y[i] + k2 * h / 2)
        k4 = f(x[i] + h, y[i] + k3 * h)
        y.append(y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
    return [x, y]


plt.plot(R_K_4(f, 0, 3)[0], R_K_4(f, 0, 3)[1], color='orange', label ='Runge 4')

plt.plot([x for x in np.linspace(0, 3, N + 1)], [exp(-x) for x in np.linspace(0, 3, N + 1)], color='g',  label='exp(x)')
plt.legend()
plt.yscale('log')
plt.grid()
plt.show()
