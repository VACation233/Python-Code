import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk

class App:
    def __init__(self,master):
        self.master=master
        self.img=None
        
        #创建UI组件
        self.label=tk.Label(self.master)
        self.label.pack()
        
        self.button=tk.Button(self.master,text="选择图片",command=self.open_file)
        