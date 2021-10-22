import numpy as np

#поиск e и m
e = [np.float32(1.0)]
i = 0
while (np.float32(1)+e[i] != np.float32(1)):
    e.append(np.float32(1 / (2 ** i)))
    i += 1

print('ULP: ' + str(e[i-1]))
print('Число разрядов в мантиссе: ' + str(i-2))

result = 0
for c in range(0, 32-i+1):
    result += 2**c
print('max степень: ' + str(result-127))
print('#############################')

e = [1.0]
i = 0
while (1.0 + e[i] != 1.0):
    e.append(1 / (2 ** i))
    i += 1

print('ULP: ' + str(e[i-1]))
print('число разрядов в мантиссе: ' + str(i-2))

result=0
for c in range(0, 64-i+1):
    result += 2**c
print('max степень: ' + str(result-1023))
print('#############################')

#print('Check: ' + str(np.finfo(float).eps))
#print('#############################')

#сравнение 1, 1+e/2, 1+e, 1+e+e/2
#compare = {'1+e/2': np.float32(1+e[i-1]/2), '1+e': np.float32(1+e[i-1]), '1': np.float32(1), '1+e+e/2': np.float32(1+e[i-1]+e[i-1]/2)}
compare ={'1+e+e/2': 1+e[i-1]+e[i-1]/2, '1+e/2': 1+e[i-1]/2, '1+e': 1+e[i-1], '1': 1.0}
compared_values = sorted(compare.values())
res={}
for l in compared_values:
    for p in compare.keys():
        if compare[p] == l:
            res[p] = compare[p]
print('Числа в порядке возрастания: ' + str(res))



