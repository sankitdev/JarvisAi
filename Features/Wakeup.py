import sys
sys.path.append('E:/ankitai')
from Body.Speak import Speak
from Body.Listen import MicExecution
def wakeup_detected():
    while True:
        query = MicExecution().lower()
        if "hello baby" in query or "hello, baby" in query:
            Speak("Yes, I'm listening. How can I help you?")
            return True
        else:
            Speak("I don't recognize you.")
            return False

