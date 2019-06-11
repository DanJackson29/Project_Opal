import requests, bs4
from Data.loc import locations as l

# Gets data from https://www.wunderground.com/weather/us/"state abreaviation"/"city name"
# Example: https://www.wunderground.com/weather/us/pa/butler


def getWeather(loc):
    inList = loc.split(",")
    if len(inList) == 1:
        s = l.locations.get(inList[0].strip())[0]
        c = l.locations.get(inList[0].strip())[1]
    elif len(inList) == 2:
        if len(inList[0].strip()) == 2:
            s = inList[0]
            c = inList[1]
        else:
            c = inList[0]
            s = inList[1]

    c = c.strip().replace(" ", "-")
    s = s.strip()
    printData(s + "/" + c)


def printData(stateCity):
    url = "https://www.wunderground.com/weather/us/" + stateCity
    res = requests.get(url)
    res.raise_for_status()
    weatherSoup = bs4.BeautifulSoup(res.text, features="html.parser")
    # hiLo doesnt always get something... not sure why
    hiLo = weatherSoup.select(".hi-lo")
    current = weatherSoup.select(".current-temp")
    feelsLike = weatherSoup.select(".feels-like .temp")

    hiLoList = hiLo[0].getText().split()
    currentList = (current[0].getText().strip()).split()

    if len(currentList) > 0:
        currentTemp = currentList[0] + "°"
        print(f"Currently: {currentTemp}")

    if len(feelsLike) > 0:
        feelsLikeTemp = feelsLike[0].getText().strip()
        print(f"Feels Like: {feelsLikeTemp}")

    if len(hiLoList) > 2:
        hi = hiLoList[0]
        lo = hiLoList[2]
        print(f"High: {hi}\nLow: {lo}\n")

    days = weatherSoup.select(".day")
    dates = weatherSoup.select(".date")
    temps = weatherSoup.select(".temp")

    if len(days) == 3 and len(dates) == 3 and len(temps) > 3:
        del temps[0]
        for i in range(0, 3):
            print(
                days[i].getText().strip().replace("\n", "")
                + ", "
                + dates[i].getText().strip().replace("\n", "")
                + ": "
                + temps[i]
                .getText()
                .strip()
                .replace("\n", "")
                .replace("|", "Low")
                .replace(" F", "°")
            )
