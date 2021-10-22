import numpy as np
import matplotlib.pyplot as plt
from math import *

def func(x):
    return x*(1-x)**2

def K_N(N1,N2,t0,t1,x0,x1):
    deltat=(t1-t0)/N1
    deltax=(x1-x0)/N2
    x=[x0+i*deltax for i in range(0,N2+1)]
    t=[t0+i*deltat for i in range(0,N1+1)]
    A=np.array(np.random.randint(0,1,(N2+1)**2).reshape(N2+1,N2+1))
    q = deltat / (deltax ** 2)
    A[0][0], A[A.shape[0] - 1][A.shape[0] - 1] = 1, 1
    for i in range(1, N2):
        A[i][i] = 1 + q
        A[i][i-1]=-q/2
        A[i][i+1]=-q/2
    U0=np.array([func(x) for x in x]).reshape(N2+1,1)
    U=U0
    T=[]
    T2 = []
    T.append(max(U0)[0])

    fig = plt.figure(figsize=(7, 7))
    ax2 = fig.add_subplot(1, 2, 2)
    plt.grid()

    for i in range(0,len(t)-1):
        B=np.array([0])
        B=np.append(B,[U[i]+((deltat)*(U[i-1]-2*U[i]+U[i+1]))/(2*deltax**2) for i in range(1,len(U)-1)])
        B=np.append(B,[0])
        B1=B.reshape(N2+1,1)
        U = np.linalg.solve(A, B1)
        T.append(max(U)[0])
        if i % 10 ==0:
           ax2.plot(x, U)


    ax1=fig.add_subplot(1, 2, 1)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Tmax')
    plt.plot(t,T, color='g', label='Tmax(t)')
    #plt.plot(t, T2, color='b', label='T2(t)')
    plt.plot(t, [exp(-arg*10 - 2) for arg in t], color='r', label='exp')
    plt.legend()
    ax1.grid(True)
    plt.show()

K_N(1000,100,0,1,0,1)