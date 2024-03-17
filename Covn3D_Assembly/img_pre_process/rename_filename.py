import os

# 定义数据顺序
data_order = ['v_0Transitions_g',
              'v_1PPCarrier_g',
              'v_2PPGearBearings_g',
              'v_3PPPlanetGears_g',
              'v_4PPCarrierShaft_g',
              'v_5PPSunShaft_g',
              'v_6PPSunGear_g',
              'v_7PPSunGearBearing_g',
              'v_8PPRingBear_g',
              'v_9PBlock2PBlock1_g',
              'v_10PickPCover_g',
              'v_11PickPScrews_g',
              'v_12GetEGT_g']

# 指定视频文件夹路径
video_folder_path = 'E:\HA4M\\action_sq2'

# 获取视频文件夹列表，并按照数字顺序排序
video_folders = sorted([f for f in os.listdir(video_folder_path) if os.path.isdir(os.path.join(video_folder_path, f))], key=lambda x: int(x.split('action')[1]))

# 检查视频文件夹数量是否与数据顺序一致
if len(video_folders) != len(data_order):
    print("错误：视频文件夹数量与数据顺序不一致。")
else:
    # 遍历视频文件夹并重命名
    for i in range(len(video_folders)):
        old_path = os.path.join(video_folder_path, video_folders[i])
        new_name = f'{data_order[i]}'
        new_path = os.path.join(video_folder_path, new_name)
        os.rename(old_path, new_path)
        print(f'重命名文件夹：{video_folders[i]} -> {new_name}')
