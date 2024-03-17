import pickle
import csv

# 读取.pkl文件
with open('UCF101_videos_prediction.pkl', 'rb') as f:
    data = pickle.load(f)

# 将数据保存为.txt文件
with open('UCF101_videos_prediction.txt', 'w') as f:
    for item in data:
        f.write(str(item) + '\n')

# 将数据保存为.csv文件
with open('UCF101_videos_prediction.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for row in data:
        csv_writer.writerow(row)
