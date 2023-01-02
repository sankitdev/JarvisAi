import speech_recognition as sr
import os
from jarvis import MainExe

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,6) #lclearistening mode..
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en") 
    except: 
        return ""
    query = str(query).lower
    print(query)
    return query

def WakeupDetected():
    queery = Listen().lower()    

    if "hello jarvis" in queery:
        MainExe()
    else:
        pass
    
while True:
    WakeupDetected()