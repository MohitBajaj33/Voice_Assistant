import requests
from ss import *
url = "https://api.openweathermap.org/data/2.5/weather?q=Ghaziabad&appid="+ key2

json_data = requests.get(url).json()
# print(json_data)
def temp():
    temprature = round(json_data["main"]["temp"]-273,1)
    return temprature

def des():
    description =json_data["weather"][0]["description"]
    return description
 