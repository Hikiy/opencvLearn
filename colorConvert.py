import cv2
import numpy

# 将图片颜色空间转换并且拾取想要的颜色


img = cv2.imread('blueButterfly.png', 1)

# 转换颜色
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = numpy.array([110, 50, 50])
upper_blue = numpy.array([130, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 用mask与原图匹配
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("image", res)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('bluButterfly1_save.png', hsv)
    cv2.destroyAllWindows()
