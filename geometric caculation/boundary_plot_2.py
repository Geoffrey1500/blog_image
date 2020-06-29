import numpy as np
from matplotlib import pyplot as plt

S = 5000
angular_res = 1/180*np.pi
print(S*angular_res)
print(angular_res)
spacing = 500

y_max_1 = np.sqrt(spacing**2/angular_res**2-S**2)
y_max_2 = np.sqrt(spacing**2*S/angular_res**2-S**2)
print(y_max_1, y_max_2)
y = np.arange(-int(min(y_max_1, y_max_2)), int(min(y_max_1, y_max_2))+1, 1)
# y = np.arange(-int(min(y_max_1, y_max_2))+1, int(min(y_max_1, y_max_2)), 1)
y = np.delete(y, int(np.where(y == 0)[0][0]))

# y_3 = np.sqrt(((S**2 + x**2)**1.5 - S**3 - S*x**2)/S)
# print(y[45:56])
# print(y_3)

z_boundary = np.sqrt(spacing*np.sqrt(S**2 + y**2)/angular_res - S**2 - y**2)
print(y.shape, z_boundary.shape)
y_z_b = np.arange(-8150, 8150, 0.1)
z_boundary_new = np.sqrt(spacing*np.sqrt(S**2 + y_z_b**2)/angular_res - S**2 - y_z_b**2)

print("xxx: ", y[np.where(z_boundary == np.max(z_boundary))])
print("xxx: ", y_z_b[np.where(z_boundary_new == np.min(z_boundary_new))])
print("xxx: ", np.sqrt(spacing*S/angular_res - S**2))

y_XX = np.arange(8150, 14001, 0.1)
# y_XX = np.delete(y_XX, int(np.where(y == 0)[0][0]))
y_boundary = np.sqrt(((spacing**2)*(S**2))/((angular_res**2)*(y_XX**2)) - S**4/(y_XX**2) - y_XX**2 - 2*S**2)
print("xxx: ", y_XX[np.where(y_boundary == np.min(y_boundary))])
# y_max = y[np.where(y_boundary == np.min(y_boundary))]
# print(np.min(y_boundary))
# y_new = np.arange(-y_max, y_max, 1)
# y_new = np.delete(y_new, 0)

# z_boundary_new = np.sqrt(spacing*np.sqrt(S**2 + y**2)/angular_res - S**2 - y**2)

# y_3 = np.sqrt(((S**2 + y_z_b**2)**1.5 - S**3 - S*y_z_b**2)/S)
y_boundary_ = np.sqrt(spacing*S/angular_res - S**2)

xx = np.arange(-y_boundary_, y_boundary_+1, 1)

y_3 = np.sqrt(((S**2 + y_z_b**2)**1.5 - S**3 - S*y_z_b**2)/S)

# fig_1 = plt.figure()
# plt.scatter(x, y_1, c='r')
# plt.scatter(x, y_2, c='r')
# plt.show()

fig_2 = plt.figure()
# plt.scatter(y_z_b, y_3, c='r', s=1)
# plt.scatter(y_z_b, -y_3, c='r', s=1)
# plt.show()

# fig_3 = plt.figure()
plt.scatter(y_z_b, z_boundary_new, c='r', s=1)
plt.scatter(y_z_b, -z_boundary_new, c='r', s=1)
# plt.show()

# fig_4 = plt.figure()
# xxx = np.arange(-min(z_boundary), min(z_boundary)+1, 1)
# plt.scatter(np.expand_dims(y_boundary, 0).repeat(len(xxx), axis=0), xxx, c='black', s=1)
# plt.scatter(-np.expand_dims(y_boundary, 0).repeat(len(xxx), axis=0), xxx, c='black', s=1)

plt.scatter(y_XX, y_boundary, c='b', s=1)
plt.scatter(y_XX, -y_boundary, c='b', s=1)
plt.scatter(-y_XX, y_boundary, c='b', s=1)
plt.scatter(-y_XX, -y_boundary, c='b', s=1)
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


# SS = np.arange(1000, 41000, 1000)
# yy_009 = np.sqrt(26*SS/(0.009/180*np.pi) - SS**2)
# yy_018 = np.sqrt(26*SS/(0.018/180*np.pi) - SS**2)
# yy_036 = np.sqrt(26*SS/(0.036/180*np.pi) - SS**2)
# yy_072 = np.sqrt(26*SS/(0.072/180*np.pi) - SS**2)
# yy_143 = np.sqrt(26*SS/(0.143/180*np.pi) - SS**2)
#
# print(0.5*26/(0.143/180*np.pi))
#
# fig_5 = plt.figure()
# plt.scatter(SS, yy_009, c='b')
# plt.scatter(SS, yy_018, c='b')
# plt.scatter(SS, yy_036, c='b')
# plt.scatter(SS, yy_072, c='b')
# plt.scatter(SS, yy_143, c='b')
# plt.show()
