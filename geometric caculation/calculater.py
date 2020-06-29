import numpy as np
import matplotlib.pyplot as plt

A, B, C, D = 0, 1, 0, -100000
normal_vector = np.array([A, B, C])
support_vector = np.array([0, 0, 1])

rotation_speed = 2*np.pi/0.04
sampling_duration = 1/125000

D_0 = 3.5
divergence = 0.0003
# incidence_angle = np.pi*45/180


def point(alpha, beta):
    x = -D*np.cos(alpha)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))
    y = -D*np.sin(alpha)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))
    z = -D*np.tan(beta)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))

    return np.array([x, y, z])


def axi_length(point_cor):
    distance = np.linalg.norm(point_cor) + (D_0/2)/np.tan(divergence/2)
    incidence_angle = np.arccos(np.dot(point_cor, normal_vector)/(np.linalg.norm(point_cor) * np.linalg.norm(normal_vector)))
    print(distance, incidence_angle*180/np.pi)

    if incidence_angle > np.pi/2:
        incidence_angle = np.pi - incidence_angle

    D_1 = 2*distance*(np.sin(divergence)*np.cos(incidence_angle))/(np.cos(2*incidence_angle) + np.cos(divergence))
    D_2 = np.sqrt(1 - (np.sin(incidence_angle)/np.cos(divergence/2))**2) * D_1
    print(np.sqrt(1 - (np.sin(incidence_angle)/np.cos(divergence/2))**2))
    # print(incidence_angle)
    # print(divergence)
    # print(np.cos(incidence_angle)/np.cos(divergence))
    # print(D_2)

    D_M = max(D_1, D_2)
    D_m = min(D_1, D_2)

    point_proj_plan = point_cor - (np.dot(point_cor, normal_vector)/np.linalg.norm(normal_vector)**2)*normal_vector

    normal_of_point = np.cross(point_cor, support_vector)
    nor_proj_plan = normal_of_point - (np.dot(normal_of_point, normal_vector) / np.linalg.norm(normal_vector) ** 2) * normal_vector

    cross_angle = np.arccos(
        np.dot(point_proj_plan, nor_proj_plan) / (np.linalg.norm(point_proj_plan) * np.linalg.norm(nor_proj_plan)))

    if cross_angle > np.pi/2:
        cross_angle = np.pi - cross_angle

    D_M_proj = D_M*np.cos(cross_angle)
    D_m_proj = D_m*np.sin(cross_angle)

    sampling_length = rotation_speed * sampling_duration * distance

    return [sampling_length, D_M/2, D_m/2, D_M_proj/2, D_m_proj/2, incidence_angle*180/np.pi, cross_angle*180/np.pi]


alpha_A = np.pi*30/180
beta_A = np.pi*30/180

point_A = point(alpha_A, beta_A)
print(point_A, np.linalg.norm(point_A))

cont_A = axi_length(point_A)
print(cont_A)

alpha_B = np.pi*90/180
beta_B = np.pi*0/180

point_B = point(alpha_B, beta_B)
print(point_B, np.linalg.norm(point_B))

cont_B = axi_length(point_B)
print(cont_B)
