'''
this code reads an image file, converts its color space from RGB to BGR, and displays it using matplotlib. 
The resulting plot shows the image with the title 'SKY', without axis labels or ticks.
'''
import cv2 as cv 
from matplotlib import pyplot as plt

img = cv.imread('my_image.jpg')
plt.imshow(cv.cvtColor( img,cv.COLOR_RGB2BGR))
plt.title('SKY')
plt.axis('off')
plt.show()
