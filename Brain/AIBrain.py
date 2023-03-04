# Api Key
fileopen = open("Data\\Api.txt","r", encoding="utf-8")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv.main import load_dotenv #old from dotenv import load_dotenv


#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    if isinstance(question, int):
        question = str(question)

    FileLog = open("DataBase\\chat_log.txt","r", encoding="utf-8")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
    FileLog = open("DataBase\\chat_log.txt","w", encoding="utf-8")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
