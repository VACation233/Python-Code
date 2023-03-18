import os;
rootpath='C:/Users/VACation/Desktop/test'#要修改的图像所在的路径
filelist=os.listdir(rootpath)#遍历文件夹
i=0

for item in filelist:
    if item.endswith('.jpg'):
        src=os.path.join(os.path.abspath(rootpath),item)#原本的名称
        dst=os.path.join(os.path.abspath(rootpath),'36_'+str(i)+'.jpg')
    try:
        os.rename(src,dst)
        i+=1
        print("rename from %s to %s"%(src,dst))
    except:
        continue
print("end")