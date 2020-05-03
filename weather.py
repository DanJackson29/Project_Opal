import requests, bs4
import json
import pandas
from Data.loc import locations as l

# Gets data from https://www.wunderground.com/weather/us/"state abreaviation"/"city name"
# Example: https://www.wunderground.com/weather/us/pa/butler


def getWeather(loc):
    printData(loc)
    # res = usCities[usCities["city"].str.lower()==loc.lower()]
    # if(len(res) == 1):
    #     print(res["state_id"].values[0] + "/"+ loc)
    #     printData(loc + "/"+res["state_id"].values[0])
    # else:
    #     print("Too many cities named: "+ loc + ". Please enter a state name to clarify:")
    #     state = input(">")
    #     fullInfo = usCities[(usCities["city"].str.lower()==loc.lower()) and (usCities["state_name"].str.lower()==loc.lower())]
    #     if(len(fullInfo) == 1):
    #         printData(loc + "/"+fullInfo["state_id"])
    #     else:
    #         print("Too many options. Futher functionality must be implemented.")


# Should catch an exception here saying that a specific city/state combo doesn't exist
def printData(stateCity):

    # Enter your API key here
    api_key = "aeb8ad5fe63ed4ba0d2c3b426b8a3f0b"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + stateCity + "&units=imperial"

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
