import numpy as np
from math import *
import matplotlib.pyplot as plt

a0, a1, w0, w1 = 1, 0.002, 5.1, 25.5
period = 2 * pi
N = 100

def getFunc(point):
    return a0 * sin(w0 * point) + a1 * sin(w1 * point)

def windowHanna(k, N):
    return 0.5 * (1 - cos(2 * pi * k / (N - 1)))

def rectangleWindow(k, N):
    return 1

def getFourier(k,window):
    real, complex = 0, 0;
    for i in range(0, N + 1):
        point = period * i / N
        real += getFunc(point) * cos(-2 * pi * i / N) * window(i, N)
        complex += getFunc(point) * sin(-2 * pi * i / N) * window(i, N)
    return sqrt(real**2 + complex**2)

fourier = [getFourier(k, windowHanna) for k in range(0, N + 1)]
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1, 1, 1)
ax.plot([2 * pi * k / period for k in range(0, N + 1)], fourier)
plt.show()