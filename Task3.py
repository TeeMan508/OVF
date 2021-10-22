from math import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time

def f1(x):
    return 1/(1 + x**2)

def f2(x):
    return x**(1/3) * exp(sin(x))

intervals = [-1, 1, 0, 1]
n = [2**i for i in range(6, 13)]


#Метод трапеций
def trapezoid(n):
   fig = plt.figure(figsize = [10,10])
   ax = fig.add_subplot(111)
   dh1 = (-intervals[0] + intervals[1]) / n
   dh2 = (-intervals[2] + intervals[3]) / n
   s1 = (dh1*f1(intervals[0]) + dh1*f1(intervals[1]))/2
   s2 = (dh2*f2(intervals[2]) + dh1*f2(intervals[3]))/2
   patch = patches.Polygon(xy=list(zip([intervals[3] - dh1 , intervals[3], intervals[3], intervals[3] - dh1], [0, 0, f1(intervals[3]), f1(intervals[3] - dh1)])))
   patch.set_edgecolor('#000000')
   patch.set_facecolor('#98d8f3')
   ax.add_patch(patch)
   for i in range(1, n):
       s1 += dh1 * f1(intervals[0] + dh1 * i)
       s2 += dh2 * f2(intervals[2] + dh2 * i)
       patch = patches.Polygon(xy = list(zip([intervals[0] + dh1 * (i-1), intervals[0] + dh1 * i, intervals[0] + dh1 * i, intervals[0] + dh1 * (i-1)], [0, 0, f1(intervals[0] + dh1 * i), f1(intervals[0] + dh1 * (i-1))])))
       patch.set_edgecolor('#000000')
       patch.set_facecolor('#98d8f3')
       ax.add_patch(patch)
   ax.plot(np.linspace(-1, 1, 1000), [f1(i) for i in np.linspace(-1, 1, 1000)], color='r')
   plt.title('N=' + str(n))
   plt.show()
   print('trapezoid', s1, s2)
   return [s1, s2]



#Метод жёлтого семьянина, который работает на АЭС
def simpson(n):
   dh1 = (-intervals[0] + intervals[1]) / n
   dh2 = (-intervals[2] + intervals[3]) / n
   s1 = (dh1*f1(intervals[0]) + dh1*f1(intervals[1]))/3
   s2 = (dh2*f2(intervals[2]) + dh1*f2(intervals[3]))/3
   for i in range(1, n):
       if i % 2 == 0:
           s1 += 2*dh1*f1(intervals[0] + dh1*i)/3
           s2 += 2*dh2*f2(intervals[2] + dh2*i)/3
       else:
           s1 += 4 * dh1 * f1(intervals[0] + dh1 * i) / 3
           s2 += 4 * dh2 * f2(intervals[2] + dh2 * i) / 3
   print('simpson', s1, s2)
   return  [s1, s2]

#Да, main из 4-х строк и че ты мне сделаешь?
sim = []
tr = []
for i in n:
    sim.append(simpson(i)[0] - pi/2)
    tr.append(abs(trapezoid(i)[0] - pi/2))
    #time.sleep(1)

plt.plot(n, tr, color='g')
# plt.plot(n, sim, color='b')
plt.yscale('log')
# plt.axis([-10, 4500, 10**(-16), 10**(0)])
plt.grid()
plt.show()



