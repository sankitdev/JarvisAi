from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.listen import Mic_connect
print(">> Starting the jarvis : Wait for some seconds..")
from Body.speak import Speak
#from Features.Clap import Tester
print(">> Starting the Jarvis : Wait For Few Seconds More")

def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready To Assist you sir.")
    while True:
        Data = Mic_connect()
        Data = str(Data)

        if len(Data)<3:
            pass

        elif "what is" in Data or "where is" in Data or "questions" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

MainExecution()


