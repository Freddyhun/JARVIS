import pygame
from pyautogui import hotkey, press
import os
import time
import pydirectinput
import winshell
import psutil

def process_status(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def process_voice_command(text):
    match text.lower():
        case jarvis if "jarvis" in text.lower():
            match text.lower():
                case clip if "clip" in text.lower():
                    print("Yes, sir. Clipped.")
                    hotkey('alt','f10')
                    try:
                        pygame.mixer.music.load('.\\sounds\\clip.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case mute if "mute" in text.lower():
                    print("Yes, sir. Muting you on discord.")
                    press('f17')
                    try:
                        pygame.mixer.music.load('.\\sounds\\mute.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case record if "record" in text.lower():
                    print("Yes, sir. Recording.")
                    hotkey('alt','f9')
                    try:
                        pygame.mixer.music.load('.\\sounds\\record.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case close if "close" in text.lower():
                    print('Yes, sir. Attempting to close the game.')
                    hotkey('alt','f4')
                    try:
                        pygame.mixer.music.load('.\\sounds\\close.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case maximum if "maximum pulse" in text.lower():
                    print("Yes, sir. Maximum pulse.")
                    pydirectinput.keyDown('q')
                    pydirectinput.keyUp('q')
                    try:
                        pygame.mixer.music.load('.\\sounds\\maximumpulse.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case rival if "rival" in text.lower():
                    print("Yes, sir. Opening Marvel Rivals.")
                    os.system("start steam://rungameid/2767030")
                    try:
                        pygame.mixer.music.load('.\\sounds\\open.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")
            
                case music if "music" in text.lower():
                    print("Yes, sir. Playing music.")
                    if process_status("AutoHotkeyU64.exe"):
                        print("AHK script already running.")
                    else:
                        print("Starting AHK script.")
                        os.startfile(".\\other\\media.ahk")

                        pydirectinput.keyDown('ctrl')
                        pydirectinput.keyDown('alt')
                        pydirectinput.keyDown('down')
                        pydirectinput.keyUp('ctrl')
                        pydirectinput.keyUp('alt')
                        pydirectinput.keyUp('down')
                        # try:
                        #     playsound('.\sounds\music.mp3')
                        # except:
                        #     print("Error playing sound.")
                        ## todo: actually add the sound file
                        ## there is DEFINITELY a better way to do this, this also requires an ahk script to be running, but im lazy
                        ## update: this still sucks but I found a way to force it to run the AHK script if it isnt running already, so.. slightly better but still bad?
                        ## still not sure if I should add a sound file for this or how to phrase it

                case recyclebin if "recycle bin" in text.lower():
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    print("Yes, sir. Emptying the recycle bin.")
                    try:
                        pygame.mixer.music.load('.\\sounds\\recyclebin.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case connect if "connect" in text.lower():
                    print("Yes, sir. Connecting to server.")
                    os.system("start %windir%\\system32\\mstsc.exe")
                    time.sleep(1)
                    press('enter')
                    try:    
                        pygame.mixer.music.load('.\\sounds\\connect.mp3')
                        pygame.mixer.music.play()
                    except:
                        print("Error playing sound.")

                case meme if "meme" in text.lower():
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