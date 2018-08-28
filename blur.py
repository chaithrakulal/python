#blurring
'''import cv2
import numpy as  np
img=cv2.imread("flower.jpg")
cv2.imshow('original image',img)
cv2.waitKey(0)
kernel_3x3= np.ones((3,3),np.float32)/9

blurred=cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow('3x3 Kernel Blurring',blurred)
cv2.waitKey(0)

kernel_7x7= np.ones((7,7),np.float32)/49
blurred2=cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow('7x7 Kernel Blurring',blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import cv2
import numpy as  np
img=cv2.imread("flower.jpg")
cv2.imshow('original image',img)
blur = cv2.blur(img, (3,3))
cv2.imshow('Blur Image',blur)
cv2.waitKey(0)

Guassian = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow('Guassian Image',Guassian)
cv2.waitKey(0)

Median = cv2.MedianBlur(img, 5)
cv2.imshow('Median Image',Median)
cv2.waitKey(0)

cv2.destroyAllWindows()
