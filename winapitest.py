import win32api
import time

while True:
    if win32api.GetAsyncKeyState(0x01) < 0:
        print("click")
        time.sleep(.49)