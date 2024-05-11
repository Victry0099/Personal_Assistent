import speech_recognition as sr
from googletrans import Translator 

# # Listen:  hindi to english
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)  # listen mode

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    return query

# Listen()
# print(Listen())

 # Traslation of english
def TranslationHiToEng(Text):
    try:
        line = str(Text)
        translate = Translator()
        result = translate.translate(line, src='hi', dest='en')
        data = result.text
        print(f"You: {data}.")
        return data
    except Exception as e:
        print(f"Translation error: {e}")
        return str(Text)

# TranslationHiToEng("हेलो गुड मॉर्निंग")

# Connect
def MicExecution():
    query = Listen()
    data = TranslationHiToEng(query)
    return data

# MicExecution()