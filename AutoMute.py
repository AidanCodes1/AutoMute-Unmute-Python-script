import win32api
import win32gui
import time
from pynput import keyboard 

def mutemic():
        print ("test2.py executed")
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
        hwnd_active = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
        return

pressed = False

def on_press(key): 
    global pressed
    if not pressed and key == keyboard.Key.f1: # only if key is not held
        print('Key %s pressed' % key) 
        mutemic()
        pressed = True # key is held


def on_release(key):
    global pressed 
    if key == keyboard.Key.f1:
        print('Key %s released' %key) 
        pressed = False # key is released

with keyboard.Listener( on_press=on_press, on_release=on_release) as listener: 
    listener.join()