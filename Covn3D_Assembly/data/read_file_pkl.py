import pickle
import csv

# 读取.pkl文件
with open('HA4MAssemblyAction.pkl', 'rb') as f:
    data = pickle.load(f)

# 将数据保存为.txt文件
with open('HA4MAssemblyAction.txt', 'w') as f:
    for value in data:
        f.write(f'{value}\n')

# 将数据保存为.csv文件
with open('HA4MAssemblyAction.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for value in data:
        csv_writer.writerow([value])
