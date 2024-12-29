## LINK TO MODEL: https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
## FILES INSIDE THE ARCHIVE GO IN .\model

import vosk
import os
import pyttsx3
import speech_recognition as sr
from pyautogui import hotkey, press
from playsound import playsound
import pydirectinput
import winshell
import time
from datetime import datetime
import psutil

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def process_status(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

# model = vosk.Model(".\\model")
## loads the model first otherwise it takes 3 years to recognize the first command
## update: the model is sentient so it loads again
## ????????????????????????????????????????????????????????????????????????????????????????

now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
if int(current_time[0:2]) < 12:
    print("Good morning, sir.")
    try:
        playsound('.\\sounds\\goodmorning.mp3')
    except:
        print("Error playing sound.")
elif int(current_time[0:2]) > 12 and int(current_time[0:2]) < 18:
    print("Good afternoon, sir.")
    try:
        playsound('.\\sounds\\goodafternoon.mp3')
    except:
        print("Error playing sound.")
elif int(current_time[0:2]) > 18:
    print("Good evening, sir.")
    try:
        playsound('.\\sounds\\goodevening.mp3')
    except:
        print("Error playing sound.")

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_vosk(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I don't understand. P.S. Say 'Jarvis'")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def process_voice_command(text):
    if "jarvis" in text.lower():
        if "clip" in text.lower():
            print("Yes, sir. Clipped.")
            hotkey('alt','f10')
            try:
                playsound('.\\sounds\\clip.mp3')
            except:
                print("Error playing sound.")

        elif "mute" in text.lower():
            print("Yes, sir. Muting you on discord.")
            press('f17')
            try:
                playsound('.\\sounds\\mute.mp3')
            except:
                print("Error playing sound.")

        elif "record" in text.lower():
            print("Yes, sir. Recording.")
            hotkey('alt','f9')
            try:
                playsound('.\\sounds\\record.mp3')
            except:
                print("Error playing sound.")

        elif "close this game" in text.lower():
            print('Yes, sir. Attempting to close the game.')
            hotkey('alt','f4')
            try:
                playsound('.\\sounds\\close.mp3')
            except:
                print("Error playing sound.")

        elif "maximum" in text.lower():
            print("Yes, sir. Maximum pulse.")
            pydirectinput.keyDown('q')
            pydirectinput.keyUp('q')
            try:
                playsound('.\\sounds\\maximumpulse.mp3')
            except:
                print("Error playing sound.")

        elif "open rival" in text.lower():
            print("Yes, sir. Opening Marvel Rivals.")
            os.system("start steam://rungameid/2767030")
            try:
                playsound('.\\sounds\\open.mp3')
            except:
                print("Error playing sound.")
        
        elif "music" in text.lower():
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

        elif "empty recycle bin" in text.lower():
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            print("Yes, sir. Emptying the recycle bin.")
            try:
                playsound('.\\sounds\\recyclebin.mp3')
            except:
                print("Error playing sound.")

        elif "connect to server" in text.lower():
            print("Yes, sir. Connecting to server.")
            os.system("start %windir%\system32\mstsc.exe")
            time.sleep(1)
            press('enter')
            try:    
                playsound('.\\sounds\\connect.mp3')
            except:
                print("Error playing sound.")

        elif "make a meme" in text.lower():
            print("Yes, sir. Getting the template ready.")
            try:
                os.startfile(".\\other\\jarvis.psd")
                playsound('.\sounds\meme.mp3')
            except:
                print("Couldn't open template, sir.")

        else:
            print("Sorry sir, I didn't understand that.")
            try:
                playsound('.\\sounds\\error.mp3')
            except:
                print("Error playing sound.")
        return
    else:
        print("Sorry, I don't understand. P.S. Say 'Jarvis'")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)
        engine.runAndWait()

if __name__ == "__main__":
    main()