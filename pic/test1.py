# class Person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self,name):
#         print(f"Hello, {name}!")

# person = Person("HAHA")
# person.greet("Alice")  # 输出 "Hello, Alice!"
# person.greet("Bob")

# #调亮度功能正常

# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
# from matplotlib.widgets import Slider

# plt.ion()
# # 加载图像
# img = Image.open('Test.png')

# # 将图像转换为numpy数组
# img_arr = np.array(img)

# # 创建子图和滑动条
# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.25)
# axSlider = plt.axes([0.2, 0.15, 0.6, 0.03])
# slider = Slider(axSlider, 'Contrast', 0, 10, valinit=1)

# # 定义用于更新图像的函数
# def update(val):
#     # 获取滑动条的值
#     contrast = slider.val

#     # 进行直方图均衡化
#     img_eq = np.clip(contrast * img_arr, 0, 255).astype(np.uint8)

#     # 绘制均衡化后的图像
#     ax.imshow(img_eq)
#     ax.set_title('Equalized Image')

#     # 绘制均衡化后的直方图
#     fig2, ax2 = plt.subplots()
#     ax2.hist(img_eq.flatten(), 256, [0, 256])
#     ax2.set_title('Equalized Histogram')
#     plt.show()

# # 初始化图像和直方图
# ax.imshow(img_arr)
# ax.set_title('Original Image')
# fig2, ax2 = plt.subplots()
# ax2.hist(img_arr.flatten(), 256, [0, 256])
# ax2.set_title('Original Histogram')

# # 将update函数绑定到滑动条
# slider.on_changed(update)
# # Turn off interactive mode
# plt.ioff()
# # 显示所有绘图
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider
# from PIL import Image

# # Enable interactive mode
# plt.ion()

# # Load image and convert to grayscale
# img = Image.open("Test.png")

# # Convert image to numpy array
# img_arr = np.array(img)

# # Define histogram equalization function
# def hist_equalization(cutoff):
#     img_eq = img_arr.copy()
#     hist, bins = np.histogram(img_eq.flatten(), 256, [0, 256])
#     cdf = hist.cumsum()
#     cdf_normalized = cdf * float(hist.max()) / cdf.max()
#     cutoff_value = int(cutoff * 255)
#     cdf_mask = np.ma.masked_less(cdf_normalized, cutoff_value)
#     cdf_mask = (cdf_mask - cdf_mask.min()) * 255 / (cdf_mask.max() - cdf_mask.min())
#     cdf_mask = np.ma.filled(cdf_mask, 0).astype('uint8')
#     img_eq = cdf_mask[img_eq]
#     return img_eq

# # Create figure and axis
# fig, ax = plt.subplots()

# # Display image
# im = ax.imshow(img_arr, cmap='gray')

# # Create slider widget
# slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])
# slider = Slider(slider_ax, 'Cutoff', 0, 1, valinit=0.5)

# # Define update function
# def update(val):
#     # Call histogram equalization function with current slider value
#     img_eq = hist_equalization(slider.val)
#     # Update image data
#     im.set_data(img_eq)
#     # Redraw canvas
#     fig.canvas.draw_idle()

# # Register update function with slider widget
# slider.on_changed(update)

# # Turn off interactive mode
# plt.ioff()

# # Display plot
# plt.show()



import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk

##UI可以参考

class HistogramEqualizationApp:
    def __init__(self, master):
        self.master = master
        
        self.master.geometry('800x600')
        self.master.title('Histogram Equalization App')
        self.img = None

        # 创建 matplotlib 图形
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax1 = self.fig.add_subplot(2, 1, 1)
        self.ax2 = self.fig.add_subplot(2, 1, 2)

        # 创建 matplotlib 的 Tkinter 组件
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 创建文件选择按钮
        self.load_button = tk.Button(self.master, text="Select Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

        # 创建滑块
        self.slider_label = tk.Label(self.master, text="Contrast: ")
        self.slider_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.slider = tk.Scale(self.master, from_=0.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL, command=self.update_histogram)
        self.slider.set(1.0)
        self.slider.pack(side=tk.LEFT, padx=10, pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            
            self.img = Image.open(file_path).convert('L')
            self.plot_histogram()

    def plot_histogram(self):
        if self.img is None:
            return
        img_arr = np.array(self.img)
        self.ax1.clear()
        self.ax1.imshow(self.img, cmap='gray')
        self.ax1.set_title('Original Image')
        self.ax2.clear()
        self.ax2.hist(img_arr.ravel(), bins=256, color='gray')
        self.ax2.set_title('Histogram')
        self.canvas.draw()

    def update_histogram(self, val):
        if self.img is None:
            return
        img_arr = np.array(self.img)
        img_eq = Image.fromarray(img_arr).histogram().equalize().np.asarray()
        
        img_eq = Image.fromarray(img_eq)
        img_eq = ImageTk.PhotoImage(img_eq)
        self.ax1.clear()
        self.ax1.imshow(img_eq, cmap='gray')
        self.ax1.set_title('Equalized Image')
        self.ax2.clear()
        self.ax2.hist(img_eq, bins=256, color='gray')
        self.ax2.set_title('Histogram')
        self.canvas.draw()


if __name__ == '__main__':
    root = tk.Tk()
    app = HistogramEqualizationApp(root)
    root.mainloop()
