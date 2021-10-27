import numpy as np
from math import *
import matplotlib.pyplot as plt

N = 500


def U(arg):
    return (arg**2)/2


def matrix(X_min, X_max):
    global h, x, A
    x = np.linspace(X_min, X_max, N)
    h = (X_max - X_min)/N
    A = np.zeros((N, N))
    A[N-1, N-1] = 1. + U(x[N-1])*h**2
    for i in range(1, N):
        A[i-1, i-1] = 1. + U(x[i-1])*h**2
        A[i, i-1] = A[i-1, i] = -1./2


def solve(psi0):
    psi = [psi0]
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(1, 1, 1)
    for i in range(1, N):
        psi.append(np.linalg.solve(A, psi[i-1]))
        if i != N-1:
            psi[i] = psi[i] / (np.linalg.norm(psi[i]))
    e = np.linalg.norm(psi[N-2])/np.linalg.norm(psi[N-1])
    print(e/h**2)
    ax.plot(x, psi[N - 1] / np.linalg.norm(psi[N - 1]), label='Psi Main')
    plt.title('E='+str(round(e/h**2, 3)))
    plt.legend()
    plt.grid()
    plt.show()

matrix(-pi,pi)
psi0 = [1/(N**2) for i in range(0, N)]
solve(psi0)


