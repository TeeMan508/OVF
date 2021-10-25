import numpy as np
from math import *
import matplotlib.pyplot as plt

u0, v0 = -2, 1
def F(u, v, t):
    return 998*u + 1998*v

def G(u, v, t):
    return -999*u - 1999*v




def EulerNeYav(a, b):
    N = 100
    u = [u0]
    v = [v0]
    t = np.linspace(a, b, N + 1)
    h = t[1] - t[0]
    for i in range(0, N):
        u.append((1999*u[i]*h+u[i]+1998*v[i]*h)/(1000*h*h+1001*h+1))
        v.append((-999*u[i]*h+v[i]-998*v[i]*h)/(1000*h*h+1001*h+1))
    return [u, v, t]


def EulerYav(F, G, a, b):
    N = 10
    u = [u0]
    v = [v0]
    t = np.linspace(a, b, N + 1)
    h = t[1] - t[0]
    for i in range(0, N):
        u.append(u[i]+h*F(u[i], v[i], t[i]))
        v.append(v[i]+h*G(u[i], v[i], t[i]))
    return [u, v, t]


res = EulerNeYav(0, 3)
ans = EulerYav(F, G, 0, 3)
plt.plot(res[2], res[0], color='b')
plt.plot(res[2], res[1], color='g')
plt.plot(ans[2], ans[0], color='y')
plt.plot(ans[2], ans[1], color='r')
plt.axis([-0.2, 3.3, -2.2, 1.2])
plt.plot()
plt.grid()
plt.show()



