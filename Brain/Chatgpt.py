from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
ScriptDir = pathlib.Path().absolute()


url ="https://flowgpt.com/chat"
chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"

chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument('--profile-directory=Default')
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_option)
driver.maximize_window()
driver.get(url=url)
ChatNumber = 3
# sleep(500)

def Cheker():
    global ChatNumber
    for i in range(1,1000):
        if i % 2!= 0:
            try:
                ChatNumber = str(i)
                Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
                Text = driver.find_element(by=By.XPATH, value=Xpath).text

            except:
                print(f"The next chatnumber is: {i} ")
                ChatNumber = str(i)
                break

def websiteopener():
    while True:
       try:
          xPATH ="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
          driver.find_element(by=By.XPATH, value=xPATH)
          break
       except:
           pass
       
def SendMessage(Query):
     xPATH ="/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/textarea"
     driver.find_element(by=By.XPATH, value=xPATH).send_keys(Query)
     sleep(0.5)
     Xpath2 = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/button"
     driver.find_element(by=By.XPATH, value=Xpath2).click()


def ResultScrapper():
    global ChatNumber
    ChatNumber = str(ChatNumber)
    Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
    Text = driver.find_element(by=By.XPATH, value=Xpath).text
    print(Text)
    ChatNumberNew = int(ChatNumber)+2
    ChatNumber =ChatNumberNew




# def popupremover():
#     Xpath ='/html/body/div[3]/div[3]/div/section/div/div[3]/button[2]'
#     driver.find_element(by=By.XPATH,value=Xpath).click()


# popupremover()
# /html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[3]/div/div/div/div[1]
# /html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[1]/div/div[5]/div/div/div/div[1]


def WaitFortheAnswer():
      sleep(2)
      Xpath = "/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button"
      while True:
       try:
          driver.find_element(by=By.XPATH, value=Xpath)
       except:
            break

websiteopener()
Cheker()
# print("Loaded!")
# SendMessage("Hello, How are you")
# sleep(5000)
while True:
    Query = input("Enter: ")
    SendMessage(Query=Query)
    WaitFortheAnswer()
    ResultScrapper()