from selenium import webdriver
import time
from Recognizer_Speech import *
class infow():
          
    def get_info(self, query):
        self.query = query
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url="https://www.google.com/") 
        search = self.driver.find_element("xpath",'//*[@id="APjFqb"]')
        search.click()
        search.send_keys(query)
        search.submit()
        run = True
        while run:
            voice = recognizer_speech()
            print(voice)

            if "search other topic" in voice:
                speak("You need information relatrd to which topic?")
                voice = recognizer_speech()
                print(voice)
                speak("Searching {} in Google".format(voice))
                search = self.driver.find_element("xpath",'//*[@id="APjFqb"]')
                search.click()
                search.send_keys(voice)
                search.submit()
            elif "close window" in voice:
                speak("close window")
                run = False
        

# assist = infow()
# assist.get_info("whtat is java")