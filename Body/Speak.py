# Speak Functions - Two Speak Functions

# Windows Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

# Windows Based
# Advantages = Fast , Offline.
# Disadvantages =  OverSpeak , Less Voices.

import pyttsx3


def Speak(text="", lang="en"):
    """
    Convert text to speech using the pyttsx3 library.

    Args:
        text (str): The text to convert to speech.
        lang (str): The language of the text. Defaults to "en" (English).

    Returns:
        None
    """
    try:
        engine = pyttsx3.init("sapi5")
        if lang == "en":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
        elif lang == "hi":
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hiIN_HemantM"
            engine.setProperty('voice', voice_id)
        engine.setProperty('rate', 170)
        print(f"\nYou: {text}.")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"\nError: {e}. Please try again.")


