import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from getAtendens import *
from yt_auto import *
from News import *
from jokes import *
from weathermap import *
from music import *
from excel_opretion import *
import randfacts
import datetime
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',160)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("hello sir, good" + wishme() + " i'm your voice assistant.") 
speak("Today is" + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Temprature in Ghaziabad is" + str(temp()) + "degree celsius" + " and with " + str(des()))
while True:
    text=""
    print("hello sir")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,duration=1.2)
        print("listening..")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("sorry, could not recognise")
            text="Error"
    if "Alexa" in text:

        speak("what can i do for you?")
        # if "what" and "about" and "you" in text:
        #     speak("I am having a good day sir")

        # speak("what can i do for you?")

        with sr.Microphone() as source:
            r.energy_threshold = 1000
            r.adjust_for_ambient_noise(source,duration=1)
            print("listening..")
            audio = r.listen(source)
            try:
                text1 = r.recognize_google(audio)
                print(text1)
            except:
                print("sorry, could not recognise")

        if "information" in text1:
            speak("You need information relatrd to which topic?")
            with sr.Microphone() as source:
                r.energy_threshold = 1000
                r.adjust_for_ambient_noise(source,duration=1)
                print("listening..")
                audio = r.listen(source)
                try:
                    info = r.recognize_google(audio)
                    print(info)
                except:
                    print("sorry, could not recognise")
            print("Searching {} in Google".format(info))
            speak("Searching {} in Google".format(info))
            assist = infow()
            assist.get_info(info)

        elif "play" and "video" in text1:
            speak("you want me to which video?")
            with sr.Microphone() as source:
                r.energy_threshold = 1000
                r.adjust_for_ambient_noise(source,duration=1)
                print("listening..")
                audio = r.listen(source)
                try:
                    vid = r.recognize_google(audio)
                    print(vid)
                except:
                    print("sorry, could not recognise")
            print("Playing {} video youtube".format(vid))
            speak("Playing {} video youtube".format(vid))
            assist =  music()
            assist.play(vid)

        elif "play" and "music" in text1:
            speak(" Sure sir, please wait.")
            music_play()
        elif "open" and "Excel" in text1:
            speak(" Sure sir, please wait.")
            OpenExcel()

        elif "show" and "attendance" in text1:
            speak("please wait.")
            assist = infowAttendance()
            assist.get_Attendance("2022b1533005", "Bajaj@123")

        elif "connect" and "Wi-Fi" in text1:
            speak("please wait.")
            assist = infowAttendance()
            assist.connect_Wifi("2022b1533005", "Bat60570")

        elif "news" in text1:
            speak("Sure sir, Now will read news for you.")
            print("Sure sir, Now will read news for you.")
            arr=news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif "fact" or "facts" in text1:
            speak("Sure sir,")
            x= randfacts.get_fact()
            print(x)
            speak("Did you know that, "+ x)

        elif "joke" or "jokes" in text1:
            speak("Sure sir, get ready for some chuckles")
            arr = joke()
            print(arr[0])
            speak(arr[0])
            print(arr[1])
            speak(arr[1])
            
    elif "Error" in text:
        text=""
    elif "exit" in text:
        exit()






