# import numpy as np

# array1 = np.array([[4,8,12],[3,6,9],[5,6,7]])
# array2 = np.array([[1,1,2],[2,4,4],[4,3,8]])
# a = np.inner(array1,array2)  	#矩阵内积
# c = np.dot(array1,array2)   	#矩阵相乘

# print('X ∙ Y = ',a)
# print('XY = ' ,c) 
# 
# 
# 
# 
# 
import pandas as pd
from io import StringIO

from sklearn import linear_model

import matplotlib.pyplot as plt



# 房屋面积与价格历史数据(csv文件)
csv_data = 'T,pro\n-3.2,20\n10,239\n0,10\n10,241\n-5,44\n-8,115\n5,75\n'

# 读入dataframe
df = pd.read_csv(StringIO(csv_data))
print(df)


# 建立线性回归模型
regr = linear_model.LinearRegression()

# 拟合
regr.fit(df['T'].reshape(-1, 1), df['pro']) # 注意此处.reshape(-1, 1)，因为X是一维的！

# 不难得到直线的斜率、截距
a, b = regr.coef_, regr.intercept_

# 方式1：根据直线方程计算的价格
print(a * 4 + b)

# 方式2：根据predict方法预测的价格
print(regr.predict(4))

# 画图
# 1.真实的点
plt.scatter(df['T'], df['pro'], color='blue')

# 2.拟合的直线
plt.plot(df['T'], regr.predict(df['T'].reshape(-1,1)), color='red', linewidth=4)

plt.show()