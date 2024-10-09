"""
4. NumPy 数组操作
numpy array operation
1. 索引和切片

和 Python 的列表类似，NumPy 数组也支持使用索引和切片来访问和修改数组的元素。

"""

import numpy as np

# 一维数组
array_1d = np.array([10, 20, 30, 40, 50])
print("数组第一个元素:", array_1d[0])  # 访问第一个元素，输出: 10
print("数组最后一个元素:", array_1d[-1])  # 访问最后一个元素，输出: 50

# 二位数组
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("访问第一行第二个元素:", array_2d[0, 1])  # 输出: 2

"""
切片操作 
使用切片操作从数组中提取子数组。
"""
# 提取一维数组的子数组
# [step:start:end]
sub_array_1d = array_1d[1:4]  # 输出: [20, 30, 40]
print(f"sub_array_1d is {sub_array_1d}")
# 提取二维数组的子数组
# [:,1:3] 取所有行的第一列到第三列
sub_array_2d = array_2d[:, 1:3]  # 输出第二列和第三列的子数组: [[2, 3], [5, 6]]
print(f"sub_array_2d is {sub_array_2d}")

"""
2. 数组运算

NumPy 数组支持基本的算术运算，如加法、减法、乘法等，这些操作会逐元素进行。

"""
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# 加法
print("数组相加:", array_1 + array_2)  # 输出: [5 7 9]

# 乘法
print("数组逐元素相乘:", array_1 * array_2)  # 输出: [ 4 10 18]

# 乘以常数
print("数组乘以 2:", array_1 * 2)  # 输出: [2 4 6]

"""
3. 数组的广播

NumPy 支持不同形状的数组进行运算（只要形状是兼容的），这叫做广播。
"""
array_3 = np.array([[1, 2, 3], [4, 5, 6]])

# 与一个常数进行运算，常数会广播到每个元素
print("数组加 10:\n", array_3 + 10)  # 输出: [[11 12 13], [14 15 16]]

# 一维数组和二维数组的广播
array_4 = np.array([1, 0, 1])
print("二维数组与一维数组相加:\n", array_3 + array_4)
# 输出: [[2 2 4], [5 5 7]]

# 初始化数组
# 0-9的平方数组
# [ 0  1  4  9 16 25 36 49 64 81]
array_4 = np.array([i ** 2 for i in range(10)])
print(array_4)
