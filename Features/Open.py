import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from googlesearch import search

def OpenExe(Query):
    Query = str(Query).lower()
    Nameoftheapp = ""

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        
    elif "play" in Query and "youtube" in Query:
        # Extract the song name from the query
        song_name = Query.replace("play ","").replace(" on youtube","")
        
        # Search for the song on Google
        search_query = f"{song_name} site:youtube.com"
        search_results = search(search_query, num_results=1)
        video_url = search_results[0]
        webbrowser.open(video_url)
        sleep(3)

        # Maximize the browser window
        pyautogui.hotkey('win', 'up')
        sleep(1)

        # Click on the play button
        pyautogui.click(x=930, y=610)
        sleep(5)

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True
