# 0001 导入tkinter库
from tkinter import *
 
# 0002 tkinter中有一个Tk()类，也就是窗口类，本段代码用于实例Tk()类的一个对象root
root=Tk()
 
# 0004 Lable是Tk()的子类，我们用它在根窗体root上面放一个文字标签控件，并且实例化对象为lable
lable=Label(root,text='nimabi')
 
# 0005 用pack()这个方法让窗体显示出来，大小自动适应
lable.pack()
 
# 0006 我们用mainloop做一个死循环让程序永远运行下去
root.mainloop()