import os
import time
import playsound
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    #Setting the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    #Text input
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        r.adjust_for_ambient_noise(source, duration = 5)
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
        
    return said

print((sr.Microphone.list_microphone_names()))
text = "Start speaking."
speak(text)
get_audio()