# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:50:11 2022

@author: DHI-TPEM
"""

from skimage import io,filters,img_as_ubyte
img=io.imread("images/img1.tif",)
# try a blurring filter
gaussian_img=filters.gaussian(img,sigma=3)


io.imsave("images/saved/img1_skimg.jpg",gaussian_img)


io.imsave("images/saved/img1_skimg.tif",gaussian_img)

gauss_img_8bit=img_as_ubyte(gaussian_img)


io.imsave("images/saved/img1_skimg.tif",gauss_img_8bit)

## open cv image write#####

import cv2

cv2.imwrite("images/saved/img1_cv2.jpg",gaussian_img)
# only dark pixels

cv2.imwrite("images/saved/img1_cv2.jpg",gauss_img_8bit)

gauss_img_8bit_RGB=cv2.cvtColor(gauss_img_8bit,cv2.COLOR_BGR2RGB)

cv2.imwrite("images/saved/img1_cv2.jpg",gauss_img_8bit_RGB)
