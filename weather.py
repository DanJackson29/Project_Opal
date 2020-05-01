import requests, bs4
import json
import pandas
from Data.loc import locations as l

# Gets data from https://www.wunderground.com/weather/us/"state abreaviation"/"city name"
# Example: https://www.wunderground.com/weather/us/pa/butler

def getWeather(loc):
    printData("test")
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


    # inList = loc.split(",")
    # if len(inList) == 1:
    #     s = l.locations.get(inList[0].strip())[0]
    #     c = l.locations.get(inList[0].strip())[1]
    # elif len(inList) == 2:
    #     if len(inList[0].strip()) == 2:
    #         s = inList[0]
    #         c = inList[1]
    #     else:
    #         c = inList[0]
    #         s = inList[1]

    # c = c.strip().replace(" ", "-")
    # s = s.strip()
    # printData(s + "/" + c)

#Should catch an exception here saying that a specific city/state combo doesn't exist
def printData(stateCity):
  
    # Enter your API key here 
    api_key = "aeb8ad5fe63ed4ba0d2c3b426b8a3f0b"
    
    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Give city name 
    city_name = input("Enter city name : ") 
    
    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 

    # url = "https://www.wunderground.com/weather/us/" + stateCity
    # res = requests.get(url)
    # res.raise_for_status()
    # weatherSoup = bs4.BeautifulSoup(res.text,'lxml')
    # # hiLo doesnt always get something... not sure why
    # hiLo = weatherSoup.select(".hi-lo")
    # current = weatherSoup.select(".current-temp")
    # feelsLike = weatherSoup.select(".feels-like .temp")

    # hiLoList = hiLo[0].getText().split()
    # currentList = (current[0].getText().strip()).split()

    # if len(currentList) > 0:
    #     currentTemp = currentList[0] + "°"
    #     print(f"Currently: {currentTemp}")

    # if len(feelsLike) > 0:
    #     feelsLikeTemp = feelsLike[0].getText().strip()
    #     print(f"Feels Like: {feelsLikeTemp}")

    # if len(hiLoList) > 2:
    #     hi = hiLoList[0]
    #     lo = hiLoList[2]
    #     print(f"High: {hi}\nLow: {lo}\n")

    # days = weatherSoup.select(".day")
    # dates = weatherSoup.select(".date")
    # temps = weatherSoup.select(".temp")

    # if len(days) == 3 and len(dates) == 3 and len(temps) > 3:
    #     del temps[0]
    #     for i in range(0, 3):
    #         print(
    #             days[i].getText().strip().replace("\n", "")
    #             + ", "
    #             + dates[i].getText().strip().replace("\n", "")
    #             + ": "
    #             + temps[i]
    #             .getText()
    #             .strip()
    #             .replace("\n", "")
    #             .replace("|", "Low")
    #             .replace(" F", "°")
    #         )
