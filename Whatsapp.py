# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
# from time import sleep
# import pandas as pd
# from py.speek import Speek
# import pathlib
# from py.jarvisAI import MicExecution

# scriptDirectory = pathlib.Path().absolute()
# options=Options
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
# os.system("")
# os.environ["WDM_LOG_LEVEL"]="0"
# pathofDriver="Database\\chromedriver.exe"
# driver=webdriver.Chrome(pathofDriver, options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# Speek("Initializing The Whatsapp Softwere.")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from time import sleep
import pandas as pd
from py.speek import Speek
import pathlib
from py.jarvisAI import MicExecution

scriptDirectory = pathlib.Path().absolute()
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
options.add_experimental_option("detach", True)
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
pathofDriver = "Database\\chromedriver.exe"
service = Service(executable_path=pathofDriver)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
Speek("Initializing The WhatsApp Software.")


ListWeb={'Prakashbhai': "+918109416924",
         'jeetu': "+918871419660"

           }

def WhatsappSender(Name):
    Speek(f"Preparing To Send a Message To {Name}")
    Speek("What's The Message By The Way?")
    Message=MicExecution()
    Number =ListWeb[Name]
    LinkWeb='https://web.whatsapp.com/send?phone='+ Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        Speek("Message Send")
        
      
    except:
        print("Invalid Number")

WhatsappSender("jeetu")

    # //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
    # /html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span
    # /html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span

# /html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
# /html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
# /html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span