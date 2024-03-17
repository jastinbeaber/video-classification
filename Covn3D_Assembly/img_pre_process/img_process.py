import os


def batch_rename_files(folder_path, new_filename_format):
    # 遍历文件夹中的所有文件
    for count, filename in enumerate(os.listdir(folder_path)):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否是一个普通文件而不是文件夹
        if os.path.isfile(file_path):
            # 构建新的文件名
            new_filename = new_filename_format.format(count + 1, filename)

            # 构建新的文件完整路径
            new_file_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            os.rename(file_path, new_file_path)

    print("文件重命名完成")


# 用法示例
folder_path = 'E:\HA4M\IDU001V003\Color\\000124702712'
new_filename_format = 'FrameID{:06d}.png'  # 例如，new_file_001_oldname.txt

batch_rename_files(folder_path, new_filename_format)
