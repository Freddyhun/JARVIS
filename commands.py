import pygame
from pyautogui import hotkey, press
import os
import time
import pydirectinput
import winshell
import psutil
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY

def process_status(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def process_voice_command(text):
    match text.lower():
        case jarvis if "jarvis" in text.lower():
            match text.lower():
                case "clip" if "clip" in text.lower():
                    print("Yes, sir. Clipped.")
                    hotkey('alt','f10')
                    try:
                        pygame.mixer.music.load('.\\sounds\\clip.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")
                        
                case "mute" if "mute" in text.lower():
                    print("Yes, sir. Muting you on discord.")
                    press('f17')
                    try:
                        pygame.mixer.music.load('.\\sounds\\mute.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "record" if "record" in text.lower():
                    print("Yes, sir. Recording.")
                    hotkey('alt','f9')
                    try:
                        pygame.mixer.music.load('.\\sounds\\record.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "close" if "close" in text.lower():
                    print('Yes, sir. Attempting to close the game.')
                    hotkey('alt','f4')
                    try:
                        pygame.mixer.music.load('.\\sounds\\close.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "maximum" if "maximum pulse" in text.lower():
                    print("Yes, sir. Maximum pulse.")
                    pydirectinput.keyDown('q')
                    pydirectinput.keyUp('q')
                    try:
                        pygame.mixer.music.load('.\\sounds\\maximumpulse.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "rival" if "rival" in text.lower():
                    print("Yes, sir. Opening Marvel Rivals.")
                    os.system("start steam://rungameid/2767030")
                    try:
                        pygame.mixer.music.load('.\\sounds\\open.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")
            
                case "music" if "music" in text.lower():
                    print("Yes, sir. Playing music.")
                    try:
                        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
                    except:
                        print("Error playing music.")

                case "recyclebin" if "recycle bin" in text.lower():
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    print("Yes, sir. Emptying the recycle bin.")
                    try:
                        pygame.mixer.music.load('.\\sounds\\recyclebin.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "connect" if "connect" in text.lower():
                    print("Yes, sir. Connecting to server.")
                    os.system("start %windir%\\system32\\mstsc.exe")
                    time.sleep(1)
                    press('enter')
                    try:    
                        pygame.mixer.music.load('.\\sounds\\connect.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case "meme" if "meme" in text.lower():
                    print("Yes, sir. Getting the template ready.")
                    try:
                        os.startfile(".\\other\\jarvis.psd")
                        pygame.mixer.music.load('.\\sounds\\meme.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Couldn't open template, sir.")
                case _:
                    print("Sorry sir, I didn't understand that.")
                    try:
                        pygame.mixer.music.load('.\\sounds\\error.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")
        case _:
            print("Say JARVIS.")
            print(text)
    return False