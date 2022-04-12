import re
from pynput.keyboard import  Key, Controller
import time
keyboard = Controller()
time.sleep(4)

for i in range(0, 100):
    i = str(i)
    keyboard.type(i)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('a')
        keyboard.press(Key.backspace)