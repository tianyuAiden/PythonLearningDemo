"""
numpy 线性代数相关操作
"""
import numpy as np

# 创建两个矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. 矩阵乘法
C = A @ B  # 或者使用 np.dot(A, B)
print("矩阵乘法结果:\n", C)

# 2. 矩阵转置
A_transpose = A.T
print("矩阵转置:\n", A_transpose)

# 3. 计算行列式
det_A = np.linalg.det(A)
print("行列式:", det_A)

# 4. 计算逆矩阵
A_inverse = np.linalg.inv(A)
print("逆矩阵:\n", A_inverse)

# 5. 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print("特征值:", eigenvalues)
print("特征向量:\n", eigenvectors)

# 6. 奇异值分解
U, S, Vt = np.linalg.svd(A)
print("U:\n", U)
print("奇异值:\n", S)
print("Vt:\n", Vt)

# 7. QR分解
Q, R = np.linalg.qr(A)
print("Q:\n", Q)
print("R:\n", R)

# 8. 解线性方程组 Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print("解 x:", x)