import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


def OpenExe(Query):
    Query =str(Query).lower()

    if "visit" in Query:
        NameofWeb = Query.replace("visit ","")
        Link = f"https://www.{NameofWeb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        NameofWeb = Query.replace("launch ","")
        Link = f"https://www.{NameofWeb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        NameofApp=Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(NameofApp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in Query:
        NameofApp=Query.replace("start ","")
        if "chrome" in NameofApp:                       # this is second way to open aystem app this is fast give the condition
            os.startfile(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        # pyautogui.press('win')
        # sleep(1)
        # keyboard.write(NameofApp)
        # sleep(1)
        # keyboard.press('enter')
        # sleep(0.5)
        # return True
    
# OpenExe('open notepad')