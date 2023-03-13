from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
from time import sleep
import pandas as pd
from Body.Speak import Speak
from Body.Listen import MicExecution
import pathlib

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
driver_service = Service(executable_path="DataBase\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service, options=options)
driver.maximize_window()
options.add_argument("--disable-extensions")
driver.get("https://web.whatsapp.com/")
Speak("Initializing The Whatsapp Software.")
time.sleep(20)
Speak("Wait for the page to load") 


ListWeb = {'Deep' : "+91",
            'dost': "+919904019094",
            "pote": '+91'}

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")

