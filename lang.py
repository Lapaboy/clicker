import ctypes
import win32api

_LAYOUTS = {
    '0x409': 'en',
    '0x419': 'ru'
}

def _getHeximalKeyboadrLayout():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2**16 - 1)
    return hex(lid)

def getKeyboardLayout():
    return _LAYOUTS[_getHeximalKeyboadrLayout()]

def switchKeyboardLayoutTo(code):
    hex_id = list(_LAYOUTS.keys())[list(_LAYOUTS.values()).index(code)]
    win32api.LoadKeyboardLayout('00000' + hex_id.replace('0x', ''), 1)