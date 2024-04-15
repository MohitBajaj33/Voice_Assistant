from selenium import webdriver
import time
from Recognizer_Speech import *

          
def music_play():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url="https://music.apple.com/us/browse") 
    time.sleep(1)
    # search = driver.find_element("xpath",'//*[@id="__next"]/header/section[1]/div[2]/a/div/input')
    search = driver.find_element("xpath",'//*[@id="scrollable-page"]/main/div/div[3]/div/div[2]/section/div[1]/ul/li[1]/div/div/div[1]/div[3]')
    search.click()
    time.sleep(4)
    search1 = driver.find_element("xpath",'//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button')
    search1.click()
    # search.send_keys(query)
    song_number = '//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button'
    i=int(song_number[55])
    run = True
    while run:
        voice = recognizer_speech()
        print(voice)
        if "next song" in voice:
            i=i+1
            path = '//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[{number}]/div[2]/div/div[1]/div[2]/div/button'
            next_song = driver.find_element("xpath",path.format(number=i))
            next_song.click()
        elif "previous song" in voice:
            i=i-1
            path = '//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[{number}]/div[2]/div/div[1]/div[2]/div/button'
            next_song = driver.find_element("xpath",path.format(number=i))
            next_song.click()
        elif "stop song"in voice:
            i=i
            path = '//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[{number}]/div[2]/div/div[1]/div[2]/div/button'
            next_song = driver.find_element("xpath",path.format(number=i))
            next_song.click()
        elif "play song" in voice:
            i=i
            path = '//*[@id="scrollable-page"]/main/div/div[2]/div/div/div[{number}]/div[2]/div/div[1]/div[2]/div/button'
            next_song = driver.find_element("xpath",path.format(number=i))
            next_song.click()
        elif "close window" in voice:
            speak("close window")
            run = False





        