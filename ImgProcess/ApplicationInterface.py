
import tkinter as tk
from PIL import Image,ImageTk,ImageEnhance
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy
from ImageProcessor import ImgProcessor
class AppInterface:
    def __init__(self,master):
        self.imgProcessor=ImgProcessor()
        self.master=master
        self.master.geometry('800x600')
        self.master.title("Histogram and Linear change")
        self.img=None
        
        #创建 matplotlib图形
        self.fig=Figure(figsize=(6,4),dpi=100)
        self.ax1=self.fig.add_subplot(2,1,1)
        self.ax2=self.fig.add_subplot(2,1,2)
        
        #将matplotlib放入tinker里面
        self.canvas=FigureCanvasTkAgg(self.fig,master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
        #创建文件选择按钮
        self.load_button=tk.Button(self.master,text="选择图像",command=self.load_image)
        self.load_button.pack(side=tk.LEFT,padx=10,pady=10)
        
        #创建滑块
        self.silder_label=tk.Label(self.master,text="Contrast: ")
        self.silder_label.pack(side=tk.LEFT,padx=10,pady=10)
        self.silder=tk.Scale(self.master,from_=0.0,to=2.0,resolution=0.01,orient=tk.HORIZONTAL,command=self.update_histogram)
        self.silder.set(1.0)
        self.silder.pack(side=tk.LEFT,padx=10,pady=10)
        
    def load_image(self):
        file_path=filedialog.askopenfilename()
        if file_path:
            
            self.img=Image.open(file_path).convert('L')
            self.imgProcessor.load_img(self.img,self.ax1)
    
    def update_histogram(self)
                
if __name__=='__main__':
        root=tk.Tk()
        app=AppInterface(root)
        root.mainloop()