"""
NumPy 数组的组合与分割
时间：10.9
NumPy 提供了几种方式来组合数组，常见的有
np.concatenate()、
np.vstack()（垂直堆叠）
np.hstack()（水平堆叠）。

"""
import numpy as np

# 创建两个一维数组
arr_01 = np.array([1, 2, 3])
arr_02 = np.array([4, 5, 6])

# 1. np.concatenate() 参数 是 元组
arr_concatenate = np.concatenate((arr_01, arr_02))
print(f"arr_concatenate is {arr_concatenate}")  # arr_concatenate is [1 2 3 4 5 6]

# 2. np.vstack() 垂直堆叠 组合成多维数组
arr_vstack = np.vstack((arr_01, arr_02))
print(f"arr_vstack is {arr_vstack}") #[[1 2 3] [4 5 6]]

# 3.np.hstack() 水平堆叠 组合成一维数组
arr_hstack = np.hstack((arr_01, arr_02))
print(f"arr_vstack is {arr_hstack}") #  [1 2 3 4 5 6]