#listen function 
#it will listen in both hindi and english  
#it will contain 3 functions

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans

#1 Creating listen function : hindi and English

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,6) #lclearistening mode..
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi") #hi means hindi
    except: 
        return ""
    query = str(query)
    return query.lower()

#2 - Translation

def TranslationHinToEng(Text):
    data = str(Text) #it converts the text into string, by default it is in string but just to avoid error we are again converting it to string
    translator = Translator() #here translate is variable and we are calling the Traslator
    result = translator.translate(data, src= 'hi', dest='en' )
    data = result.text
    print(f"You : {data}.")
    return data

#Mic Connect

def Mic_connect():
    query = Listen() #everything will be stored in query variable
    data = TranslationHinToEng(query)
    return data
    
Listen()

