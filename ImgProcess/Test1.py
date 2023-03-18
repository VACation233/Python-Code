import tkinter as tk
from tkinter import filedialog, Label, Button, Scale, LabelFrame, Frame
from PIL import Image, ImageTk, ImageOps
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建打开图片的按钮
        self.btn_open = Button(self, text="打开图片", command=self.open_image)
        self.btn_open.pack(side="left")

        # 创建滑块
        self.scale = Scale(self, label="参数", from_=0, to=255, orient="horizontal", command=self.update_image)
        self.scale.pack(side="left")

        # 创建图片显示框
        self.image_frame = LabelFrame(self, text="图片", width=400, height=400)
        self.image_frame.pack(side="left", padx=10, pady=10)

        # 创建直方图显示框
        self.hist_frame = LabelFrame(self, text="直方图", width=400, height=400)
        self.hist_frame.pack(side="left", padx=10, pady=10)

    def open_image(self):
        # 弹出文件对话框，选择要打开的图片
        self.filename = filedialog.askopenfilename()
        if self.filename != "":
            # 打开图片并显示在窗口中
            self.img = Image.open(self.filename)
            self.tkimg = ImageTk.PhotoImage(self.img)
            self.image = Label(self.image_frame, image=self.tkimg)
            self.image.pack()

            # 显示原始直方图
            self.hist, self.bins = ImageOps.histogram(self.img)
            self.hist_plot = Figure(figsize=(4, 4), dpi=100)
            self.hist_plot.add_subplot(111).plot(self.bins[:-1], self.hist)
            self.canvas = FigureCanvasTkAgg(self.hist_plot, master=self.hist_frame)
            self.canvas.get_tk_widget().pack()

            # 将滑块的值初始化为0
            self.scale.set(0)

    def update_image(self, value):
        # 更新图片
        img_arr = np.array(self.img)
        img_eq_arr = np.clip(int(value) * img_arr / 255, 0, 255).astype(np.uint8)
        img_eq = Image.fromarray(img_eq_arr)
        self.tkimg_eq = ImageTk.PhotoImage(img_eq)
        self.image.configure(image=self.tkimg_eq)

        # 更新直方图
        hist_eq, bins = ImageOps.histogram(img_eq)
        self.hist_plot.clf()
        self.hist_plot.add_subplot(111).plot(bins[:-1], hist_eq)
        self.canvas.draw()

# 创建主窗口
root = tk.Tk()
root.title("图像直方图线性变换")

# 创建应用程序实例
app = Application(master=root)

# 运行主循环
app.mainloop()
