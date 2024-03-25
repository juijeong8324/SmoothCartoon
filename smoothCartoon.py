import cv2
import numpy as np

def cartoonize(img):
  kernel_size = 3 # 3 7
  line_size = 7 # 3 7
  # Create Edge Mask
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayScale
  gray_blur = cv2.medianBlur(gray, kernel_size) # Smoothing
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, kernel_size)
  edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

  blurred = cv2.bilateralFilter(img, d=10, sigmaColor=250,sigmaSpace=250) # reduce noise
  cartoon = cv2.bitwise_and(blurred, edges)
  return cartoon

# Read input image, return type is numpy.ndarray
input_image = cv2.imread('test3.jpg')

# Apply cartoonize effect
cartoon_image = cartoonize(input_image)

# Display the original and cartoon images
merge = np.hstack((input_image, cartoon_image))
cv2.imshow('Original Image | Cartoon Image', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()