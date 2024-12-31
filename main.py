import speech_recognition
from pynput.keyboard import Key, Controller
import pyaudio
import pyttsx3

recognizer = speech_recognition.Recognizer()
keyboard = Controller()

while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.0)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            print (text)
            if text == "say again":
                keyboard.press('2')
                keyboard.release('2')

            elif text == "acknowledge":
                keyboard.press('1')
                keyboard.release('1')


    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue