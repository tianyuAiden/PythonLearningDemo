"""
NumPy 的随机数生成

NumPy 提供了 numpy.random 模块来生成随机数。你可以生成不同类型的随机数，包括：

•	均匀分布的随机数
•	正态分布的随机数
•	整数随机数
•	从给定数组中随机选择元素
"""

import numpy as np

# 生成 5 个均匀分布的随机数，范围在 [0, 1) 默认生成该范围，如果想生成其他范围则
#

random_uniform = np.random.rand(5)
print("均匀分布随机数:", random_uniform)

#  {random_number} = a + (b - a) *{random_value}
# 生成 5 个均匀分布的随机数，范围在 [2, 5)
a = 2
b = 5
random_uniform_custom_range = a + (b - a) * np.random.rand(5)
print("范围在 [2, 5) 的均匀分布随机数:", random_uniform_custom_range)

# 生成 5 个正态分布的随机数，均值为 0，标准差为 1
random_normal = np.random.randn(5)
print("正态分布随机数:", random_normal)


# 生成 5 个在 [1, 10) 范围内的随机整数
random_integers = np.random.randint(1, 10, size=5)
print("随机整数:", random_integers)

# 从给定数组中随机选择 3 个元素 会重复
array = np.array([10, 20, 30, 40, 50])
random_choice = np.random.choice(array, size=3)
print("随机选择的元素:", random_choice)