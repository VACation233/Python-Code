import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

##可以打开图片、点击修改亮度

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")

        # 创建菜单栏
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.open_image)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # 创建控件
        self.image_label = tk.Label(self.master)
        self.image_label.pack(side="left", padx=10, pady=10)

        self.process_button = tk.Button(self.master, text="Process", command=self.process_image)
        self.process_button.pack(side="top", padx=10, pady=10)

        # 初始化变量
        self.img = None
        self.out = None

    def open_image(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.img = cv2.imread(filename, 0)
            self.show_image()

    def show_image(self):
        # 调整图像尺寸以适应标签
        img = cv2.resize(self.img, (400, 400))

        # 将OpenCV图像转换为PIL图像
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # 显示图像
        self.image_label.configure(image=img)
        self.image_label.image = img

    def process_image(self):
        # 线性变换
        a = 1.5
        b = 50
        self.out = np.uint8(np.clip((a * self.img + b), 0, 255))

        # 显示处理后的图像
        self.show_processed_image()

    def show_processed_image(self):
        # 调整图像尺寸以适应标签
        img = cv2.resize(self.out, (400, 400))

        # 将OpenCV图像转换为PIL图像
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        # 显示图像
        self.image_label.configure(image=img)
        self.image_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



# import tkinter as tk
# from PIL import Image, ImageTk, ImageEnhance


# class ImageProcessor:
#     def __init__(self, image_path):
#         self.image_path = image_path
#         self.image = Image.open(image_path)
#         self.brightness_factor = 1.0
#         self.contrast_factor = 1.0
#         self.processed_image = self.image.copy()
    
#     def update_brightness(self, factor):
#         self.brightness_factor = factor
#         self.update_processed_image()

#     def update_contrast(self, factor):
#         self.contrast_factor = factor
#         self.update_processed_image()

#     def update_processed_image(self):
#         self.processed_image = self.image.copy()
#         brightness = ImageEnhance.Brightness(self.processed_image)
#         self.processed_image = brightness.enhance(self.brightness_factor)
#         contrast = ImageEnhance.Contrast(self.processed_image)
#         self.processed_image = contrast.enhance(self.contrast_factor)

#     def get_processed_image_tk(self, size):
#         return ImageTk.PhotoImage(self.processed_image.resize(size))


# class Application:
#     def __init__(self, master):
#         self.master = master
#         self.image_processor = ImageProcessor("Test.png")

#         # Create sliders to adjust brightness and contrast
#         self.brightness_label = tk.Label(self.master, text="Brightness")
#         self.brightness_scale = tk.Scale(self.master, from_=0.1, to=2.0, resolution=0.1,
#                                          orient=tk.HORIZONTAL, command=self.update_brightness)
#         self.brightness_scale.set(self.image_processor.brightness_factor)
#         self.contrast_label = tk.Label(self.master, text="Contrast")
#         self.contrast_scale = tk.Scale(self.master, from_=0.1, to=2.0, resolution=0.1,
#                                        orient=tk.HORIZONTAL, command=self.update_contrast)
#         self.contrast_scale.set(self.image_processor.contrast_factor)

#         # Create a canvas to display the image
#         self.canvas = tk.Canvas(self.master)
#         self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         # Update the canvas with the processed image
#         processed_image_tk = self.image_processor.get_processed_image_tk((600, 600))
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=processed_image_tk)
#         self.canvas.image = processed_image_tk

#         # Pack the sliders
#         self.brightness_label.pack()
#         self.brightness_scale.pack()
#         self.contrast_label.pack()
#         self.contrast_scale.pack()

#     def update_brightness(self, factor):
#         self.image_processor.update_brightness(float(factor))
#         self.update_canvas()

#     def update_contrast(self, factor):
#         self.image_processor.update_contrast(float(factor))
#         self.update_canvas()

#     def update_canvas(self):
#         processed_image_tk = self.image_processor.get_processed_image_tk((600, 600))
#         self.canvas.itemconfig(self.canvas_image, image=processed_image_tk)
#         self.canvas.image = processed_image_tk


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Application(root)
#     root.mainloop()
