from PIL import Image
import os
import tkinter as tk
from tkinter import Label, filedialog
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

root=tk.Tk()
root.withdraw()
label=Label(root,text="选择文件夹")
label.pack()
#FolderPath=filedialog.askdirectory()
File=filedialog.askopenfilename()
if not File:
    print("No Openfile Choices")
    exit()

print(File)
SavePath=filedialog.askdirectory()

#print(os.path.abspath(SavePath))
i=0
left=0
right=20

while(right<=280):
    img=Image.open(File)
    cut=img.crop((left,0,right,28))
    cut.save(os.path.join(os.path.abspath(SavePath),str(i)+'c.png'))
    i=i+1
    left+=20
    right+=20
print("end")

