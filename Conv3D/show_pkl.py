import pickle

# 读取.pkl文件
with open('UCF101actions.pkl', 'rb') as f:
    data = pickle.load(f)

# 打印数据
print(data)