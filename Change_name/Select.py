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
i=1
#number=FolderPath[-2:]
#print("编号为%s"%(number))
#number='0';
#number=input("请输入积木编号")
for item in filelist:
    if item.endswith(".png"):
        src=os.path.join(os.path.abspath(FolderPath),item)
        #dst=os.path.join(os.path.abspath(FolderPath),str(number)+'_'+str(i)+'.jpg')
        dst=os.path.join(os.path.abspath(FolderPath),str(i)+'.png')
        try:
            os.rename(src,dst)
            i+=1
            print("Rename from %s To %s"%(src,dst))
        except:
            continue
print("end")
'''print(filelist)
for item in filelist:
    filename=item.split('.')[0]
    if item.endswith(".gif"):
        src=os.path.join(os.path.abspath(FolderPath),item)
        dst=os.path.join(os.path.abspath(FolderPath),filename+'.png')
        try:
            os.rename(src,dst)
            print("Rename from %s To %s" %(src,dst))
        except:
            print("Error")
            continue
print("end")'''
    
