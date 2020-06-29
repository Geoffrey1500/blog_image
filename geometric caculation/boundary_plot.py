import numpy as np
from matplotlib import pyplot as plt

S = 5000
angular_res = 1/180*np.pi
print(angular_res)
spacing = 200

x = np.arange(-10000, 10001, 1)
y_1 = x*np.sqrt(1 + (x/S)**2)
# print(x, y_1)

y_2 = -x*np.sqrt(1 + (x/S)**2)

# y_3 = np.sqrt(((S**2 + x**2)**1.5 - S**3 - S*x**2)/S)
# print(y[45:56])
# print(y_3)

y_boundary = np.sqrt(spacing*S/angular_res - S**2)
print(y_boundary.shape, x.shape)
xx = np.arange(-y_boundary, y_boundary+1, 1)
y_3 = np.sqrt(((S**2 + xx**2)**1.5 - S**3 - S*xx**2)/S)
# y_4 = np.sqrt((xx**4 - 2*S**4 + (4*S**8 + xx**8 - 2*S**4*xx**4 + 4*S**2*xx**6 + S**6*xx**2)**0.5)/(2*S**2))

z_boundary = np.sqrt(spacing*np.sqrt(S**2 + xx**2)/angular_res - S**2 - xx**2)

# fig_1 = plt.figure()
# plt.scatter(x, y_1, c='r')
# plt.scatter(x, y_2, c='r')
# plt.show()

fig_2 = plt.figure()
plt.scatter(xx, y_3, c='r', s=1)
plt.scatter(xx, -y_3, c='r', s=1)

# plt.scatter(xx, y_4, c='r', s=1)
# plt.scatter(xx, -y_4, c='r', s=1)
# plt.show()

# fig_3 = plt.figure()
plt.scatter(xx, z_boundary, c='b', s=1)
plt.scatter(xx, -z_boundary, c='b', s=1)
# plt.show()

# fig_4 = plt.figure()
xxx = np.arange(-max(z_boundary), max(z_boundary)+1, 1)
plt.scatter(np.expand_dims(y_boundary, 0).repeat(len(xxx), axis=0), xxx, c='black', s=1)
plt.scatter(-np.expand_dims(y_boundary, 0).repeat(len(xxx), axis=0), xxx, c='black', s=1)
plt.show()

# alpha = np.arctan(x[3]/S)
# beta = np.arctan(y_3[3]/S*np.cos(alpha))
#
# cos_2_beta = np.cos(beta)**2
# cos_alpha = np.cos(alpha)
# print(cos_2_beta/cos_alpha)

# alpha_test = np.arccos(np.sqrt(S*angular_res/spacing))
# x_test = S*np.tan(alpha_test)
# print(x_test)


SS = np.arange(0, 41000, 10)
yy_009 = np.sqrt(26*SS/(0.009/180*np.pi) - SS**2)
yy_018 = np.sqrt(26*SS/(0.018/180*np.pi) - SS**2)
yy_036 = np.sqrt(26*SS/(0.036/180*np.pi) - SS**2)
yy_072 = np.sqrt(26*SS/(0.072/180*np.pi) - SS**2)
yy_143 = np.sqrt(26*SS/(0.143/180*np.pi) - SS**2)

print(0.5*26/(0.143/180*np.pi))

fig_5 = plt.figure()
# plt.scatter(SS, yy_009, c='b', s=1)
plt.scatter(SS, yy_018, c='b', s=1)
plt.scatter(SS, yy_036, c='b', s=1)
plt.scatter(SS, yy_072, c='b', s=1)
plt.scatter(SS, yy_143, c='b', s=1)
plt.show()
