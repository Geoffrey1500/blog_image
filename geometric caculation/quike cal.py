import numpy as np

D_0 = 3.5
distance = 50000

divergence = 0.00023
radius = D_0/2 + distance*np.tan(divergence/2)

normal_vector = np.array([0, 80000, 0])
point_cor = np.array([40000, 40000, 56568.5425])

incidence_angle = np.arccos(np.dot(point_cor, normal_vector)/(np.linalg.norm(point_cor) * np.linalg.norm(normal_vector)))

distance_2 = np.linalg.norm(point_cor) + (D_0/2)/np.tan(divergence/2)
radius_2 = distance_2*np.tan(divergence/2)

print(radius, radius_2)
print(incidence_angle*180/np.pi)

print(distance_2)

c = D_0 * ((np.sin(divergence)*np.cos(incidence_angle))/(np.cos(2*incidence_angle) + np.cos(divergence)))/np.tan(divergence/2)

print(c)
