from Brain.AIBrain import ReplyBrain
from py.jarvisAI import MicExecution
print(">> Starting The Jarvis: Wait For Some Second.")
from py.speek import Speek
from features.clap import Tester
print(">> Starting The Jarvis: Wait For Some Second.")
from Newmain import MainTaskExecution

# def MainExe():
#     while True:
#         query=Listen()
#         if "hello" in query:
#             Speek("Hi, I am Jarvis! im good thankyou for awaking ")
#         elif "bye" in query:
#             Speek("Hello Bye.")

# MainExe()

def MainExecution():
    Speek("Hello Sir")
    Speek("I'm Jarvis, I'm Ready To Assist You Sir")
    while True:
         Data =MicExecution()
         Data =str(Data).replace(".","")

         ValueReturn =MainTaskExecution(Data)
         if ValueReturn==True:
             pass

         elif len(Data)<3:
            pass

         elif "turn on the tv" in Data:  # specific command
           Speek("ok..Turning on the TV")
         else:
        #    Reply = ReplyBrain(Data)
        #    Speek(Reply)
             pass
       
        
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected! >>")
        print("")
        MainExecution()
    else:
        pass
ClapDetect()