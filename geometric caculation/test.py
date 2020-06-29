import numpy as np
import matplotlib.pyplot as plt

A, B, C, D = 0, 1, 0, -20000

rotation_speed = 2*np.pi/0.04
sampling_duration = 1/125000

D_0 = 3
divergence = 0.0002
# incidence_angle = np.pi*45/180

alpha = np.pi*45/180
beta = np.pi*30/180
point_X = -D*np.cos(alpha)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))
point_Y = -D*np.sin(alpha)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))
point_Z = -D*np.tan(beta)/(A * np.cos(alpha) + B*np.sin(alpha) + C*np.tan(beta))

point_A = [point_X, point_Y, point_Z]

distance = np.sqrt(point_X**2 + point_Y**2 + point_Z**2)

print("Point_A", point_X, point_Y, point_Z)

point_vector = np.array([point_X, point_Y, point_Z])
normal_vector = np.array([A, B, C])
support_vector = np.array([0, 0, 1])

incidence_angle = np.arccos(np.dot(point_vector, normal_vector)/(np.linalg.norm(point_vector) * np.linalg.norm(normal_vector)))
# print(180*incidence_angle/np.pi)
D_M = D_0 + 2*distance*np.sin(divergence)/(np.cos(2*incidence_angle) + np.cos(divergence))
D_m = D_0 + 2*distance*np.sin(divergence)/(np.cos(incidence_angle) * (1 + np.cos(divergence)))

point_proj_plan = point_vector - (np.dot(point_vector, normal_vector)/np.linalg.norm(normal_vector)**2)*normal_vector
print("point_proj_plan", point_proj_plan)

normal_of_point = np.cross(point_vector, support_vector)
nor_proj_plan = normal_of_point - (np.dot(normal_of_point, normal_vector)/np.linalg.norm(normal_vector)**2)*normal_vector
print("nor_proj_plan", nor_proj_plan)

cross_angle = np.arccos(np.dot(point_proj_plan, nor_proj_plan)/(np.linalg.norm(point_proj_plan) * np.linalg.norm(nor_proj_plan)))
print("xxx is: " + str(cross_angle*180/np.pi))
critical_length_major = D_M*np.cos(cross_angle)
critical_length_minor = D_m*np.sin(cross_angle)
print("xxxxxx " + str(critical_length_major) + ", " + str(critical_length_minor))

D_diver = D_0 + 2*distance*np.tan(divergence/2)

D_rotation = rotation_speed*sampling_duration*distance

print(D_M, D_m)

alpha_ = np.pi*45/180
beta_ = np.pi*30/180 + rotation_speed*sampling_duration
point_X_ = -D*np.cos(alpha_)/(A * np.cos(alpha_) + B*np.sin(alpha_) + C*np.tan(beta_))
point_Y_ = -D*np.sin(alpha_)/(A * np.cos(alpha_) + B*np.sin(alpha_) + C*np.tan(beta_))
point_Z_ = -D*np.tan(beta_)/(A * np.cos(alpha_) + B*np.sin(alpha_) + C*np.tan(beta_))

point_B = [point_X_, point_Y_, point_Z_]

distance = np.sqrt(point_X_**2 + point_Y_**2 + point_Z_**2)

print(point_X_, point_Y_, point_Z_)

point_vector_ = np.array([point_X_, point_Y_, point_Z_])
normal_vector_ = np.array([A, B, C])

incidence_angle_ = np.arccos(np.dot(point_vector_, normal_vector_)/(np.linalg.norm(point_vector_) * np.linalg.norm(normal_vector_)))
print(180*incidence_angle/np.pi, 180*incidence_angle_/np.pi)

D_M_ = D_0 + 2*distance*np.sin(divergence)/(np.cos(2*incidence_angle_) + np.cos(divergence))
D_m_ = D_0 + 2*distance*np.sin(divergence)/(np.cos(incidence_angle_) * (1 + np.cos(divergence)))

print(D_M_, D_m_)
