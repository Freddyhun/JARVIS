## LINK TO MODEL: https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
## FILES INSIDE THE ARCHIVE GO IN .\model

import vosk
import os
import pyttsx3
import pydirectinput
import winshell
import time
from datetime import datetime
from pyautogui import hotkey, press
import pygame
import psutil
import wave

engine = pyttsx3.init()

def process_status(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

class SpeechModel:
    _instance = None

    @classmethod
    def get_model(cls, path=".\\model"):
        if cls._instance is None:
            cls._instance = vosk.Model(path)
        return cls._instance

# load pygame
pygame.mixer.init()

# Load the Vosk model once
model = SpeechModel.get_model()

def capture_voice_input():
    """Capture audio input from the microphone and save it as a WAV file."""
    import sounddevice as sd
    import numpy as np

    print("Listening...")
    duration = 5  # seconds
    fs = 32000  # Sampling frequency
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the recording to a WAV file
    temp_filename = "temp_audio.wav"
    with wave.open(temp_filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())

    return temp_filename

def convert_voice_to_text(audio_file):
    """Convert recorded audio to text using Vosk."""
    try:
        recognizer = vosk.KaldiRecognizer(model, 32000)
        with wave.open(audio_file, "rb") as wf:
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    text = eval(result)["text"]
                    print("You said:", text)
                    return text
    except Exception as e:
        print("Error recognizing speech:", e)
    return ""

now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
if int(current_time[0:2]) < 12:
    print("Good morning, sir.")
    try:
        pygame.mixer.music.load('.\\sounds\\goodmorning.mp3')
        pygame.mixer.music.play()
    except:
        print("Error playing sound.")
elif int(current_time[0:2]) > 12 and int(current_time[0:2]) < 18:
    print("Good afternoon, sir.")
    try:
        pygame.mixer.music.load('.\\sounds\\goodafternoon.mp3')
        pygame.mixer.music.play()
    except:
        print("Error playing sound.")
elif int(current_time[0:2]) > 18:
    print("Good evening, sir.")
    try:
        pygame.mixer.music.load('.\\sounds\\goodevening.mp3')
        pygame.mixer.music.play()
    except:
        print("Error playing sound.")

def process_voice_command(text):
    if "jarvis" in text.lower():
        if "clip" in text.lower():
            print("Yes, sir. Clipped.")
            hotkey('alt','f10')
            try:
                    pygame.mixer.music.load('.\\sounds\\clip.mp3')
                    pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "mute" in text.lower():
            print("Yes, sir. Muting you on discord.")
            press('f17')
            try:
                pygame.mixer.music.load('.\\sounds\\mute.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "record" in text.lower():
            print("Yes, sir. Recording.")
            hotkey('alt','f9')
            try:
                pygame.mixer.music.load('.\\sounds\\record.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "close this game" in text.lower():
            print('Yes, sir. Attempting to close the game.')
            hotkey('alt','f4')
            try:
                pygame.mixer.music.load('.\\sounds\\close.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "maximum" in text.lower():
            print("Yes, sir. Maximum pulse.")
            pydirectinput.keyDown('q')
            pydirectinput.keyUp('q')
            try:
                pygame.mixer.music.load('.\\sounds\\maximumpulse.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "open rival" in text.lower():
            print("Yes, sir. Opening Marvel Rivals.")
            os.system("start steam://rungameid/2767030")
            try:
                pygame.mixer.music.load('.\\sounds\\open.mp3')
                pygame.mixer.music.play()
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
                pygame.mixer.music.load('.\\sounds\\recyclebin.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "connect to server" in text.lower():
            print("Yes, sir. Connecting to server.")
            os.system("start %windir%\\system32\\mstsc.exe")
            time.sleep(1)
            press('enter')
            try:    
                pygame.mixer.music.load('.\\sounds\\connect.mp3')
                pygame.mixer.music.play()
            except:
                print("Error playing sound.")

        elif "make a meme" in text.lower():
            print("Yes, sir. Getting the template ready.")
            try:
                os.startfile(".\\other\\jarvis.psd")
                pygame.mixer.music.load('.\\sounds\\meme.mp3')
                pygame.mixer.music.play()
            except:
                print("Couldn't open template, sir.")

        else:
            print("Sorry sir, I didn't understand that.")
            try:
                pygame.mixer.music.load('.\\sounds\\error.mp3')
                pygame.mixer.music.play()
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