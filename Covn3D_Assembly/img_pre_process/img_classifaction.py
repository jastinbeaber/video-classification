import os
import shutil
from tqdm import tqdm  # 引入tqdm

# 定义输入文件和文件夹路径
labels_file_path = r'E:\HA4M\IDU001V003\Labels.txt'
images_folder_path = r'E:\HA4M\IDU001V003\video_sq3'

# 定义输出文件夹的根路径
output_root_folder = r'E:\HA4M\action_sq3'

# 获取Labels.txt文件总行数
total_lines = sum(1 for _ in open(labels_file_path, 'r'))

# 读取Labels.txt文件并显示进度条
with open(labels_file_path, 'r') as labels_file:
    for line in tqdm(labels_file, total=total_lines, desc="Processing files"):
        # 解析每一行数据
        elements = line.strip().split()

        # 检查是否有足够的元素
        if len(elements) != 3:
            print(f"Skipping invalid line: {line}")
            continue

        frame_number, action_sequence, is_repeat = map(int, elements)

        # 构建输出文件夹路径
        output_folder_path = os.path.join(output_root_folder, f'action{action_sequence}')

        # 创建输出文件夹（如果不存在）
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        # 构建输入图片路径
        image_file_path = os.path.join(images_folder_path, f'FrameID{frame_number + 1:06d}.png')

        # 检查文件是否存在
        if not os.path.exists(image_file_path):
            print(f"Skipping non-existent file: {image_file_path}")
            continue

        # 构建输出图片路径
        output_image_path = os.path.join(output_folder_path, f'FrameID{frame_number + 1:06d}.png')

        # 将图片复制到对应的输出文件夹
        shutil.copy(image_file_path, output_image_path)

        # 获取当前动作文件夹中的所有图片文件
        image_files = [f for f in os.listdir(output_folder_path) if f.endswith('.png')]

        # 按照帧数大小排序
        image_files.sort(key=lambda x: int(x.split('FrameID')[1].split('.png')[0]))

        # 重命名图片
        for index, image_file in enumerate(image_files, start=1):
            old_path = os.path.join(output_folder_path, image_file)
            new_name = f'FrameID{index:06d}.png'
            new_path = os.path.join(output_folder_path, new_name)
            os.rename(old_path, new_path)

print("图片分类和重命名完成！")
