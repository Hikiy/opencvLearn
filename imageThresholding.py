import cv2

img = cv2.imread('butterfly1.png')
# 1.灰度化图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2.二值化 2参数是阀值 3参数是最大值 4参数是阀值类型
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 使用Otsu法计算阀值
ret2, binary2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 打印阀值
print(ret)
print(ret2)

# 局部阀值法
binary3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0)
binary4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)

cv2.imshow('nomal', binary)
cv2.imshow('otsu', binary2)
cv2.imshow('mean', binary3)
cv2.imshow('gaussian', binary4)

cv2.waitKey(0)
