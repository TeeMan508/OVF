import numpy as np
import matplotlib.pyplot as plt
from math import *
x0 = -2*pi
xn = 2*pi

N = 100
x = np.linspace(x0, xn, N)
h = x[1] - x[0]
A = np.zeros((N, N))

E_main = 10
E = [0.2]
Psi = [[1 for arg in x]]


def U(arg):
    return (arg**2)/2


fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)

A[N-1, N-1] = 1/h**2 + U(x[N-1])
for i in range(1, N):
    A[i-1, i-1] = 1/h**2 + U(x[i-1])
    A[i-1, i] = A[i, i-1] = -1/(2*h**2)
for i in range(1, N):
    if np.linalg.norm(Psi[i-1]) != 0:
        Psi.append(np.linalg.solve(A - E[i-1]*np.eye(N), Psi[i-1]))
        Psi[i] = Psi[i]/np.linalg.norm(Psi[i])
        E.append(E[i-1] + np.linalg.norm(Psi[i-1])/np.linalg.norm(Psi[i]))
        print(E[i])
        if i < 4:
            ax.plot(x, Psi[i], label='Psi' + str(i))
        if E[i] < E_main:
            Psi_main = Psi[i]
            E_main = E[i]
    else:
        N = i
        break

print(E_main)
plt.grid()
plt.legend()
plt.show()





