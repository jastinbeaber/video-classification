import os
import shutil

# 源文件夹路径
source_folder = r'E:\video-classification\Covn3D_Assembly\databases\train'

# 目标文件夹列表
target_folders = [
    "0Transitions",
    "1PPCarrier",
    "2PPGearBearings",
    "3PPPlanetGears",
    "4PPCarrierShaft",
    "5PPSunShaft",
    "6PPSunGear",
    "7PPSunGearBearing",
    "8PPRingBear",
    "9PBlock2PBlock1",
    "10PickPCover",
    "11PickPScrews",
    "12GetEGT"
]

# 遍历目标文件夹列表
for folder in target_folders:
    # 构建目标文件夹路径
    target_folder = os.path.join(r'E:\video-classification\Covn3D_Assembly\databases\train', folder)

    # 如果目标文件夹不存在，创建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 获取与目标文件夹名字一致的文件列表
    files_to_move = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f.startswith(folder)]

    # 将文件移动到目标文件夹
    for file_name in files_to_move:
        source_file = os.path.join(source_folder, file_name)
        target_file = os.path.join(target_folder, file_name)
        shutil.move(source_file, target_file)

print("文件移动完成")
