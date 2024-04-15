from selenium import webdriver
import time
from Recognizer_Speech import *
class infowAttendance():
    
    def get_Attendance(self, admission, password):
        self.admission = admission
        self.password = password
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://abes.web.simplifii.com/index.php") 
        # admissionInput = self.driver.find_element_by_xpath('//*[@id="email"]')
        admissionInput=self.driver.find_element("xpath", '//*[@id="email"]')
        admissionInput.click()
        admissionInput.send_keys(admission)
        passwordInput = self.driver.find_element("xpath", '//*[@id="demo-field"]')
        passwordInput.click()
        passwordInput.send_keys(password)
        enter = self.driver.find_element("xpath",'//*[@id="loginButton"]')
        enter.click()
        run = True
        while run:
            voice = recognizer_speech()
            print(voice)

            if "attendance summary" in voice:
                click_Attendance_Summary = self.driver.find_element("xpath",'//*[@id="2"]')
                click_Attendance_Summary.click()
                time.sleep(2)
            elif "my course" in voice:
                click_My_Courses = self.driver.find_element("xpath",'//*[@id="1"]')
                click_My_Courses.click()
                time.sleep(2)
            elif "my schedule" in voice:
                click_My_Schedule = self.driver.find_element("xpath",'//*[@id="0"]')
                click_My_Schedule.click()
                time.sleep(2)
            elif "completed quiz" in voice:
                click_Completed_Quizzes = self.driver.find_element("xpath",'//*[@id="5"]')
                click_Completed_Quizzes.click()
                time.sleep(2)
            elif "close window" in voice:
                speak("close window")
                run = False


    def connect_Wifi(self, admission, password):
            self.admission = admission
            self.password = password
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://192.168.1.254:8090/") 
            time.sleep(4)
            # admissionInput = self.driver.find_element_by_xpath('//*[@id="email"]')
            admissionInput=self.driver.find_element("xpath", '//*[@id="username"]')
            admissionInput.click()
            admissionInput.send_keys(admission)
            passwordInput = self.driver.find_element("xpath", '//*[@id="password"]')
            passwordInput.click()
            passwordInput.send_keys(password)
            enter = self.driver.find_element("xpath",'/html/body/div/div[1]/div[2]/div[3]/a')
            enter.click()
            time.sleep(6)