from math import *
import matplotlib.pyplot as plt

a0, a1, w0, w1, N = 1, 100, 5.1, 25, 100
period = 2*pi
t = [period*i/N for i in range(0, N+1)]


def f(t):
    return a0 * sin(w0 * t) + a1 * sin(w1 * t)


def DumbWindow(k):
    if (k >= 0) and (k < N):
        return 1
    else:
        return 0


def HannWindow(k):
    return 0.5 * (1 - cos(2 * pi * k / (N - 1)))


def fft(t, f, win):
    real, complex, res = [0], [0], [0]
    for i in range(1, N+1):
        realj = 0
        complexj =0
        resj = 0
        for j in range(1, N+1):
            realj += f(t[j-1]) * cos(1 * i * t[j-1]) * win(j-1)
            complexj += f(t[j-1]) * sin(1 * i * t[j-1]) * win(j-1)
        real.append(realj)
        complex.append(complexj)
        resj = real[i] ** 2 + complex[i] ** 2
        res.append(resj)
    return res


fourier1 = fft(t, f, DumbWindow)
fourier2 = fft(t, f, HannWindow)
fig = plt.figure(figsize=(7, 7))
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot([2*pi*j/period for j in range(0, N+1)], fourier1, color='r', label='Rectangle Window')
ax1.plot([2*pi*j/period for j in range(0, N+1)], fourier2, color='g', label='Hann Window')
ax1.set_xlabel('Индекс узла')
ax1.set_ylabel('Спектральная мощность')
plt.title('Task 12')
plt.legend()
plt.grid()
plt.show()
