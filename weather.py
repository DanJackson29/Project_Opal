import requests, bs4
import json
import pandas
from Data.loc import locations as l

# Gets data from https://www.wunderground.com/weather/us/"state abreaviation"/"city name"
# Example: https://www.wunderground.com/weather/us/pa/butler

def getWeather(loc):
     # Enter your API key here 
    api_key = "aeb8ad5fe63ed4ba0d2c3b426b8a3f0b"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    if(len(loc)==5):
        complete_url = base_url + "appid=" + api_key + "&zip=" + loc 
    else:
        complete_url = base_url + "appid=" + api_key + "&q=" + loc 

    response = requests.get(complete_url) 
    
    data = response.json()
