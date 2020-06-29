import shapely.geometry as sp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

w = 30.75
w = w*np.pi/180

rotation_angle_set = []
base_to_depth = []
overlapping_ratio = []

# def over_cal(theta, bd):
for theta in range(0, 60, 1):
    for bd in np.arange(0.6, 2.0, 0.2):
        rotation_A = theta*np.pi/180
        alpha = np.pi/2 - w / 2 - rotation_A
        a_ = 1/np.tan(alpha)
        b_ = 1/np.tan(np.pi-w-alpha)
        if rotation_A < np.pi/2 + w/2 - np.arctan(bd/2):
            if a_ - b_ < bd:
                overlapping = (2*(1/np.tan(alpha)-bd/2))/(1/np.tan(alpha)+1/np.tan(np.pi-w-alpha))
            else:
                overlapping = (2*(1/np.tan(np.pi-w-alpha) + bd/2))/(1/np.tan(alpha)+1/np.tan(np.pi-w-alpha))

            if overlapping > 0.8:
                rotation_angle_set.append(theta)
                base_to_depth.append(bd)
                overlapping_ratio.append(overlapping)

print(len(overlapping_ratio))
