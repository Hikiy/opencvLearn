import cv2

img = cv2.imread('Interstellar.png')

grad_x = cv2.Sobel(img, cv2.CV_32F, 1, 0)  # 使用CV_32F防止数据溢出
grad_y = cv2.Sobel(img, cv2.CV_32F, 0, 1)
gradx = cv2.convertScaleAbs(grad_x)
grady = cv2.convertScaleAbs(grad_y)

cv2.imshow("src", img)
cv2.imshow("gradx", grad_x)
cv2.imshow("grady", grady)

# 合并x, y两个梯度
gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)

cv2.imshow("gradxy", gradxy)
cv2.waitKey()
