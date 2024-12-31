import speech_recognition
from pynput.keyboard import Key, Controller
import sys
import pyaudio
import pyttsx3

recognizer = speech_recognition.Recognizer()
keyboard = Controller()

while True:
    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            print (text)
            
            if text == "acknowledge" or text == "acknowledge landing clearance" or text == "acknowledge go around" or text == "acknowledge taxi clearance" or text == "announce position" or text == "acknowledge taxi":
                keyboard.press('1')
                keyboard.release('1')
            elif text == "say again" or text == "announce on final" or text == "request directions to the airport" or text == "announce taxi":
                keyboard.press('2')
                keyboard.release('2')
            elif text == "announce on upwind leg" or text == "announce taxi to parking":
                keyboard.press('3')
                keyboard.release('3')
            elif text == "announce on upwind leg":
                keyboard.press('4')
                keyboard.release('4')
            elif text == "exit" or text == "quit":
                sys.exit()


    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue