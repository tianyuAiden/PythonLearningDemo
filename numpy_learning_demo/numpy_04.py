"""
数组的高级操作
numpy advance operations
numpy array's shape change
"""

# 数组的形状变换

"""
NumPy 提供了一些方法来改变数组的形状，常见的操作包括 reshape()、flatten() 和 transpose()。
"""

import numpy as np

# 创建一个 1D 数组
array = np.arange(12)
print("原数组:", array)

# 重塑为 3x4 的 2D 数组
reshaped_array = array.reshape((3, 4))
print("重塑后的数组:\n", reshaped_array)
reshaped_array = reshaped_array.reshape((2, 6))
# 重塑后的数组的元素数量必须和之前相等，否则会报错
print(reshaped_array)


# 展平数组 flatten
flattened_array = reshaped_array.flatten()
print("展平后的数组:", flattened_array)

"""
transpose()：数组的转置
transpose() 可以对二维数组进行转置操作，将行变为列，列变为行。
2行6列变为6行2列
"""
transpose_array = reshaped_array.transpose()
print(f"transpose_array is {transpose_array}")