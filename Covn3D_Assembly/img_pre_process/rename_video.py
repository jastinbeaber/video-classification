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

# 指定视频文件路径
video_folder_path = '../databases/train'

# 获取视频文件列表，并按照数字顺序排序
video_files = sorted([f for f in os.listdir(video_folder_path) if f.endswith('.mp4')], key=lambda x: int(x.split('_')[1][:-4]))

# 检查视频文件数量是否与数据顺序一致
if len(video_files) != len(data_order):
    print("错误：视频文件数量与数据顺序不一致。")
else:
    # 遍历视频文件并重命名
    for i in range(len(video_files)):
        old_path = os.path.join(video_folder_path, video_files[i])
        new_name = f'{data_order[i]}.mp4'
        new_path = os.path.join(video_folder_path, new_name)
        os.rename(old_path, new_path)
        print(f'重命名：{video_files[i]} -> {new_name}')
