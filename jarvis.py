## LINK TO MODEL: https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
## FILES INSIDE THE ARCHIVE GO IN .\model

import vosk
import pyttsx3
from datetime import datetime
from pyautogui import hotkey, press
import pygame
import wave

engine = pyttsx3.init()

class SpeechModel:
    _instance = None

    @classmethod
    def get_model(cls, path=".\\model"):
        if cls._instance is None:
            cls._instance = vosk.Model(path)
        return cls._instance

# load pygame
pygame.mixer.init()

# load the Vosk model once
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
current_hour = int(current_time[0:2])
match current_hour:
    case current_hour if current_hour < 12:
        print("Good morning, sir.")
        try:
            pygame.mixer.music.load('.\\sounds\\goodmorning.mp3')
            pygame.mixer.music.play()
        except:
            print("Error playing sound.")
    case current_hour if current_hour > 12 and current_hour < 18:
        print("Good afternoon, sir.")
        try:
            pygame.mixer.music.load('.\\sounds\\goodafternoon.mp3')
            pygame.mixer.music.play()
        except:
            print("Error playing sound.")
    case current_hour if current_hour > 18:
        print("Good evening, sir.")
        try:
            pygame.mixer.music.load('.\\sounds\\goodevening.mp3')
            pygame.mixer.music.play()
        except:
            print("Error playing sound.")

from commands import process_voice_command

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)
        engine.runAndWait()

if __name__ == "__main__":
    main()