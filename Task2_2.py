import math
import time

import matplotlib.pyplot as plt
import numpy as np
def func(x,k):
    return math.pi/2-math.atan(math.sqrt(x**2/(k**2-x**2)))-x
#dihotomy
def step_of_dihotomy(func,mass,c):
    if func(mass[0],c)*func((mass[0]+mass[1])/2,c)<=0:
        return [mass[0],(mass[0]+mass[1])/2]
    else:
        return [(mass[0]+mass[1])/2,mass[1]]
def dihotomy(a,U,accurancy,func):
    n=0
    k=math.sqrt(2*U*a**2)
    interval=[0,2]
    fig,axes=plt.subplots(figsize=(10, 10))
    axes.axhline(y=0, color='black')
    axes.grid(True)
    axes.set_ylabel('y',color='black')
    axes.set_xlabel('x',color='black')
    x = np.linspace(0, 2, 1001)
    y = [func(x, k) for x in x]
    axes.plot(x, y, color='red', label='f(x)')
    axes.legend()
    while ((interval[1]-interval[0])>10**(-accurancy)/10):
        axes.axvline(x=interval[0], color='g')
        axes.axvline(x=interval[1], color='b')
        #axes.set_xlim(interval[0], interval[1])
        #axes.set_ylim(func(interval[1],k),func(interval[0],k))
        interval=step_of_dihotomy(func,interval,k)
        n+=1
        #time.sleep(0.5)
        #axes.set_xlim(interval[0],interval[1])
    x0=int(interval[0]*10**(accurancy))/10**(accurancy)
    axes.set_title(f'Dihotomy:\nx = {x0}\nE = {int((-U+((x0)**2)/(2*a**2))*10**(accurancy))/10**(accurancy)}\nn = {n}')
    #plt.show()
def simple_iterations(x0,a,U,accurancy,lamb,func):
    n=0
    N=int(math.log(1/10**(-accurancy))/math.log(1/lamb))
    x=x0
    k=math.sqrt(2*U*a**2)
    fig, axes = plt.subplots(figsize=(10, 10))
    axes.axhline(y=0, color='black')
    axes.grid(True)
    axes.set_ylabel('y', color='black')
    axes.set_xlabel('x', color='black')
    x1 = np.linspace(0, 2, 1001)
    y1 = [func(x, k) for x in x1]
    axes.plot(x1, y1, color='red', label='f(x)')
    axes.legend()
    for i in range(0,N+1):
        x-=-lamb*func(x,k)
        n+=1
        axes.plot(x1,(x1-x)/lamb,color='gray')
        #plt.pause(1)
    xk = int(x * 10 ** (accurancy)) / 10 ** (accurancy)
    axes.set_title(f'SI:\nx = {xk}\nE = {int((-U + ((xk) ** 2) / (2 * a ** 2)) * 10 ** (accurancy)) / 10 ** (accurancy)}\nn = {n}')
    plt.show()
def newtone(x0,a,U,accurancy,func):
    n=0
    x=x0
    k=math.sqrt(2*U*a**2)
    dx=0.00001
    fig, axes = plt.subplots(figsize=(10, 10))
    axes.axhline(y=0, color='black')
    axes.grid(True)
    axes.set_ylabel('y', color='black')
    axes.set_xlabel('x', color='black')
    x1 = np.linspace(0, 2, 1001)
    y1 = [func(x, k) for x in x1]
    axes.plot(x1, y1, color='red', label='f(x)')
    axes.legend()
    while (True):
        if (math.fabs(func(x,k)*dx/(func(x+dx,k)-func(x,k)))<10**(-accurancy-1)):
            break
        else:
            x-=func(x,k)*dx/(func(x+dx,k)-func(x,k))
            n+=1
            axes.plot(x1,(x1-x)*(func(x+dx,k)-func(x,k))/dx,color='gray')
    xk = int(x * 10 ** (accurancy)) / 10 ** (accurancy)
    axes.set_title(f'Newton:\nx = {xk}\nE = {int((-U + ((xk) ** 2) / (2 * a ** 2)) * 10 ** (accurancy)) / 10 ** (accurancy)}\nn = {n}')
    axes.axis([1.5350, 1.5375, -0.025, 0.025])
    plt.show()

dihotomy(10,10,4,func)
newtone(0,10,10,20,func)
simple_iterations(0,10,10,4,0.6,func)



