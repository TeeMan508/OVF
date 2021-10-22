import numpy as np
from scipy import optimize
from math import *
import matplotlib.pyplot as plt

d = 2
U = 6
k0 = sqrt(2*U)
accuracy = 1e-10

def f(x):
    return tan(x*d) - sqrt((k0/x)**2-1)

def df(x):
    return d*(1/sin(x*d)**2)+(k0**2)/((x**3)*sqrt((k0/x)**2-1))

def ddf(x):
    return -2*(d**2)*(1/tan(x*d))*(1/(cos(x*d)**2))-3*(k0**2)/((x**4)*sqrt((k0/x)**2-1)) + (k0**4)/((x**6)*sqrt(((k0/x)**2-1))**3)

print('###################################################################################################################################')



def ICP():
    # if -pi / (2*d) < -k0:
    #     a = -k0
    # else:
    a = pi / (2*d)
    if 3*pi/(2*d) > k0:
        b = k0
    else:
        b = 3*pi / (2*d) + 0.1
    return [a, b]

print(ICP())

#Метод деления отрезка пополам(метод дихотомии)
# a = 2.8 #или 3.4 если нужен следующий корень
# b = 4
a = ICP()[0]
b = ICP()[1]
err = [(b-a)/2]
i = 1
absic1 = [1]
plt.subplot(2, 2, 1)
plt.plot([x for x in np.linspace(0.37, 1.03, 1000)], [f(x) for x in np.linspace(0.37, 1.03, 1000)], color = 'b')
plt.axis([0.37, 1.03, -3200, 1500])
plt.grid()
plt.vlines(a, -5000, 5000, color = 'g')
plt.vlines(b, -5000, 5000, colors='r')
while err[i-1] > accuracy:
   if f((a+b)/2)*f(a) <= 0:
       err.append((b - a) / 2)
       b = ((a+b)/2)
       i += 1
       absic1.append(i)
       plt.vlines(b, -5000, 5000, colors='r')
   else:
       err.append((b - a) / 2)
       a = ((a+b)/2)
       i+= 1
       absic1.append(i)
       plt.vlines(a, -5000, 5000, colors='g')
print('Метод деления отрезка пополам(метод дихотомии)')
print((a+b)/2)
print('Ответ: ' + str(round(U - (((a+b)/2)**2)/2, 10)) +' Количество шагов для необходимой точности 1e-10: ', str(int(i)), ' Значение функции в найденом X: ', str(f((a+b)/2)))
print('###################################################################################################################################')

#Метод простых итераций
x0 = 0.2 #(ICP()[1] + ICP()[0])/2
Y = 0.01
#mindphi= 1-Y*df(optimize.fmin(lambda x: -(1-Y*df(x)), 0.2)[0])
#print(1-Y*df(x0))
def phi(x):
    return x - Y*f(x)
res = [x0, phi(x0), phi(phi(x0))]
i = 2
errr = [1]
absic2 = [1]
#steps = (log(-log(abs(1-Y*df(x0))))-log(accuracy))/(-log(abs(mindphi))) #ошибка в количестве шагов
while ((res[i]-res[i-1])**2)/(abs(2*res[i-1]-res[i]-res[i-2])) > accuracy:
    errr.append(((res[i]-res[i-1])**2)/(abs(2*res[i-1]-res[i]-res[i-2])))
    res.append(phi(res[i]))
    absic2.append(i)
    i += 1
    if 2*res[i-1]-res[i]-res[i-2] == 0:
        break

print('Метод простых итераций')
print(res[i])
print('Ответ: ' + str(round(U - (res[i]**2)/2, 10)) +' Количество шагов для необходимой точности 1e-10: ', str(i-1), ' Значение функции в найденом X: ', str(f(res[i])))
print('###################################################################################################################################')

#Метод Ньютона
x0 = 0.07 #(ICP()[1] + ICP()[0])/2
ans = [x0]
er = [0.01]
i = 1
absic3 = [i]
while abs(er[i-1]) > accuracy/100:
    ans.append(ans[i-1] - f(ans[i-1])/df(ans[i-1]))
    #er.append(er[i-1] + (-er[i-1]*df(ans[i-1])+0.5*ddf(ans[i-1])*(er[i-1]**2))/(df(ans[i-1])-er[i-1]*ddf(ans[i-1])))
    er.append(-0.5 * (er[i-1]**2) * ddf(x0) / df(x0))
    i += 1
    absic3.append(i)
print('Метод Ньютона')
print(ans[i-1])
print('Ответ: ' + str(round(U - (ans[i-1]**2)/2, 10)) + ' Количество шагов для необходимой точности 1e-10: ', str(i-1), ' Значение функции в найденом X: ', str(f(ans[i-1])))
print('###################################################################################################################################')



#Графики
for i in range(2, 4):
    plt.subplot(2,2,i)
    plt.plot([x for x in np.linspace(0.4, 1, 1000)], [f(x) for x in np.linspace(0.4, 1, 1000)])
    plt.grid()
plt.show()






#Дихотомия 2
# a = 2.8 #или 3.4 если нужен следующий корень
# b = 4
# steps = int(log(abs(b-a)/(2*accuracy))/log(2))
# for i in range(1, steps+1):
#    if f((a+b)/2)*f(a) <= 0:
#        b = ((a+b)/2)
#    else:
#        a = ((a+b)/2)
# print('Метод деления отрезка пополам(метод дихотомии)')
# print('Ответ: ' + str(round(U - (((a+b)/2)**2)/2, 10)) +' Количество шагов для необходимой точности 1e-10: ', str(int(steps)), ' Значение функции в найденом X: ', str(f((a+b)/2)))
# print('###################################################################################################################################')







