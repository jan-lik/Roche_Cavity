import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import solve, Symbol

def model(m1, m2, a, limit, step):
    #''' рисуем модель полости по полученным данным'''
    lobe, xg, yg, zg, l1_ = lobe_for_model(m1, m2, float(a), limit, step)
    fig = plt.figure(figsize=(5, 5))
    ax_3d = Axes3D(fig)
    ax_3d.scatter(xg, yg, zg, color='turquoise', alpha=0.1)
    #ПОПЫТКА СДЕЛАТЬ КАРКАСНУЮ СЕТКУ
    xgg = []
    ygg = []
    zgg = []
    for i in range(len(xg)):
        if (-0.01 < xg[i] < 0.01) or (-0.21 < xg[i] < -0.19) or (-0.41 < xg[i] < -0.39) or (-0.81 < xg[i] < -0.79) or (0.21 > xg[i] >0.19) or (0.41 > xg[i] >0.39) or (0.81 >xg[i] >0.79):
            xgg.append(xg[i])
            ygg.append(yg[i])
            zgg.append(zg[i])
    for i in range(len(xg)):
        if (-0.01 < yg[i] < 0.01) or (-0.21 < yg[i] < -0.19) or (-0.41 < yg[i] < -0.39) or (-0.81 < yg[i] < -0.79) or (0.21 > yg[i] >0.19) or (0.41 > yg[i] >0.39) or (0.81 >yg[i] >0.79):
            xgg.append(xg[i])
            ygg.append(yg[i])
            zgg.append(zg[i])
    ax_3d.scatter(xgg, ygg, zgg, color='g')
    '''
    ax_3d.scatter(np.array([0]), np.array([0]), np.array([0]), color='r', s=20)
    ax_3d.scatter(np.array([a]), np.array([0]), np.array([0]), color='b', s=20)
    ax_3d.scatter(np.array([l1_]), np.array([0]), np.array([0]), color='y', s=20)
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    ax_3d.set_xlim([-a, a])
    ax_3d.set_ylim([-a, a])
    ax_3d.set_zlim([-a, a])
    plt.show()