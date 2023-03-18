# from PIL import Image
# import cv2
# import os
# from tkinter import filedialog
# # 遍历文件夹
# filePath=filedialog.askdirectory(title="选择图片的文件夹")
# filePath=os.path.abspath(filePath)
# for file_name in os.listdir(filePath):
#     # 读取原始图片并转为灰度图像
#     img = cv2.imread(os.path.join(filePath, file_name))
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # 对灰度图像进行二值化处理
#     thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#     # 将二值化后的图像转换为 RGB 格式，并将背景颜色设为透明
#     img_pil = Image.fromarray(thresh).convert('RGB')
#     img_pil.putalpha(255 - thresh)
#     # 保存处理后的图像
#     img_pil.save(os.path.join(filePath, 'new_' + file_name))
# print("已完成")

from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

##正常导入图片、显示直方图

# Load image
img = Image.open("test2.png")

# Apply histogram equalization
img_eq = ImageOps.equalize(img)

# Convert image to numpy array
img_arr = np.array(img)
img_eq_arr = np.array(img_eq)

# Display the original and equalized images
fig, (ax1, ax2,ax3,ax4) = plt.subplots(ncols=4, figsize=(10, 5))
ax1.imshow(img_arr)
ax1.set_title('Original Image')
ax2.imshow(img_eq_arr)
ax2.set_title('Equalized Image')
img_eq_arr = np.array(img_eq)[:, :, 0]  # 取第一个通道
ax3.hist(img_eq_arr.ravel(), bins=256, color='gray')
ax3.set_title('Equalized Histogram')

img_arr=np.array(img)[:, :, 0]
ax4.hist(img_arr.ravel(),bins=256,color='gray')
ax4.set_title('Original Histogram')
plt.show()

