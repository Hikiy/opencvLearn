import cv2

img = cv2.imread('butterfly1.png', 1)
# 灰阶模式
# img = cv2.imread('butterfly1.png', 0)
# 包含α通道
# img = cv2.imread('butterfly1.png', -1)

cv2.imshow('image', img)

# 等待键盘输入，这里会堵塞
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     # wait for 's' key to save and exit
    # 保存图片
    cv2.imwrite('butterfly1_save.png', img)
    cv2.destroyAllWindows()
