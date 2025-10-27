import numpy as np
import cv2 as cv

# 创建一个黑色画布
img = np.zeros((512,512,3), np.uint8)

# 开始绘制图像
# 1. 直线
cv.line(img,(0,0),(512,512),(255,255,255),2)
# 2. 矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
# 3. 圆形
cv.circle(img,(447,63), 63, (0,0,255), -1)
# 4.文本
fontFace = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), fontFace, 4,(255,255,255),2,cv.LINE_AA)


# 展示画布
cv.imshow('img', img)
# 结束显示
cv.waitKey(0)
cv.destroyAllWindows()
'''
语法:
1. 绘制直线:
# 参数:画布    起点     终点       RGB     线条粗细
cv.line(img,(0,0),(512,512),(255,255,255),2)  

2. 绘制矩形 ** 最后一个参数如果为-1则代表填充 **
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

3. 绘制圆形
cv.circle(img,(447,63), 63, (0,0,255), -1)

4. 绘制椭圆,略
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

5. 绘制多边形,略
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

6. 添加文本
font = cv.FONT_HERSHEY_SIMPLEX
           图像   文本 字体位置(默认左下角) 字体类型 size rgb  thickness 线条类型(AA挺好)
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
'''