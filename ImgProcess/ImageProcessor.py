import cv2
import numpy as np
from PIL import Image,ImageTk
class ImgProcessor:
    #def __init__(self):
        
    def load_img(self,img,):
        if img is None:
            return
        img_arr=np.array(img)
        