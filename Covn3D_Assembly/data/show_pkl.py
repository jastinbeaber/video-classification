import pickle

# 读取.pkl文件
with open('HA4MAssemblyAction.pkl', 'rb') as f:
    data = pickle.load(f)

# 打印数据
print(data)