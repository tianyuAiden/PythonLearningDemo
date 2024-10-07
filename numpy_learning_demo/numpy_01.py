"""
this is the first numpy learning demo
NumPy 基础 numpy fundamental
author: tianyuAiden
"""
import numpy as np

# numpy创建数组
# 一维数组
array_1d = np.array([1, 2, 3, 4, 5])
print(f"一维数组为{array_1d}")

# 二维数组
array_2d = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
print(f"二维数组为{array_2d}")

# 使用 np.arange() 创建范围数组
array_range = np.arange(10)
print(array_range)

# 使用 np.zeros() 和 np.ones() 创建全零或全一数组
array_zero = np.zeros((2, 3))
print(array_zero)

array_one = np.ones((2, 3))
print(array_one)
