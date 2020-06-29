import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 设平面方程为： Ax + By + Cz + D = 0

A, B, C, D = 1, 0, 0, -5000

angular_res = 3/180*np.pi

Y_up, Y_low = 10000, -10000
Z_up, Z_low = 10000, -10000

angular_sup = 86/180*np.pi
up_part = -D*angular_res

i_up, i_low = np.arctan(Y_up/-D)//angular_res + 2, np.arctan(Y_low/-D)//angular_res
j_up, j_low = angular_sup//angular_res + 2, -angular_sup//angular_res

X, Y, Z = [], [], []
S_y, S_z = [], []
D_s = []
S_fi = []

for i in range(int(i_low), int(i_up)):
    tan_i = np.tan(i * angular_res)
    cos_i = np.cos(i * angular_res)
    sin_i = np.sin(i * angular_res)

    x = -D
    y = -D * tan_i

    for j in range(int(j_low), int(j_up)):
        tan_j = np.tan(j*angular_res)
        cos_j = np.cos(j*angular_res)

        z = -D*tan_j/cos_i

        if Z_low <= z <= Z_up:
            s_y = 1/(up_part/cos_i**2)
            s_y_2 = 1/(up_part/cos_i**2)*np.sqrt(1 + tan_j**2*sin_i**2)
            s_z = 1/(up_part/(cos_i * cos_j**2))
            # s_fin = min(s_y, s_z)
            s_fin = min(s_y_2, s_z)

            X.append(x)
            Y.append(y)
            Z.append(z)

            S_y.append(s_y)
            S_z.append(s_z)
            D_s.append(s_y_2)
            S_fi.append(s_fin)

# print(len(S_y), len(S_z))
# print(S_z[0:21])
fig = plt.figure()
ax = Axes3D(fig)

# a = np.array(Y)
# b = np.array(Z)
# print(a[0:20], b[0:20])
# print(len(set(a)), len(set(b)))
# print(len(a), len(b))
# c = np.array(S_fi).reshape([len(Y), len(Z)])
# a, b = np.meshgrid(a, b)
# ax.plot_surface(a, b, c, rstride=1, cstride=1, cmap='rainbow')

# ax.scatter(X, Y, Z, c='r')
# ax.scatter(Y, Z, S_y, c='b')
# ax.scatter(Y, Z, S_z, c='r')
ax.scatter(Y, Z, S_fi, c='r')


fig2 = plt.figure()
# plt.scatter(Y[1000:-1000], Z[1000:-1000], c='r', s=1)
plt.scatter(Y, Z, c='r', s=100, marker='*')
plt.show()
