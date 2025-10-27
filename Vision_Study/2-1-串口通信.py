import cv2 as cv
import keyboard
import time
import serial

# STM32串口连接
try:
    ser = serial.Serial("COM6", 115200, timeout=0.1)  # 缩短超时时间
    print(f"串口打开成功: {ser.name}")
except serial.SerialException as e:
    print("串口打开失败:", e)
    exit()

# 初始发送
ser.write(b"send")
print("初始握手信号已发送")

try:
    while True:
        # 1. 检测按键发送数据
        if keyboard.is_pressed('s'):
            ser.write(bytes([0x12,0x11,0x13,0x14]))  # 发送4个字节
            print("已发送字节数据")
            time.sleep(0.2)  # 防抖，但缩短时间

        # 2. 非阻塞读取串口数据并回显
        if ser.in_waiting > 0:
            data = ser.readline()
            if data:
                print("接收到数据:")
                print(data.strip())

        # 3. 退出机制
        if keyboard.is_pressed('esc'):
            print("退出程序")
            break
        
        # 4. 短暂延迟减少CPU占用
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("程序被用户中断")
except Exception as e:
    print(f"程序出错: {e}")
finally:
    # 确保串口关闭
    ser.close()
    print("串口已关闭")

'''
语法:
1.ser = serial.Serial("串口号", 波特率, timeout=超时时间(s))
@ 初始化串口

2. ser.write(data)
@ 向串口发送二进制字节数据
* data:要发送的数据（必须是字节序列）
! 如果是字符串，必须先使用 .encode() 转换为字节类型 / 前缀加b
# return 发送成功的字节数

$
# 初始建立可变的字节array
frame = bytearray([0x12, 0x34, 0x56, 0x78])
# 进行相关操作
frame.insert(2, 0xAB)  # 在索引2位置插入0xAB ,即中间插入一个
frame.extend([0x34, 0x56, 0x78]) # 尾部插入多个字节
frame[1] = 0xAB     # 修改第2个字节
del frame[1]        # 删除字节 
# 通过串口发送(先转化为bytes!!!)
ser.write(bytes(frame))
$

3. ser.in_waiting
@ 用来判断当前接收缓冲区里有多少数据
$
if ser.in_waiting:
    line = ser.readline()
    print("接收:", line.decode(errors="ignore"))
$

4. data = ser.read(size=1)
@ 从串口接收 固定字节数 的数据，返回 bytes 类型
# return ：实际读取的字节数据

5. line = ser.readline()
@ 读取 一行数据，直到遇到换行符 \n 或超时

'''