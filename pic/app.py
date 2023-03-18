import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image,ImageTk

class App:
    def __init__(self,master):
        self.master=master
        self.img=None
        self.photo=None
        self.scale=None
        self.angle=None
        self.brightness=None
        
        #创建UI组件
        self.label=tk.Label(self.master)
        self.label.pack()