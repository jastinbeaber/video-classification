from PIL import Image
import os

def resize_images(input_folder, output_folder, new_width, new_height):
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图片
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # 检查是否为图片文件
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            output_path = os.path.join(output_folder, filename)

            # 打开图片
            img = Image.open(input_path)

            # 调整分辨率
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # 保存调整后的图片
            resized_img.save(output_path)

            print(f"Resized: {filename}")

if __name__ == "__main__":
    # 输入文件夹和输出文件夹路径
    input_folder_path = "E:\HA4M\IDU001V003\Color\\000124702712"
    output_folder_path = "E:\HA4M\IDU001V003\\video_sq3"

    # 新的宽度和高度
    new_width = 342
    new_height = 256

    # 调用函数
    resize_images(input_folder_path, output_folder_path, new_width, new_height)
