import speech_recognition as sr
import pyttsx3 as p
r = sr.Recognizer()
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',160)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def recognizer_speech():
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,duration=1.2)
        print("listening..")
        audio = r.listen(source)
        text1 =""
        try:
            text1 = r.recognize_google(audio)
        except:
            print("sorry, could not recognise")
            text1=""
        return text1
