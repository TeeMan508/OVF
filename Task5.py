import numpy as np
from math import *
import matplotlib.pyplot as plt

n=30
x = [(1+float(k)/n) for k in range(1, n+1)]
y = [log(i) for i in x]
mas = np.array([x, y]).transpose()

#Подсчет разделенных разностей и их запись в матрицу
def a(xy):
    for l in range(1, n+1):
       c = [0*k for k in range(0, l)]
       for i in range(0, len(x)-l):
          c.append((xy[i+l-1, l] - xy[i+l, l]) / (xy[i, 0] - xy[i+l, 0]))
          #print(c, i)
       xy = np.column_stack((xy, np.array(c)))
    return(xy)
#print(a(mas))


#Раскрытие скобок по схеме Горнера
def f(x, mas):
    xy = a(mas)
    res = xy[0,1]
    for i in range(1, n):
        ans = 1
        for j in range(0, i):
            ans *= (x - xy[j, 0])
        res += ans*xy[i,i+1]
    return res


plt.figure(figsize=[10,5])
plt.subplot(1,2,1)
plt.title('P(x)')
plt.grid()
plt.plot([x for x in np.linspace(1.1, 2, 1000)], [f(x, a(mas)) for x in np.linspace(1.1, 2, 1000)], color='green')
plt.scatter(x,y)
plt.subplot(1,2,2)
plt.title('P(x)-log(x)')
plt.grid()
plt.plot([x for x in np.linspace(1.1, 2, 1000)], [(f(x, a(mas)) - log(x)) for x in np.linspace(1.1, 2, 1000)], color='red')
plt.show()










# t1 = np.array([[1, 1, 1, 1], [3, 3, 3, 3]]).transpose()
# t2 = np.array([2, 2, 2, 2])
#
# t = np.column_stack((t1, t2))
# print(np.sum(t))






