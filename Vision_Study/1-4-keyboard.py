# 1-4 按键操作 2025.10.28
import keyboard
import time
import cv2 as cv

def shoot():
    print("w+s按下")

# 按键阻塞,等待命令
print("等待按下b键开始")
keyboard.wait('b')
print("开始执行逻辑(按下ESC键退出)")

# 注册热键,按下触发回调功能
keyboard.add_hotkey("w+s", shoot)

# while
while True:
    if keyboard.is_pressed('s'):
        print("S pressed!")
        time.sleep(0.2) # 防抖
    elif keyboard.is_pressed('esc'):
        print('退出')
        break
    


'''
语法:
1. keyboard.is_pressed(key)
@ 检测某个键是否被按下
* Key可以是's'也可以是'esc'

2. keyboard.wait(key)
@ 阻塞程序，直到按下指定键才继续

3. keyboard.add_hotkey(hotkey, callback)
@ 定义组合快捷键
* hotkey:热键:字符串,比如'ctrl+shift+s'
* callback:无参数的回调函数
! 在main调用注册,后面按下之后会自动回调

4. keyboard.unhook_all_hotkeys()
@ 解除所有热键
'''