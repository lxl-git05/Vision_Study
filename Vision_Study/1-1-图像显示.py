# ********导入库********
import numpy as np
import cv2 as cv

# ********功能区********
# 加载一张图片
img = cv.imread("D:\head.jpg",1)

# 显示图像
cv.imshow('Image1', img)

# 保存图像
cv.imwrite("D:/liu/image.jpg", img)  # 推荐用 .jpg、.png 等

# ********结束区********
# 等待关闭所有窗口
cv.waitKey(0)
cv.destroyAllWindows()

# ********函数解释区********
"""
语法:
# 1. image = cv2.imread(filename, flags=cv2.IMREAD_COLOR)
flags:
    cv.IMREAD_COLOR：以彩色模式加载图像，任何图像的透明度都将被忽略。这是默认参数。
    cv.IMREAD_GRAYSCALE：以灰度模式加载图像
    cv.IMREAD_UNCHANGED：包括alpha通道的加载图像模式。
    
# 2. cv2.imshow(winname, mat)
winname:
    显示窗口的名称（作为窗口的唯一标识符）。如果同名窗口已存在，则在该窗口显示
mat:
    要显示的图像数据
注意：在调用显示图像的API后，要调用cv.waitKey()给图像绘制留下时间，否则窗口会出现无响应情况，并且图像无法显示出来。

# 3. cv2.imwrite(filename, img, params=None)
params:
    编码参数，用于控制保存质量、压缩率等，具体参数取决于图像格式。
    自己搜,不必须
"""
# ****************项目区****************
# 解释:1. 增加了图片展示格式 2. 增加了图片显示格式 3. 增加了按键动作 
# ********导入库********
import numpy as np
import cv2 as cv

# ********功能区********
# 加载一张图片
img_IMREAD_COLOR = cv.imread("D:\head.jpg",cv.IMREAD_COLOR)         # 彩色格式
img_IMREAD_GRAYSCALE = cv.imread("D:\head.jpg",cv.IMREAD_GRAYSCALE) # 灰度图格式
img_IMREAD_UNCHANGED = cv.imread("D:\head.jpg",cv.IMREAD_UNCHANGED) # alpha通道格式
# 显示图像
cv.imshow('Image1', img_IMREAD_COLOR)       # 直接显示

cv.namedWindow('Image2', cv.WINDOW_NORMAL)  # 先创建窗口
cv.imshow('Image2', img_IMREAD_GRAYSCALE)   # 直接显示

cv.namedWindow('Image3', cv.WINDOW_NORMAL)  # 先创建窗口
cv.imshow('Image3',img_IMREAD_UNCHANGED)    # 再展示图像

# 保存图像
cv.imwrite("D:/liu/Image1.jpg", img_IMREAD_COLOR)  # 推荐用 .jpg、.png 等

# ********结束区********
# 等待关闭所有窗口
key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
elif key == ord('g'):
    cv.imwrite("D:/liu/Image2.jpg", img_IMREAD_GRAYSCALE)
    cv.destroyAllWindows()
elif key == ord('c'):
    cv.imwrite("D:/liu/Image3.jpg", img_IMREAD_UNCHANGED)
    cv.destroyAllWindows()
elif key == ord('a'):
    print('hello world')
    cv.destroyAllWindows()
else:
    cv.destroyAllWindows()