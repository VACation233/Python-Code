from PIL import Image
import os
import tkinter as tk
from tkinter import Label,filedialog
import sys
import io
import cv2

root=tk.Tk()
#隐藏主窗口
root.withdraw()
label=Label(root,text="选择需要处理的文件")
label.pack()

File=filedialog.askopenfilename()
if not File:
    print("No file selected")
    exit()
#使用open方法打开图片，并用convert()转化为RGBA格式
image=Image.open(File).convert("RGBA")
r,g,b,a=image.split()

print(r.mode,g.mode,b.mode,a.mode)
#point方法对 alpha 通道的像素值进行映射处理，接受一个函数作为参数，这个函数将被应用到图像的每个像素上，返回的值将替代原来的像素值
# lambda表达式
a=a.point(lambda i:255 if i>128 else 0)

result=Image.merge("RGBA",(r,g,b,a))
result.show()
result.save("result.png",'PNG')

#image=cv2.imread(File)





