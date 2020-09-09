import cv2
import numpy as np
import sys

# 用线性拟合来处理玻璃边角问题，但是拿垂直的线没办法，所以当作是学习使用线性拟合了

# 线性拟合处理
def getKAndB(points):
    outPut = cv2.fitLine(points, cv2.DIST_HUBER, 0, 0.1, 0.01)
    k = outPut[1] / outPut[0]
    b = outPut[3] - k * outPut[2]
    return [k, b]


# 图片处理（模糊、二值化）
img = cv2.imread('7.bmp', 0)
blur = cv2.blur(img, (9, 9))
ret, dst = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(dst, cv2.MORPH_GRADIENT, kernel)
result = cv2.erode(gradient, (5, 5), iterations=3)

# 获取图片宽高
height, width = result.shape
if width <= 20 or height <= 20:
    print('图片太小了')
    sys.exit()

# 循环查找第一个拐点和线的公式，用的是线性拟合
points1 = []
points2 = []
point1 = [0, 0]

# 两个坐标集，其中监测用的固定为20个像素，每移一个像素就对比一次斜率变化，如果两个斜率大于一定值则说明拐弯了
for i in range(0, 20):
    for j in range(height):
        if gradient[j, i] == 255:
            points1.append([i, j])
            points2.append([i, j])
            break

for i in range(20, width-1):
    for j in range(height):
        if gradient[j, i] == 255:
            points1.append([i, j])
            points2.append([i, j])
            del(points2[0])
            break
    points1n = np.array(points1)
    points2n = np.array(points2)
    k1, b1 = getKAndB(points1n)
    k1T, b1T = getKAndB(points2n)
    if k1T - k1 > 0.1:
        x1 = i - 10
        y1 = int(k1 * x1 + b1)
        # 第一个拐弯点
        point1 = [x1, y1]
        break

print(point1)
if point1[0] == 0 and point1[1] == 0:
    print('没找到第1个拐点')
    sys.exit()

# 为了更准确，以拐弯点之前的线段来重新计算直线公式
points1 = []
for i in range(0, point1[0]-20):
    for j in range(height):
        if gradient[j, i] == 255:
            points1.append([i, j])
points1n = np.array(points1)
k1, b1 = getKAndB(points1n)
print(k1, b1)

# 同理计算右下角的直线的公式，不同在于读取像素的时候和上面是反过来的
points3 = []
points4 = []
point2 = [0, 0]

for j in range(height-1, height-21, -1):
    for i in range(width-1, 0, -1):
        if gradient[j, i] == 255:
            points3.append([i, j])
            points4.append([i, j])
            break

for j in range(height-22, 0, -1):
    for i in range(width-1, 0, -1):
        if gradient[j, i] == 255:
            points3.append([i, j])
            points4.append([i, j])
            del(points4[0])
            break
    points3n = np.array(points3)
    points4n = np.array(points4)
    k2, b2 = getKAndB(points3n)
    k2T, b2T = getKAndB(points4n)
    print(k2, k2T)
    if k2 - k2T > 10 and 0 < k2T < 10:
        y2 = j + 10
        x2 = int((y2-b2)/k2)
        # 第2个拐弯点
        point2 = [x2, y2]
        break

print(point2)
if point2[0] == 0 and point2[1] == 0:
    print('没找到第2个拐点')
    sys.exit()

# 为了更准确，以拐弯点之前的线段来重新计算直线公式
points3 = []
for j in range(height-1, height-point2[1]+5, -1):
    for i in range(width-1, 0, -1):
        if gradient[j, i] == 255:
            points3.append([i, j])
points3n = np.array(points3)
k2, b2 = getKAndB(points3n)
print(k2, b2)

# 计算出两条延长线的交点：

x3 = (b2-b1)/(k1-k2)
y3 = int(k1*x3+b1)
x3 = int(x3)
# 两条直线的交点
point3 = [x3, y3]
print(point3)

# cv2.imshow('image', img)
# # cv2.imshow('closing', closing)
# cv2.imshow('blur', blur)
# cv2.imshow('dst', dst)
# cv2.imshow('gradient', gradient)
cv2.imshow('d', result)

k = cv2.waitKey(0)

