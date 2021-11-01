import numpy as np
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
N = 100
const = 0.05
L = 1
t = np.linspace(0, 0.01, N)
x = y = np.linspace(-L, L, N)


def uL(y,t):
    return sin(2*pi*t)


def  MatixOfInitalConditions():
    U = np.zeros((N, N, N))
    for i in range(0, N):
        for j in range(0, N):
            U[i, 0, j] = U[i, N-1, j] = uL(y[j], t[i])
            U[i, j, 0] = U[i, j, N-1] = const
    return U


def TimeFulling(U):
    hx = x[1] - x[0]
    hy = y[1] - y[0]
    ht = t[1] - t[0]
    for i in range(1, N-1):
        for j in range(1, N-1):
            for k in range(0, N-1):
                U[i+1,j,k] = U[i,j,k] * (ht/hx**2) * (U[i,j+1,k] - 2*U[i,j,k] + U[i,j-1,k]) + (ht/(2*hy**2)) * (U[i,j,k+1] - 2*U[i,j,k] + U[i,j,k-1])
    return U


res = TimeFulling(MatixOfInitalConditions())
#print(res[:, 250, 250])
fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, res[49, :, :], cmap='inferno')
plt.grid()
ax2 = fig.add_subplot(122)
ax2.plot(t, res[:, 49, 49], color='r')
#ax2.axis([0.8, 1,-2, 2])
plt.grid()
plt.show()



