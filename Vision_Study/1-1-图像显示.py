# 1-1 图像显示 2025.10.27
# 导入库
import numpy as np
import cv2 as cv

# 加载一张图片
img = cv.imread("D:\\head.jpg", 1)

# 展示图片
cv.imshow('image.png',img)

# 关闭图片
cv.waitKey(0)
cv.destroyAllWindows()

'''
语法:
------
@ : 函数功能介绍
* : 函数参数介绍
# : 函数返回值介绍
$$:函数示例代码
! : 注意事项
------
1. img = cv2.imread(filename, flags=None)
@ 加载图片:
* filename: 文件地址
* flags : 三种选择: / cv2.IMREAD_COLOR 或 1 / cv2.IMREAD_GRAYSCALE 或 0 /  cv2.IMREAD_UNCHANGED 或 -1

2. cv2.imshow(winname, mat)
@ 展示图片
* cv2.imshow(winname, mat)
* winname: 窗口的名称（字符串）。用于标识显示窗口，如果名字相同，会在原窗口更新图像
* mat: 要显示的图像矩阵（通常是 cv.imread() 读取的图像对象）

3. cv2.waitKey(delay=0)
@ 读取按键键码,等待用户输入
* delay : 等待时间(单位：毫秒 ms)表示程序暂停多长时间等待键盘输入。如果设为 0,则无限等待用户按键。
# 返回按键的ASCII码
$
key = cv.waitKey(0)
if key == 27:  # ESC 退出
    break
elif key == ord('s'):  # s 保存图像
    cv.imwrite("save.jpg", img)
$
! : 由于imshow只是"请求显示",所以窗口会马上被销毁.因此需要waitkey进行时间延长

4. cv.destroyAllWindow()
@ 关闭所有由 cv.imshow() 创建的窗口

5. cv.destroyWindow("窗口名")
@ 单独关闭某窗口

6. cv2.namedWindow(winname, flags=cv2.WINDOW_AUTOSIZE)
@ 先创建窗口,再加载图像,这样可以调整窗口大小
* winname: 窗口名称（字符串）
* flags  : 窗口显示模式，常用值：cv2.WINDOW_NORMAL(可以手动调整窗口大小) / cv2.WINDOW_AUTOSIZE（默认）窗口大小自动匹配图像大小，不能调整。
$
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
$

7. cv2.imwrite(filename, img, params=None)
@ 保存图像到文件的函数
* filename:文件名,记得加后缀如.jpg
* params : 保存参数(如压缩质量等,自己查)
# 返回bool值
$
cv.imwrite("D:/liu/Image4.jpg" , img ) 
$

'''