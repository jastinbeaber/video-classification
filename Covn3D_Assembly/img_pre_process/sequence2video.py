import cv2
import os
from tqdm import tqdm

# 设置输入视频序列的根文件夹路径
root_folder = 'E:\\HA4M\\action_sq1\\'

# 设置输出视频的文件夹路径
output_folder = 'E:\\HA4M\\output_videos\\'

# 创建输出视频文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历每个视频序列
for i in range(13):
    input_frames_folder = os.path.join(root_folder, f'action{i}')

    # 获取文件夹中的所有帧文件
    frame_files = [f for f in os.listdir(input_frames_folder) if f.endswith('.png')]

    # 获取第一帧的大小以创建视频
    first_frame = cv2.imread(os.path.join(input_frames_folder, frame_files[0]))
    height, width, _ = first_frame.shape

    # 设置输出视频的文件路径和名称
    output_video_path = os.path.join(output_folder, f'action_{i}.mp4')

    # 设置视频编码器和输出视频对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4编码
    video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (width, height))  # 30.0是帧速率，可以根据需要调整

    # 添加进度条
    for frame_file in tqdm(frame_files, desc=f'处理视频{i}'):
        frame_path = os.path.join(input_frames_folder, frame_file)
        frame = cv2.imread(frame_path)
        video.write(frame)

    # 释放视频对象
    video.release()

print("视频处理完成。")
