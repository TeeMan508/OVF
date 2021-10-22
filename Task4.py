import numpy as np
from math import *
import matplotlib.pyplot as plt

def IntegrateLikeSimpson(f, dddf, a, b, accuracy):
   err=[1]
   i = 1
   while err[i-1] > accuracy:
       err.append((-1) * ((b-a)/i)**4 * (1/180) * (dddf(b) - dddf(a)) + ((b-a)/i)**4)
       i += 1
   global dh
   #print(i)
   dh = (-a + b)/(1*i)
   print(dh)
   s = (dh*f(a) + dh*f(b))/3
   for l in range(1, i):
       if l % 2 == 0:
           s += 2 * dh * f(a + dh * l)/3
       else:
           s += 4 * dh * f(a + dh * l)/3
   return s



def J(m, x):
    def f(t):
        return cos(m*t - x*sin(t))/pi
    def dddf(t):
        return (sin(m*t - x*sin(t))*(m - x*cos(t))**3 - 3*x*sin(t)*(m - x*cos(t))*cos(m*t - x*sin(t)) - x*cos(t)*sin(m*t - x*sin(t)))/pi
    return IntegrateLikeSimpson(f, dddf, 0, pi, 1e-17)

#Посчитал проиозводную численно и похавал с точностью 1e-5, будем делать Аналитически
def Jm_derivative(J, m, a, b, x):
    # if x == a:
    #     return (J(m, a + dh*2) - J(m, a))/(dh*2)
    # if x == b:
    #     return (-J(m, b - dh*2) + J(m, b))/(dh*2)
    return (J(m, x+dh) - J(m, x-dh))/(dh*2)



# for x in np.linspace(0, 2*pi, 1000):
#     print(J(1, x) + dJ(0, x))

plt.plot([x for x in np.linspace(0, 2*pi, 10)], [J(1, x) + Jm_derivative(J, 0, 0, 2*pi, x) for x in np.linspace(0, 2*pi, 10)])
plt.grid()
plt.show()

