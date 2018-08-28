import cv2
import numpy as pd
img=cv2.imread("flower.jpg")
height,width=img.shape[:2]
#let's get the starting pixel coordinates(top left,of cropping rectangles)
start_row,start_col=int(height*.01),int(width*.01)
#let's get the ending pixel coordinates(bottom left,of cropping rectangles) 
end_row,end_col=int(height*.25),int(width*.25)
#simply use the indexing to crop the image
cropped1=img[start_row:end_row,start_col:end_col]

start_row,start_col=int(height*.25),int(width*.25)
#let's get the ending pixel coordinates(bottom left,of cropping rectangles) 
end_row,end_col=int(height*.50),int(width*.50)
#simply use the indexing to crop the image
cropped2=img[start_row:end_row,start_col:end_col]

start_row,start_col=int(height*.50),int(width*.50)
#let's get the ending pixel coordinates(bottom left,of cropping rectangles) 
end_row,end_col=int(height*.75),int(width*.75)
#simply use the indexing to crop the image
cropped3=img[start_row:end_row,start_col:end_col]

start_row,start_col=int(height*.75),int(width*.75)
#let's get the ending pixel coordinates(bottom left,of cropping rectangles) 
end_row,end_col=int(height*.1),int(width*.1)
#simply use the indexing to crop the image
cropped4=img[start_row:end_row,start_col:end_col]
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.imshow("cropped",cropped1)
cv2.waitKey(0)
cv2.imshow("cropped",cropped2)
cv2.waitKey(0)
cv2.imshow("cropped",cropped3)
cv2.waitKey(0)
cv2.imshow("cropped",cropped4)
cv2.waitKey(0)
cv2.destroyAllWindows()
