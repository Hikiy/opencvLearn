import numpy as np
import cv2

# 腐蚀操作和膨胀操作

img = cv2.imread('butterfly1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0)

# kernel（卷积核核）指定一个范围矩阵，这里就是以像素点为中心的一个3*3的矩形
kernel = np.ones((3, 3), np.uint8)

# 腐蚀操作，范围内有黑则变黑
erosion = cv2.erode(binary, kernel, iterations=1)

# 膨胀操作，范围内有白就白  1:迭代次数，也就是执行几次膨胀操作
dilate = cv2.dilate(binary, kernel, 1)

# 开运算 先腐蚀再膨胀 去除毛刺
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, 1)

# 闭运算 线膨胀在腐蚀 填补缺陷
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# 梯度运算 显示边缘信息 即膨胀后的图像 - 腐蚀后的图像
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('src', binary)
cv2.imshow('dilate', dilate)
cv2.imshow('erosion', erosion)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)

cv2.waitKey()