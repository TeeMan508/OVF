from math import *
import numpy as np
import matplotlib.pyplot as plt

y0 = 1
yn = 10
N = 1000
x0 = 0
xn = 2*pi
x = np.linspace(x0, xn, N)
h = x[1] - x[0]

def f(x):
    return sin(x)


A = np.zeros((N, N))
A[0, 0] = -2/h**2
A[N-1, N-1] = -2/h**2
A[0, 1] = 1/h**2
A[1, 0] = 1/h**2
A[0, N-1] = 0 #y0/h**2
A[N-1, 0] = 0 #yn/h**2
for i in range(2, N):
    A[i-1, i-1] = -2/h**2
    A[i, i-1] = A[i-1, i] = 1/h**2


d = np.array([f(arg) for arg in x])
d[0] = d[0] - y0/h**2
d[N-1] = d[N-1] - yn/h**2
B = A[0:-1, 0:-1]
D = d[0:-1]
U = A[0:N-1, N-1]
V = A[N-1, 0:N-1]
p = np.linalg.solve(B, D)
q = np.linalg.solve(B, -U)

y_n = (d[N-1]-np.dot(V, p))/(A[N-1, N-1] + np.dot(V, q))

y = p + y_n * q

res = np.insert(y, N-1, y_n)
print(res.shape)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, res, color='r')
plt.grid()
plt.show()






