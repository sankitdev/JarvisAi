# Import necessary libraries
import wikipedia
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and rate
engine.setProperty('voice', 'en-us')
engine.setProperty('rate', 150)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning, sir.")
    elif hour>=12 and hour<18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")

# Function to take command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

#Function to wakeup
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
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    query = Listen().lower()

    if "hello jarvis" in query:
        os.startfile(r"E:\A.I Jarvis using python\main.py")
       
    else:
        pass

WakeupDetected() 

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        # Logic to execute tasks based on the command
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia, " + results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")
        elif "exit" in query:
            speak("Exiting, sir.")
            exit()