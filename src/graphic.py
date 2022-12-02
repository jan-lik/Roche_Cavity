import numpy as np
import matplotlib.pyplot as plt
xg = np.array([
            [16, 16, 16, 16, 16, 16, 16],
            [32, 32, 32, 32, 32, 32, 32],
            [64, 64, 64, 64, 64, 64, 64],
            [128, 128, 128, 128, 128, 128, 128]
        ])
yg = ([
            [1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 6, 7],
            [1, 2, 3, 4, 5, 6, 7]
        ])
zg = np.array([
    [550, 700, 650, 550, 300, 100, 5],
    [650, 760, 720, 620, 350, 150, 15],
    [720, 800, 780, 700, 500, 250, 50],
    [580, 690, 600, 550, 250, 50, 5]
])
a = 2
l1_ = 1
fig = plt.figure(figsize=(5, 5))
ax_3d = fig.add_subplot(projection='3d')
#Рисуем все точки, которые относятся к полости Роша
ax_3d.scatter(xg, yg, zg, color='g', s=5)
#Отмечаем первую звезду
ax_3d.scatter(np.array([0]), np.array([0]), np.array([0]), color='r', s=20)
#Отмечаем вторую звезду
ax_3d.scatter(np.array([a]), np.array([0]), np.array([0]), color='b', s=20)
#Отмечаем точку Лагранжа
ax_3d.scatter(np.array([l1_]), np.array([0]), np.array([0]), color='y', s=20)
ax_3d.set_title('Полость Роша')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d.set_xlim([-a, 2 * a])
ax_3d.set_ylim([-a, a])
ax_3d.set_zlim([-a, a])
plt.show()