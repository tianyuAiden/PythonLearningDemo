"""
numpy 数组的数学计算
"""
import numpy as np

# 创建一个数组
arr = np.array([1, 2, 3, 4])

# 加法
arr_add = arr + 10
print("加法:", arr_add)

# 乘法
arr_mul = arr * 2
print("乘法:", arr_mul)

# 除法
arr_div = arr / 2
print("除法:", arr_div)
# 创建一个二维数组
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 求和
total_sum = np.sum(arr_2d)
print("总和:", total_sum)

# 均值
mean = np.mean(arr_2d)
print("均值:", mean)

# 标准差
std_dev = np.std(arr_2d)
print("标准差:", std_dev)

# 最大值
max_value = np.max(arr_2d)
print("最大值:", max_value)

# 最小值
min_value = np.min(arr_2d)
print("最小值:", min_value)

"""
标准差
用于衡量一组数据的离散程度。简单来说，标准差越小，数据点就越接近其均值（平均数），反之，标准差越大，数据点的分散程度越大。

计算过程
1.	计算均值：先计算数据集的均值（平均数）。
2.	计算偏差：计算每个数据点与均值的差（偏差）。
3.	平方偏差：将每个偏差平方，以消除负值。
4.	计算方差：求出所有平方偏差的平均值，这个值称为方差。
5.	开平方：最后对方差开平方，得到标准差。

"""
