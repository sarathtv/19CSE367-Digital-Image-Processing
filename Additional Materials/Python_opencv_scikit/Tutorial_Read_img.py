# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:49:52 2022

@author: DHI-TPEM
"""

# scikit image  pip install scikit-image
# opencv pip install opencv-python

#https://scikit-image.org/docs/stable/
#https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

##skimage
from skimage import io,img_as_float,img_as_ubyte

img_sk=io.imread("images/img1.tif",)
# height, width and channel
# target -- to convert to float
#  img_as_float()

img2=img_as_float(img)

# img_as_ubyte()

img_8bit=img_as_ubyte(img2)
# astypefloat
### cv2####

import cv2
img=cv2.imread("images/img1.tif")
# open cv reads image as BGR chanel 
# scikit image reads in RGB
gray_img=cv2.imread("images/img1.tif",0)

clr_img=cv2.imread("images/img1.tif",1)

# default--> cv2.imread ,reads imgs as color images


# BGR-> RGB
img_opencv_RGB=cv2.cvtColor(clr_img,cv2.COLOR_BGR2RGB)

















