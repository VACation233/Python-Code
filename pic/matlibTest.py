import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

##可以正常导入图片，但是不知道修改了哪些内容

# 加载图像
img = Image.open('Test.png')

# 将图像转换为numpy数组
img_arr = np.array(img)

# 显示原始图像
fig, ax = plt.subplots()
ax.imshow(img_arr)
ax.set_title('Original Image')

# 计算图像的直方图
hist, bins = np.histogram(img_arr.flatten(), 256, [0, 256])

# 绘制原始图像的直方图
fig, ax = plt.subplots()
ax.hist(img_arr.flatten(), 256, [0, 256])
ax.set_title('Original Histogram')

# 进行直方图均衡化
img_eq = ImageOps.equalize(img)

# 显示均衡化后的图像
fig, ax = plt.subplots()
ax.imshow(np.asarray(img_eq))
ax.set_title('Equalized Image')

# 绘制均衡化后的直方图
fig, ax = plt.subplots()
ax.hist(np.asarray(img_eq).flatten(), 256, [0, 256])
ax.set_title('Equalized Histogram')

# 显示所有绘图
plt.show()
