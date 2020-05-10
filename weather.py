import requests, bs4
import json
import pandas
from Data.loc import locations as l

DEGREE_SIGN = u"\N{DEGREE SIGN}"


def getWeather(loc):
    # Enter your API key here
    api_key = "aeb8ad5fe63ed4ba0d2c3b426b8a3f0b"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    if len(loc) == 5:
        complete_url = base_url + "appid=" + api_key + "&zip=" + loc + "&units=imperial"
    else:
        complete_url = base_url + "appid=" + api_key + "&q=" + loc + "&units=imperial"

    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    weather_data = response.json()
    # for k in weather_data:
    # print(k, weather_data[k])

    temp_lo = int(weather_data["main"]["temp_min"])
    temp_hi = int(weather_data["main"]["temp_max"])
    curr_temp = int(weather_data["main"]["temp"])
    loc_name = weather_data["name"]
    cloud_desc = weather_data["weather"][0]["description"]

    if str(cloud_desc) == "cloudy":
        cloud_desc = "cloudy skies"
    elif str(cloud_desc) == "clear sky":
        cloud_desc = "clear skies"

    print(
        "Currently in "
        + str(loc_name)
        + " it is "
        + str(curr_temp)
        + DEGREE_SIGN
        + " with "
        + str(cloud_desc)
        + "."
        + "\nToday's high is "
        + str(temp_hi)
        + DEGREE_SIGN
        + " and the low is "
        + str(temp_lo)
        + DEGREE_SIGN
    )
