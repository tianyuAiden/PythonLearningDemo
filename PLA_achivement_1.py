import numpy as np

# 感知机算法的实现
class Perceptron:
    def __init__(self, learning_rate=1, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.where(y <= 0, -1, 1)

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = np.sign(linear_output)

                if y_predicted != y_[idx]:
                    self.weights += self.learning_rate * y_[idx] * x_i
                    self.bias += self.learning_rate * y_[idx]

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.sign(linear_output)


# 训练数据 (A, B 为负类，C, D 为正类)
X = np.array([[2, 2], [3, 3], [5, 3], [6, 2]])  # 样本特征
y = np.array([-1, -1, 1, 1])  # 类别标签

# 创建感知机模型，设置学习率和最大迭代次数
perceptron = Perceptron(learning_rate=0.1, n_iters=10)
perceptron.fit(X, y)

# 输出权重和偏置
print(f"权重: {perceptron.weights}")
print(f"偏置: {perceptron.bias}")