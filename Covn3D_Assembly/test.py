import numpy as np

# 创建一个一维数组
arr1 = np.array([1, 2, 3, 4, 5])

# 创建一个二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 打印数组
print("一维数组:")
print(arr1)

print("\n二维数组:")
print(arr2)

# 数组形状
print("\n数组形状:")
print(arr1.shape)  # 一维数组的形状
print(arr2.shape)  # 二维数组的形状

# 数组运算
print("\n数组运算:")
sum_arr1 = np.sum(arr1)
sum_arr2 = np.sum(arr2, axis=0)  # 沿着列相加
print("一维数组求和:", sum_arr1)
print("二维数组每列求和:", sum_arr2)

# 其他数学运算
print("\n其他数学运算:")
sqrt_arr1 = np.sqrt(arr1)
exp_arr2 = np.exp(arr2)
print("一维数组平方根:", sqrt_arr1)
print("二维数组指数运算:", exp_arr2)
