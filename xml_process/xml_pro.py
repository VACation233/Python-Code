import xml.dom.minidom as xmldom
import os
import tkinter as tk
from tkinter import Label,filedialog
root=tk.Tk()
label=Label(root,text="选择文件夹")
label.pack()
#FolderPath=filedialog.askdirectory()
#print("%s has been selected!" %(FolderPath))
xml_filepath=filedialog.askopenfile().name
#filename=os.path.basename(xml_file)
#print("%s has been selected!" %(xml_filepath))

xml_obj=xmldom.parse(xml_filepath)
root = xml_obj.documentElement

list=root.getElementsByTagName("object")
print(list)
print(len(list))
