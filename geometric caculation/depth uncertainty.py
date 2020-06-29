import numpy as np
import shapely.geometry as sp
import math
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.frame import DataFrame


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

    # 过相机中心且与像素平面平行的直线方程为：y = kx + d_
    # 像素平面的直线方程为：y = kx + C_
    d_ = center_cor[1] - slope_*center_cor[0]
    if math.pi/2 < slope_ < math.pi:
        C_ = d_ - focal_length*np.sqrt(slope_**2 + 1)
    else:
        C_ = d_ + focal_length * np.sqrt(slope_ ** 2 + 1)

    # 计算ray（光心和坐标原点的连线）与sensor plane的交点
    ray_slope = center_cor[1]/center_cor[0]
    ray_inter_x = C_/(ray_slope - slope_)

    inter_cor_x = list(np.random.normal(ray_inter_x, pixel_size/4, 500))
    # print(ray_inter_x, " ", np.mean(inter_cor_x), " ", np.var(inter_cor_x))
    inter_cor_y = list(map(lambda x: slope_*x + C_, inter_cor_x))
    inter_cor_set = list(zip(inter_cor_x, inter_cor_y))

    return inter_cor_set


def cross_point(line_1, line_2):  # 计算交点函数
    x1, y1, x2, y2 = line_1[0], line_1[1], line_1[2], line_1[3]
    x3, y3, x4, y4 = line_2[0], line_2[1], line_2[2], line_2[3]

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
    center_A = (-20000, 25000)
    center_B = (20000, 25000)

    rotation_A = 30
    rotation_B = -30

    focal_length = 8.8
    sensor_size = 13.2
    pixel_size = sensor_size/5472
    print(pixel_size)
    # 产品型号：精灵Phantom 4 Pro V2.0
    # sensor size = 13.2*8.8 mm
    # maximum resolution = 5472*3648
    fov = (np.arctan(sensor_size / (2 * focal_length)) * 180 / np.pi) * 2
    print("Camera horizontal FoV is:" + str(fov))

    a1, b1 = camera_in_axis(rotation_A, center_A)
    a2, b2 = camera_in_axis(rotation_B, center_B)

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

            error_cor_set = []
            for i in range(len(inter_in_A)):
                # print(i)
                line1 = [center_A[0], center_A[1], inter_in_A[i][0], inter_in_A[i][1]]
                for j in range(len(inter_in_B)):
                    line2 = [center_B[0], center_B[1], inter_in_B[j][0], inter_in_B[j][1]]
                    error_cor_set.append(cross_point(line1, line2))
            error_x = [error_cor_set[i][0] for i in range(len(error_cor_set))]
            error_y = [error_cor_set[i][1] for i in range(len(error_cor_set))]
            print("协标准差矩阵为：\n", np.sqrt(np.cov(error_x, error_y, bias=True)))
            print("相关系数为：\n", np.corrcoef(error_x, error_y))
            cor_set = {"X": error_x,
                       "Y": error_y}
            data_st = DataFrame(cor_set)
            # print(data_st)
            print(np.mean(error_x), np.std(error_x), np.ptp(error_x))
            print(np.mean(error_y), np.std(error_y), np.ptp(error_y))
            # plt.scatter(error_x, error_y, marker = 'x',color = 'red', s = 40 ,label = 'First')
            sns.jointplot(x=data_st['X'], y=data_st['Y'], data=data_st, kind='hex', height=5)
            plt.show()

            sns.set_palette("hls")
            sns.distplot(error_y, color="r", bins=30, kde=True)
            plt.show()
        else:
            print("因为重叠区域不包括 interested point (原点)，所以计算无效")
    else:
        print("他们没有相交，计算无效")
