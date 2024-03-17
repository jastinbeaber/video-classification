import os
import shutil

def organize_images_in_folders(parent_folder):
    # 获取父文件夹中的所有子文件夹
    folders = [folder for folder in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, folder))]

    for folder in folders:
        # 构建源文件夹路径和目标文件夹路径
        source_folder_path = os.path.join(parent_folder, folder)
        target_folder_path = os.path.join(source_folder_path, "video1")

        # 创建目标文件夹
        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)

        # 获取源文件夹中的所有文件
        files = os.listdir(source_folder_path)

        for file in files:
            # 检查文件是否是图片文件
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                # 构建源文件路径和目标文件路径
                source_path = os.path.join(source_folder_path, file)
                target_path = os.path.join(target_folder_path, file)

                # 剪切文件到目标文件夹
                shutil.move(source_path, target_path)

        print(f"图片剪切完成，从 {source_folder_path} 到 {target_folder_path}。")

if __name__ == "__main__":
    # 父文件夹路径
    parent_folder_path = "E:\\HA4M\\action_sq1"

    organize_images_in_folders(parent_folder_path)
