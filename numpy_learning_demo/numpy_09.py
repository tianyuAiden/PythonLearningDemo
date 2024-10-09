"""
计算满足条件的元素个数

假设我们有一个 NumPy 数组，我们想计算数组中大于某个特定值的元素个数
"""
import numpy as np

# 创建一个数组
arr = np.array([1, 5, 8, 12, 4, 7, 9])

# 计算大于 5 的元素个数
count_greater_than_5 = np.sum(arr > 5)
print("大于 5 的元素个数:", count_greater_than_5)


# 计算大于 5 的元素个数
count_greater_than_5 = np.count_nonzero(arr > 5)
print("大于 5 的元素个数:", count_greater_than_5)