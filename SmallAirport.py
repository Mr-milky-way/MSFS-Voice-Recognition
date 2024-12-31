import speech_recognition
from pynput.keyboard import Controller
import subprocess
import sys

recognizer = speech_recognition.Recognizer()
keyboard = Controller()

print("Running Small")

# Adjust ambient noise once outside the loop
with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.5)
    print("Microphone calibrated. Listening for commands...")

    while True:
        try:
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio).lower()
            print(text)

            if text == "large":
                print("Switching to LargeAirport.py...")
                subprocess.run(["python3", "LargeAirport.py"])
                sys.exit()
            elif text in ["exit", "quit"]:
                print("Exiting...")
                sys.exit()
            elif text in ["acknowledge", "acknowledge landing clearance", "acknowledge go around", 
                          "acknowledge taxi clearance", "announce position", "acknowledge taxi", 
                          "acknowledge radar contact", "announce taxi"]:
                keyboard.press('1')
                keyboard.release('1')
            elif text in ["say again", "announce on final"]:
                keyboard.press('2')
                keyboard.release('2')
            elif text == "announce on upwind leg":
                keyboard.press('3')
                keyboard.release('3')
            elif text in ["announce on crosswinds leg", "announce on crosswind leg"]:
                keyboard.press('4')
                keyboard.release('4')

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
        continue
