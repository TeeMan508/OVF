import numpy as np
from math import *
import matplotlib.pyplot as plt

def IntegrateLikeSimpson(f, dddf, a, b, accuracy):
   err=[1]
   i = 1
   while err[i-1] > accuracy:
       err.append((-1) * ((b-a)/i)**4 * (1/180) * (dddf(b) - dddf(a)) + ((b-a)/i)**4)
       i += 1
   #global dh
   dh = (-a + b)/i
   s = (dh*f(a) + dh*f(b))/3
   for i in range(1, i):
       if i % 2 == 0:
           s += 2 * dh * f(a + dh * i)/3
       else:
           s += 4 * dh * f(a + dh * i)/3
   return s

def IntegrateLikeSimpson2(f, a, b, n):
   dh = (-a + b)/n
   s = (dh*f(a) + dh*f(b))/3
   for i in range(1, n):
       if i % 2 == 0:
           s += 2 * dh * f(a + dh * i)/3
       else:
           s += 4 * dh * f(a + dh * i)/3
   return s


def J(m, x):
    def f(t):
        return cos(m*t - x*sin(t))/pi
    def dddf(t):
        return (sin(m*t - x*sin(t))*(m - x*cos(t))**3 - 3*x*sin(t)*(m - x*cos(t))*cos(m*t - x*sin(t)) - x*cos(t)*sin(m*t - x*sin(t)))/pi
    return IntegrateLikeSimpson2(f, 0, pi, 10**4)

# #Посчитал проиозводную численно и похавал с точностью 1e-5, будем делать Аналитически
# def Jm_derivative(J, m, a, b, x):
#     if x == a:
#         return (J(m, a + dh) - J(m, a))/dh
#     if x == b:
#         return (J(m, b) - J(m, b - dh))/dh
#     return (J(m, x+dh) - J(m, x))/dh

def dJ(m, x):
    def f(t):
        return sin(t)*sin(m*t - x*sin(t))/pi
    return IntegrateLikeSimpson2(f, 0, pi, 10**4)


# for x in np.linspace(0, 2*pi, 1000):
#     print(J(1, x) + dJ(0, x))

plt.plot([x for x in np.linspace(0, 2*pi, 1000)], [J(1, x) + dJ(0, x) for x in np.linspace(0, 2*pi, 1000)])
plt.grid()
plt.show()