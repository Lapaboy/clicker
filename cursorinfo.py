import win32gui
from time import sleep

while True:
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    print(x, y)
    sleep(0.1)
