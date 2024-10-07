"""
NumPy 数组属性
numpy array attribute
"""
import numpy as np

"""
1. 形状（shape）
shape 属性返回数组的形状，即每个维度的大小。它是一个元组，表示数组在每个维度上的元素数量。

2. 维度（ndim）

ndim 属性返回数组的维数（即数组的维度数量）。

3. 数据类型（dtype）

dtype 属性返回数组中元素的数据类型。NumPy 支持多种数据类型，包括整数、浮点数和复数等。

4. 元素数量（size）

size 属性返回数组中元素的总数量。
"""
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])

print(f"array_2d 的形状为 {array_2d.shape}")
print(f"array_1d 的形状为 {array_1d.shape}")

print("------------")
print(f"array_2d 的维度ndim为 {array_2d.ndim}")
print(f"array_1d 的维度ndim为 {array_1d.ndim}")

print("------------")
print(f"array_2d 的数据类型dtype为 {array_2d.dtype}")
print(f"array_1d 的数据类型dtype为 {array_1d.dtype}")

print("------------")
print(f"array_2d 的数量size为 {array_2d.size}")
print(f"array_1d 的数量size为 {array_1d.size}")