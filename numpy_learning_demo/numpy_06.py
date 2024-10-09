"""
NumPy 数组的分割

NumPy 提供了几种方法来分割数组，常用的有
 np.split()
 np.hsplit()
 np.vsplit()
"""

import numpy as np

# 创建两个一维数组
arr_01 = np.array([1, 2, 3])
arr_02 = np.array(([4, 5, 6],[1, 2, 3],[1, 2, 3],[1, 2, 3]))

# 1.np.split() 分割
arr_split = np.split(arr_01, 3)
print(f"arr_split is {arr_split}")

# 2.np.hsplit() 纵向分割
arr_hsplit = np.hsplit(arr_02,3)
print(f"arr_hsplit is {arr_hsplit}")

# 3.横向分割
arr_vsplit = np.vsplit(arr_02,4)
print(f"arr_vsplit is {arr_vsplit}")
