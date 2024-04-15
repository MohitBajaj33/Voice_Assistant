from selenium import webdriver
import time
from Recognizer_Speech import *

class music():
          
    def play(self, query):
        self.query = query
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query) 
        video = self.driver.find_element("xpath",'//*[@id="video-title"]')
        video.click()
        run = True
        while run:
            voice = recognizer_speech()
            print(voice)
            if "search other video" in voice:
                speak("you want me to which video?")
                voice = recognizer_speech()
                print(voice)
                print("Playing {} video youtube".format(voice))
                speak("Playing {} video youtube".format(voice))
                Search_video = self.driver.find_element("xpath",'//*[@id="search-input"]')
                Search_video.click()
                time.sleep(2)
                Search_video.clear()
                Search_video.send_keys(voice)
                Search_video.submit()
            elif "close window" in voice:
                speak("close window")
                run = False



# assist = music()
# assist.play("java")