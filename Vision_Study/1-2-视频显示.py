# 1-2 视频显示 2025.10.27
# 导入库
import numpy as np
import cv2 as cv

# 选择摄像头路径
cap = cv.VideoCapture(0)    # 这里换成视频地址就可以播放视频

# 使用循环使得视频变帧图:
while True:
    ret, frame = cap.read()  # 读取一帧
    if not ret:
        print("读取帧失败或摄像头断开")
        break
    # 处理图像,彩色转灰度
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Camera", gray)  # 显示当前帧

    if cv.waitKey(1) & 0xFF == 27:  # 按 ESC 键退出
        break

# 释放资源
cap.release()
cv.destroyAllWindows()

'''
语法:
------
1. cv2.VideoCapture(index_or_filename, apiPreference=None)
@ 打开摄像头或视频文件
* index_or_filename: 整数表示编号(摄像头编号,0为内置) / 字符串(如'video.mp4')即为视频文件
* apiPreference : 视频捕获后端 API 的偏好值（一般可以省略，使用默认即可）

2. cap.isOpened()
@ 判断摄像头或视频文件是否成功打开,避免程序报错
# 返回bool

3. ret, frame = cap.read()
@ 从摄像头或视频文件获取帧
* ret : 布尔值，表示是否成功读取一帧
* frame: 读取到的图像帧（NumPy ndarray）

4. value = cap.get(propId)
@ 获取摄像头或视频流属性
* propId : 要获取的属性 ID，OpenCV 提供了一系列常用的属性常量,自己查(如帧宽高帧率,时间戳,亮度,对比度等)
! : 返回值为浮点数,如果需要整数，需用 int() 转换

5. cap.set(propId, value)
@ 设置摄像头或视频流属性
* value : 设置的值（float），例如 640.0、30.0 等

6. dst = cv.cvtColor(src, code)
* src : 输入图像（NumPy ndarray）
* dst : 输出图像（转换后的图像矩阵）
* code : 颜色空间转换的代码，例如 BGR → GRAY、BGR → RGB 等:
//
cv2.COLOR_BGR2GRAY	BGR 彩色 → 灰度图
cv2.COLOR_BGR2RGB	BGR → RGB（OpenCV 默认读取为 BGR）
cv2.COLOR_RGB2BGR	RGB → BGR
cv2.COLOR_BGR2HSV	BGR → HSV（色调、饱和度、明度）
cv2.COLOR_BGR2LAB	BGR → Lab 颜色空间
cv2.COLOR_GRAY2BGR	灰度 → BGR 彩色图
//

!!! : OpenCV 默认读入彩色图像为 BGR，不是 RGB。


7. cap.release()
@! : 释放资源

------
1. 播放视频文件
! : 需要进行waitKey延时,使得视频流畅

2. 保存视频
@ 自己查
'''
