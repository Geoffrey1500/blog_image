import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

S = 5000
angular_res = 0.036/180*np.pi
LoD = 26

i_max = np.arctan(np.sqrt(LoD/(angular_res*S) - 1))/angular_res
print(i_max)

print(S*np.tan(i_max*angular_res), np.sqrt(LoD*S/angular_res - S**2))

j_max = np.arctan(np.sqrt(LoD*np.cos(1*angular_res)/(S*angular_res) - 1))/angular_res
print(j_max)

total_point = 0
for i in range(0, int(i_max), 1):
    j = np.arctan(np.sqrt(LoD*np.cos(i*angular_res)/(S*angular_res) - 1))/angular_res
    total_point += int(j)

print(total_point)

total_point_2 = 0
for i in range(0, int(i_max), 1):
    j_2 = np.arctan(np.sqrt(LoD*(np.cos(i*angular_res))**2/(S*angular_res) - 1))/angular_res
    total_point_2 += int(j_2)
print(total_point_2)
