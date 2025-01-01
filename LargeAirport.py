import speech_recognition
from pynput.keyboard import Controller
import subprocess
import sys

recognizer = speech_recognition.Recognizer()
keyboard = Controller()

print("Running Large")

# Adjust microphone sensitivity once outside the loop
with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=0.5)
    print("Microphone calibrated. Listening for commands...")

    while True:
        try:
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio).lower()
            print(text)

            if text in ["acknowledge", "acknowledge landing clearance", "acknowledge go around",
                        "acknowledge taxi clearance", "acknowledge taxi", "acknowledge radar contact",
                        "tune atis", "request pushback", "request pushback stop", "acknowledge takeoff clearance",
                        "acknowledge frequency change", "acknowledge pattern entry instructions", "acknowledge pattern entry instruction",
                        "acknowledge ground hand off"]:
                keyboard.press('1')
                keyboard.release('1')
            elif text in ["say again", "request directions to the airport", "announce taxi", 
                          "request fuel supply", "request fuel supply end", "request push back steer to the left",
                          "request touch and go"]:
                keyboard.press('2')
                keyboard.release('2')
            elif text in ["announce taxi to parking", "request power supply", "request power supply end", "request push back steer to the right", 
                          "request pushback push straight", "request push back to push straight", "request full stop landing", "request taxi to parking"]:
                keyboard.press('3')
                keyboard.release('3')
            elif text in ["request passenger boarding start", "request passenger boarding stop"]:
                keyboard.press('4')
                keyboard.release('4')
            elif text in ["request baggage service", "request baggage service end", "request baggage service stop"]:
                keyboard.press('5')
                keyboard.release('5')
            elif text in ["request catering service", "request catering service end", "request catering service stop"]:
                keyboard.press('6')
                keyboard.release('6')
            elif text in ["exit", "quit"]:
                print("Exiting...")
                sys.exit()
            elif text == "small":
                print("Launching SmallAirport.py...")
                subprocess.run(["python3", "SmallAirport.py"])
                sys.exit()

        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
        continue
