import numpy as np
import matplotlib.pyplot as plt
from math import *
x0 = -pi*2
xn = pi*2

N = 100
x = np.linspace(x0, xn, N)
h = x[1] - x[0]
A = np.zeros((N, N))

E_main = 10
E = [E_main/10]
Psi = [[1/sqrt(N) for arg in x]]


def U(arg):
    return (arg**2)/2


fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111)
plt.title('Task11')

A[N-1, N-1] = 1/h**2 + U(x[N-1])
for i in range(1, N):
    A[i-1, i-1] = 1/h**2 + U(x[i-1])
    A[i-1, i] = A[i, i-1] = -1/(2*h**2)


for i in range(1, N+1):
    Psi.append(np.linalg.solve(A-E[i-1]*np.eye(N, N), Psi[i-1]))
    E.append(E[i-1] + np.linalg.norm(Psi[i-1])/np.linalg.norm(Psi[i]))
    #print(E[i])
    if i < -1:
        ax.plot(x, Psi[i], label='Psi' + str(i))
    if E[i] < E_main:
        Psi_main = Psi[i]
        E_main = E[i]

print(E_main)
ax.plot(x, Psi_main, color='r', label='PsiMain')
#ax.axis([-3.2, 3.2, 0, 1])
plt.grid()
plt.legend()
plt.show()






