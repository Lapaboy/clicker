import win32api, win32con, win32gui
import time
from vkkeycodes import VK_CODE

delay = .05

def set_cursor(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE, x, y, x, y)

def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def press(char):
    win32api.keybd_event(VK_CODE[char], 0, 0, 0)
    time.sleep(delay)
    win32api.keybd_event(VK_CODE[char], 0, win32con.KEYEVENTF_KEYUP, 0)

def _leftShiftPress(char):
    win32api.keybd_event(VK_CODE['left_shift'], 0, 0, 0)
    win32api.keybd_event(VK_CODE[char], 0, 0, 0)
    time.sleep(delay)
    win32api.keybd_event(VK_CODE['left_shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(VK_CODE[char], 0, win32con.KEYEVENTF_KEYUP, 0)

def typer(string):
    for char in string:
        if char == '!':
            _leftShiftPress('1')
        elif char == '@':
            _leftShiftPress('2')
        elif char == '{':
            _leftShiftPress('[')
        elif char == '?':
            _leftShiftPress('/')
        elif char == ':':
            _leftShiftPress(';')
        elif char == '"':
            _leftShiftPress('\'')
        elif char == '}':
            _leftShiftPress(']')
        elif char == '#':
            _leftShiftPress('3')
        elif char == '$':
            _leftShiftPress('4')
        elif char == '%':
            _leftShiftPress('5')
        elif char == '^':
            _leftShiftPress('6')
        elif char == '&':
            _leftShiftPress('7')
        elif char == '*':
            _leftShiftPress('8')
        elif char == '(':
            _leftShiftPress('9')
        elif char == ')':
            _leftShiftPress('0')
        elif char == '_':
            _leftShiftPress('-')
        elif char == '=':
            _leftShiftPress('+')
        elif char == '~':
            _leftShiftPress('`')
        elif char == '<':
            _leftShiftPress(',')
        elif char == '>':
            _leftShiftPress('.')

        elif char == ' ':
            press('spacebar')
        elif char.istitle(): 
            _leftShiftPress(char.lower())
        else:    
            press(char)
