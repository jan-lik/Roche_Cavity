import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import solve, Symbol

def volume_counter(lobe, l1, limit, step):
    counter = 0
    for x in range(int(limit / step / 3), int((l1 + limit) / step)):
        for y in lobe[x]:
            for el in y:
                if el > 0:
                    counter += 1
    return counter / (limit / step) ** 3

print('Масса первой звезды в массах Солнца')
m1 = float(input())
print('Масса второй звезды в массах Солнца')
m2 = float(input())
print('Большая полуось системы в а.е.')
a = float(input())

m1s = np.arange(1, 100, 20)
m2s = np.arange(1, 100, 20)
a_s = np.arange(1, 6, 1)
ans = [[],[],[],[]]
_ = 1
for m1_ in m1s:
    for m2_ in m2s:
        for a_ in a_s:
            #print(_)
            limit = a_
            step = 0.05
            lobe, xg, yg, zg, l1_ = lobe_(m1_, m2_, float(a_), limit, step)
            #volume = volume_counter(lobe, l1_, limit, step)
            ans[0].append(m1_)
            ans[1].append(m2_)
            ans[2].append(a_)
            #ans[3].append(volume)
            _ += 1


n = m1 / m2

limit = a
step = 0.1

lobe, xg, yg, zg, l1_ = lobe_(m1, m2, float(a), limit, step)

#volume = volume_counter(lobe, l1_, limit, step)
#print(volume)
#print(ans)

model(m1, m2, a, limit, step)