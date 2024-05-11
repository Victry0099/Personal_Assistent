# windows based: fast, ofline work
import pyttsx3

# def Speek(Text):
#     engine= pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[0].id)
#     engine.setProperty('rate',170)
#     print("")
#     print(f"You: {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()

# Speek("Hey, I am jarvis thankyou for calling")

# Chrome based: More voices, More clear  dis= word limit , slow

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By

from time import sleep

chrome_options = Options()  
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--headless')
# chrome_options.headless =False
path = "Database\\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()


website = r"https://ttsmp3.com"
driver.get(website)
# Locate the dropdown element by its ID
language_dropdown = driver.find_element(By.ID, 'sprachwahl')

# Create a Select object to work with the dropdown
select = Select(language_dropdown)

# Select the option by visible text
select.select_by_visible_text('British English / Brian')

def Speek(Text):


    lengthoftext = len(str(Text))


    if lengthoftext ==0:
        pass
    else:
        print("")
        print(f"AI: {Text}.")
        print("")
        Data = str(Text)
            # Find the <textarea> element
        xpath_of_textarea = '//textarea[@id="voicetext"]'
        textarea_element = driver.find_element(By.XPATH, xpath_of_textarea)

        # Send text to the <textarea>
        textarea_element.send_keys(Data)

        # Find and click the "Read" button
        xpath_of_read_button = '//input[@id="vorlesenbutton"]'
        read_button = driver.find_element(By.XPATH, xpath_of_read_button)
        read_button.click()

        # Clear the <textarea> after clicking the button
        textarea_element.clear()

        if lengthoftext >=30:
            sleep(4)
        elif lengthoftext >=40:
            sleep(6)
        elif lengthoftext >=55:
            sleep(8)
        elif lengthoftext >=70:
            sleep(10)
        elif lengthoftext >=100:
            sleep(13)
        elif lengthoftext >=120:
            sleep(14)
        else:
            sleep(2)
       

# Speek("hello jarvis thankyou for calling")