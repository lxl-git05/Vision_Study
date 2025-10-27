# 导入库
import numpy as np
import cv2 as cv

# 电脑摄像头捕获
cap = cv.VideoCapture(0)    # 这里换成视频地址就可以播放视频

# 循环(展示摄像头读取的画面)
while ( cap.isOpened() ):
    # 读取是否捕获 + 图像帧
    ret, frame = cap.read()
    # 处理图像,彩色转灰度
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 展示图像
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# 释放资源
cap.release()
cv.destroyAllWindows()

'''
语法:
1. cv.VideoCapture() 
    cap = cv2.VideoCapture(index, apiPreference=None)
    一般直接cap = cv.VideoCapture(0)即可

2. cap.read()
从已打开的摄像头或视频文件中读取下一帧图像
    无参数
return : 
    ret   : 读取是否成功
    frame : 读取到的图像帧（BGR格式的三维数组），失败时为None

3. cap.get() + cap.set()
    value = cap.get(propId)
    success = cap.set(propId, value)    # 返回是否set成功
'''
