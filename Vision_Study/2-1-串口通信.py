import serial
import cv2 as cv

# win使用com1连接串行口
ser=serial.Serial("COM6",115200,timeout=0.5)

#打印设备名称
print(ser.name)
#打印设备名
print(ser.port)
# 检查是否连接
print(ser.isOpen())
# 发送数据
ser.write(b"send")  # 不带\n则接收端也不会检测到\n
# 读取数据
while True:
    data = ser.readline()
    print(data)
