"""
波士顿房屋价格预测模型
多元线性回归模型制作
时间：20241104
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# 导入数据集
"""
1.读取数据，处理文本格式的分隔符，跳过不需要的前22行，并将结果存储在一个没有自定义列名的DataFrame中
"""
data_url = "/Users/gaotianyu/PycharmProjects/BasicMachineLearning/Linear_Regression_Model/sources/housing-data.csv"
# 直接读取数据，无需行合并
raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=0, header=None)

# 检查数据的形状
print(raw_df.shape)  # 输出行数和列数

# 创建列名
columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 创建DataFrame，方便数据分析和特征处理
boston = pd.DataFrame(raw_df.values, columns=columns)
# print(boston.head())

# print(boston.describe()) # 控制台输出

# 绘制直方图
boston.hist(bins=20, figsize=(20, 15))
# plt.show()

# 绘制各个特征与房价之间的关系
# 设置Matplotlib的全局字体和负号显示
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 将字体设置为SimHei，以便支持中文显示
# plt.rcParams['axes.unicode_minus'] = False  # 避免负号显示成方块，确保图中负号正常显示

# 计算DataFrame的相关矩阵
correlation_matrix = boston.corr()  # 使用DataFrame的corr()方法计算各个特征间的相关系数，生成相关矩阵

# 创建图形并设置尺寸
# plt.figure(figsize=(12, 10))  # 设置图形大小为12x10英寸，以使热图中的各项内容清晰可见

# 使用Seaborn库绘制相关矩阵的热图
sns.heatmap(
    correlation_matrix,  # 传入相关矩阵数据
    annot=True,  # 显示每个单元格中的相关系数数值
    fmt=".2f",  # 设置数值格式为保留两位小数
    cmap="coolwarm"  # 设置颜色映射为coolwarm，便于区分正负相关
)

# 显示图形
# plt.show()  # 展示相关矩阵的热图

# 可视化刚才筛选的相关因素房价关系
warnings.filterwarnings('ignore')

# 异常值处理
boston.boxplot(column=['RM'])
plt.show()
boston.loc[boston['RM'] > 8, 'RM'] = 8
plt.show()
