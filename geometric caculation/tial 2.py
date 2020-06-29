# This version is not accurate as last version

import numpy as np
import shapely.geometry as sp
import math


def camera_in_axis(sensor_slope, center_cor):
    slope_ = sensor_slope * np.pi / 180
    fov_ = fov * np.pi / 180

    k_right = np.tan(-(np.pi - fov_)/2 + slope_)
    b_right = center_cor[1] - k_right * center_cor[0]
    x_intersection_right = -b_right/k_right

    k_left = np.tan(-(np.pi - fov_)/2 - fov_ + slope_)
    b_left = center_cor[1] - k_left * center_cor[0]
    x_intersection_left = -b_left/k_left

    return x_intersection_left, x_intersection_right


def sensor_plane_inter(sensor_slope, center_cor):
    slope_ = sensor_slope * np.pi / 180
    fov_ = fov * np.pi / 180

    # 过相机中心且与像素平面平行的直线方程为：y = kx + d_
    # 像素平面的直线方程为：y = kx + C_
    d_ = center_cor[1] - slope_*center_cor[0]
    if math.pi/2 < slope_ < math.pi:
        C_ = d_ - focal_length * np.sqrt(slope_**2 + 1)
    else:
        C_ = d_ + focal_length * np.sqrt(slope_**2 + 1)

    # 求fov右边界与sensor plane的交点坐标（x_intersection_right， y_intersection_right）
    k_right = np.tan(-(np.pi - fov_)/2 + slope_)
    b_right = center_cor[1] - k_right * center_cor[0]
    x_intersection_right = (C_ - b_right)/(-slope_ + k_right)
    y_intersection_right = slope_*x_intersection_right + C_

    # 求fov左边界与sensor plane的交点坐标（x_intersection_left， y_intersection_left）
    k_left = np.tan(-(np.pi - fov_)/2 - fov_ + slope_)
    b_left = center_cor[1] - k_left * center_cor[0]
    x_intersection_left = (C_ - b_left)/(-slope_ + k_left)
    y_intersection_left = slope_*x_intersection_left + C_

    # 计算ray（光心和坐标原点的连线）与 sensor plane的交点
    ray_slope = center_cor[1]/center_cor[0]
    ray_inter_x = C_/(ray_slope - slope_)
    ray_inter_y = ray_slope*ray_inter_x

    # 计算ray所属的pixel左右端点及其坐标
    x_left = ((ray_inter_x - x_intersection_left)//pixel_size) * pixel_size + x_intersection_left
    y_left = slope_ * x_left + C_
    x_right = ((ray_inter_x - x_intersection_left)//pixel_size + 1) * pixel_size + x_intersection_left
    y_right = slope_ * x_right + C_

    print((y_intersection_right - y_intersection_left) / (x_intersection_right - x_intersection_left), slope_,
          (y_right - y_left) / (x_right - x_left))

    inter_cor_set = [(x_left, y_left), (x_right, y_right)]
    # print(((ray_inter_x - x_intersection_left)//pixel_size))

    # print(x_left, ray_inter_x, x_right)
    # print([(x_left, y_left), (x_right, y_right)])

    sensor_line = sp.LineString([(x_intersection_right, y_intersection_right),
                                 (x_intersection_left, y_intersection_left)])
    inter_circle = sp.Point(ray_inter_x, ray_inter_y).buffer(pixel_size/2)
    inter_region = inter_circle.intersection(sensor_line)
    inter_cor_set_2 = list(inter_region.coords)
    print(inter_cor_set)
    print(inter_cor_set_2)
    print(np.sqrt((inter_cor_set[0][0] - inter_cor_set[1][0])**2 + (inter_cor_set[0][1] - inter_cor_set[1][1])**2))
    print(np.sqrt((inter_cor_set_2[0][0] - inter_cor_set_2[1][0])**2 + (inter_cor_set_2[0][1] - inter_cor_set_2[1][1])**2))
    print(pixel_size)

    return inter_cor_set


def cross_point(line_1, line_2):  # 计算交点函数
    x1 = line_1[0]
    y1 = line_1[1]
    x2 = line_1[2]
    y2 = line_1[3]

    x3 = line_2[0]
    y3 = line_2[1]
    x4 = line_2[2]
    y4 = line_2[3]

    k1 = (y2 - y1) * 1.0 / (x2 - x1)  # 计算k1,由于点均为整数，需要进行浮点数转化
    b1 = y1 * 1.0 - x1 * k1 * 1.0  # 整型转浮点型是关键
    if (x4 - x3) == 0:  # L2直线斜率不存在操作
        k2 = None
        b2 = 0
    else:
        k2 = (y4 - y3) * 1.0 / (x4 - x3)  # 斜率存在操作
        b2 = y3 * 1.0 - x3 * k2 * 1.0
    if k2 == None:
        x = x3
    else:
        x = (b2 - b1) * 1.0 / (k1 - k2)
    y = k1 * x * 1.0 + b1 * 1.0
    return x, y


if __name__ == '__main__':
    center_A = (-2000, 10000)
    center_B = (2000, 10000)

    rotation_A = 20
    rotation_B = -20

    focal_length = 24
    sensor_size = 13.2
    resolution = [5472, 3648]
    pixel_size = sensor_size/resolution[0]
    print(pixel_size)
    # 产品型号：精灵Phantom 4 Pro V2.0
    # sensor size = 12.8*9.6 mm 或者很有可能是 13.2*8.8 mm
    # maximum resolution = 5472*3648
    fov = (np.arctan(sensor_size / (2 * focal_length)) * 180 / np.pi) * 2
    print("Camera horizontal FoV is:" + str(fov))

    a1, b1 = camera_in_axis(rotation_A, center_A)
    a2, b2 = camera_in_axis(rotation_B, center_B)
    print(a1, b1)
    print(a2, b2)

    A_ = sp.LineString([(a1, 0), (b1, 0)])
    B_ = sp.LineString([(a2, 0), (b2, 0)])

    overlap_region = A_.intersection(B_).bounds

    if overlap_region:

        print("重叠区域左端点为：" + str(overlap_region[0]))
        print("重叠区域右端点为：" + str(overlap_region[2]))

        if overlap_region[0] < 0 < overlap_region[2]:
            overlap_range = abs(overlap_region[2] - overlap_region[0])
            overlap_ratio = overlap_range/abs(a1 - b1)
            print("Overlap ratio is: " + str(overlap_ratio))
            inter_in_A = sensor_plane_inter(rotation_A, center_A)
            inter_in_B = sensor_plane_inter(rotation_B, center_B)

            line1 = [center_A[0], center_A[1], inter_in_A[0][0], inter_in_A[0][1]]
            line2 = [center_A[0], center_A[1], inter_in_A[1][0], inter_in_A[1][1]]

            line3 = [center_B[0], center_B[1], inter_in_B[0][0], inter_in_B[0][1]]
            line4 = [center_B[0], center_B[1], inter_in_B[1][0], inter_in_B[1][1]]

            inter_polygon = sp.Polygon([cross_point(line1, line3), cross_point(line1, line4),
                                        cross_point(line2, line3), cross_point(line2, line4)])

            error_in_x = abs(inter_polygon.bounds[2] - inter_polygon.bounds[0])
            error_in_y = abs(inter_polygon.bounds[3] - inter_polygon.bounds[1])

            print("Depth error is: " + str(error_in_y) + "mm")
            print("Horizontal error is: " + str(error_in_x) + "mm")
        else:
            print("因为重叠区域不包括 interested point (原点)，所以计算无效")
    else:
        print("他们没有相交，计算无效")
