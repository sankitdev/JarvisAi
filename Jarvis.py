from Features.Wakeup import wakeup_detected
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
from Body.Speak import Speak
from Features.Open import OpenExe

def MainExecution():
    while True:
        Data = MicExecution()
        Data = str(Data).replace("", "")

        if "exit" in Data or "Exit." in Data or "Exit Right now" in Data or "Goodbye" in Data:
            Speak("Goodbye Sir")
            break

        elif len(Data) < 3:
            pass

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:
            Speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)
            
        elif "open" in Data or "start" in Data or "launch" in Data or "visit" in Data:
            if OpenExe(Data):
                Speak("Ok, opening it now")
            else:
                Speak("Sorry, I could not open it")
        
        elif "play" in Data or "search" in Data:
            if OpenExe(Data):
                Speak(f"Playing {Data.replace('play', '').replace('search', '')}")
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

    Speak("Exiting...")

def run_program():
    assistant_has_spoken = False
    continue_running = wakeup_detected()
    if not continue_running:
        if not assistant_has_spoken:
            Speak("You are not the real one baby. Good bye")
        return
    assistant_has_spoken = True
    MainExecution()

if __name__ == "__main__":
    run_program()
