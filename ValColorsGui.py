from time import time
from win32gui import GetWindowText, GetForegroundWindow
import pyperclip
import random
import time
import ctypes
from pynput.keyboard import Key, Controller
from pynput import keyboard
import os

kb = Controller()

def on_press(key):
    if key == keyboard.Key.shift_r:
        if GetWindowText(GetForegroundWindow()) == 'VALORANT  ':

            kb.release(Key.shift_r)
            kb.press(Key.ctrl)
            kb.press('a')
            time.sleep(0.001)
            kb.release('a')
            kb.release(Key.ctrl)

            kb.press(Key.ctrl)
            kb.press('x')
            time.sleep(0.001)
            kb.release('x')
            kb.release(Key.ctrl)

            latest = ''
            colors = ['&lt;enemy>', '&lt;system>', '&lt;notification>', '&lt;team>', '&lt;warning>', '&lt;team>', '&lt;notification>', '&lt;system>']
            output = ''

            mode = 'rainbow'

            s = pyperclip.paste()

            if mode == 'random':
                for i in s:
                    if i != ' ':
                        rand = random.choice(colors)
                        while rand == latest:
                            rand = random.choice(colors)
                        latest = rand
                        output += rand + i + '&lt;/>'
                    else:
                        output += ' '

            elif mode == 'rainbow':
                counter = 0
                for i in s:
                    if i != ' ':
                        output += colors[counter % len(colors)] + i + '</>'
                        counter += 1
                    else:
                        output += ' '


            print('input: '+s)
            print('output: '+output)
            pyperclip.copy(output)
            kb.press(Key.ctrl)
            kb.press('v')
            kb.release('v')
            kb.release(Key.ctrl)

            kb.press(Key.enter)
            kb.release(Key.enter)

ctypes.windll.user32.MessageBoxW(0, "Application successfully injected.\n\nPress RSHIFT instead of ENTER to send a clored message!\nKill process in taskmanager to stop the application.", "Valorant Chat Color", 0)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
