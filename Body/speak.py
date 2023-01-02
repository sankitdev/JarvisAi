#windows based - pyttsx3
#chrome Based - selenium

import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5") #sapi5 is microsoft speech API
    voices = engine.getProperty('voices')
    #for voice in voices: (using this we can loop all the avaialble voices in windows)
    engine.setProperty('voice', voices[0].id) #set the id 0 (male) and 1 (female)
    engine.setProperty('rate', 160)
    print(f"You : {Text}.")
    engine.say(Text)
    engine.runAndWait()


