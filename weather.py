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
        complete_url = base_url + "appid=" + api_key + "&zip=" + loc + "&units=imperial"
    else:
        complete_url = base_url + "appid=" + api_key + "&q=" + loc + "&units=imperial"

    response = requests.get(complete_url) 
    
    data = response.json()

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    weather_data = response.json()

    temp_lo = weather_data["main"]["temp_min"]
    temp_hi = weather_data["main"]["temp_max"]
    curr_temp = weather_data["main"]["temp"]

    print("The current temperature in " + stateCity + " is " + str(curr_temp) + " with a high of " + str(temp_hi) + " and low of " + str(temp_lo) + ".")
