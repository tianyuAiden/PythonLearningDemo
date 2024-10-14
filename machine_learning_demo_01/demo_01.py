"""
使用numpy实现向量运算
"""
import numpy as np

w = np.array([1.0, 2.5, -3.3])
b = 4
x = np.array([10, 20, 30])

f = np.dot(w, x) + b

print(f"f is {f}")
