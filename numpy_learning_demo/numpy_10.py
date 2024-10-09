"""
数组的复制与视图
"""

# 1.数组的复制
# 复制 会创建一个新的数组，包含原数组的数据，但两者是独立的，即对其中一个数组的修改不会影响另一个数组。
import numpy as np

# 创建一个原数组
original_array = np.array([1, 2, 3, 4, 5])

# 使用 copy() 方法进行复制
copied_array = original_array.copy()

# 修改复制的数组
copied_array[0] = 10

print("原数组:", original_array)  # 输出: [1 2 3 4 5]
print("复制的数组:", copied_array)  # 输出: [10 2 3 4 5]


"""
数组的视图
视图 是对原数组的一个引用，任何对视图的修改都会影响到原数组，反之亦然。视图不会创建新的数组，而是使用原数组的数据。
"""

# 创建一个原数组
original_array = np.array([1, 2, 3, 4, 5])

# 使用视图
view_array = original_array.view()

# 修改视图的数组
view_array[0] = 10

print("原数组:", original_array)  # 输出: [10 2 3 4 5]
print("视图数组:", view_array)     # 输出: [10 2 3 4 5]