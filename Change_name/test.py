import os
import tkinter as tk
from tkinter import Label, filedialog
root=tk.Tk()
#root.withdraw()
label=Label(root,text="选择文件夹")
label.pack()
FolderPath=filedialog.askdirectory()
#root.mainloop()
#root.withdraw()
#FilePath=filedialog.askopenfilename()
#FolderPath=os.path.dirname
print("%s has been selected!" %(FolderPath))
filelist=os.listdir(FolderPath)
i=0
number=str(FolderPath)
number=number[-2:]
print(number)