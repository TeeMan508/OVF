import numpy as np
import matplotlib.pyplot as plt
from math import *

N = 100
y0 = x0 = 5
a, b, c, d = 7, 1, 3, 9
t1, t2 = 0, 5
def f1(x, y, t):
    return a*x - b*x*y

def f2(x, y, t):
    return c*x*y - d*y

def R_K_2(f1, f2, t1, t2):
    alpha = 3./4
    x = [x0]
    y = [y0]
    t = np.linspace(t1, t2, N + 1)
    h = t[1] - t[0]
    for i in range(0, N):
        x.append(x[i] + h*((1 - alpha)*f1(x[i], y[i], t[i]) + alpha*f1(x[i]+f1(x[i], y[i], t[i])*h/(2*alpha), y[i] + f2(x[i], y[i], t[i])*h/(2*alpha), t[i]+ h/(3*alpha))))
        y.append(y[i] + h*((1 - alpha)*f2(x[i], y[i], t[i]) + alpha*f2(x[i]+f1(x[i], y[i], t[i])*h/(2*alpha), y[i] + f2(x[i], y[i], t[i])*h/(2*alpha), t[i]+ h/(3*alpha))))
    return [x, y, t]


res = R_K_2(f1, f2, t1, t2)

plt.subplot(121)
plt.plot(res[0], res[1], color='r')
plt.subplot(122)
plt.plot(res[2], res[0], color='g')
plt.plot(res[2], res[1], color='b')
plt.grid()
plt.show()