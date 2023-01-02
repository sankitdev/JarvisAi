import wolframalpha
from Body.speak import Speak
def WolfRam(query):
    api_key = "A7WQJ6-E2RVP2Y4XY"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        Speak("No Data Found")
def Calculator(query):
    term = str(query)
    term = term.replace("jarvis","")
    term = term.replace("add","+")
    term = term.replace("sub","-")
    term = term.replace("into","*")
    term = term.replace("divide","//")

    Final = str(term)
    try:
        result = WolfRam(Final)
        Speak(f"{result}")
    except:
        Speak("There is some error")

Calculator("500 into 56 add 6987 divide 56")