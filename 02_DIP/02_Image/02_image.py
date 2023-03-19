#imageio
import imageio

#opencv
import cv2

#scikit image
import skimage


#matplotlib
import matplotlib.pyplot as plt

#Numpy
import numpy as np

#pillow
from PIL import Image


#reading image
img_one = cv2.imread(r'images/c_img.jpg')
print('shape of image one: ', img_one.shape)

print(img_one)
print(img_one.dtype)

plt.imshow(img_one)
plt.title('Image One')
plt.axis('off')

#pillow vs opencv
img_one_pil = Image.open(r'images/c_img.jpg')
plt.imshow(img_one_pil)
plt.title('Image One  pil')
plt.axis('off')


img_two_cv = cv2.imread(r'images/colors.png')
img_two_pil = Image.open(r'images/colors.png')

plt.subplot(1, 2, 1)
plt.imshow(img_two_cv)
plt.title('img_two_cv')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_two_pil)
plt.title('img_two_pil')
plt.axis('off')

# PIL: RGB --> CV: BGR

# COLOR SPACE CONVERSION
img_two_cv_rgb = cv2.cvtColor(img_two_cv, cv2.COLOR_RGB2BGR)
img_two_pil = Image.open(r'images/colors.png')

plt.subplot(1, 2, 1)
plt.imshow(img_two_cv_rgb)
plt.title('img_two_cv_rgb')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_two_pil)
plt.title('img_two_pil')
plt.axis('off')

# RGB --> GBR (NO DIFFERENCE TO DISPAY)


#Color to Gray!
img_two_cv = cv2.imread(r'images/colors.png')
img_two_cv_gray = cv2.cvtColor(img_two_cv, cv2.COLOR_RGB2GRAY)
img_two_cv_gray_bgr = cv2.cvtColor(img_two_cv, cv2.COLOR_BGR2GRAY)

cv2.imshow('img_two_cv_gray', img_two_cv_gray)
cv2.waitKey(0)


cv2.imshow('img_two_cv_gray', img_two_cv_gray_bgr)
cv2.waitKey(0)

#Gray
img_two_cv_gray = cv2.imread(r'images/colors.png', 0)
print('shape of gray image: ', img_two_cv_gray.shape)


#color image
img_two_cv_color = cv2.imread(r'images/colors.png', 1)

#unchanged
img_two_cv_unchanged = cv2.imread(r'images/colors.png', -1)

#Color image Channels
img_channels = cv2.imread(r'images/colors.png')

#bgr
blue_ch = img_channels[:, :, 0]
green_ch = img_channels[:, :, 1]
red_ch = img_channels[:, :, 2]


#b, g, r =cv2.split(img)
plt.subplot(2, 2, 1)
plt.imshow(img_channels)
plt.title('original img')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(blue_ch)
plt.title('blue ch')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(green_ch)
plt.title('green ch')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(red_ch)
plt.title('red ch')
plt.axis('off')















