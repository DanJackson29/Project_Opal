import pyttsx3
import weather
import refrigerator

voiceEngine = pyttsx3.init()
voiceEngine.setProperty(
    "voice",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)


def runWeatherCommand():
    voiceEngine.say("Where would you like weather from?")
    voiceEngine.runAndWait()
    loc = input(">")
    weather.getWeather(loc)

def runGetRecipe():
    voiceEngine.say("What recipe would you like to hear?")
    voiceEngine.runAndWait()
    recipe = input(">")
    refrigerator.printRecipe(recipe)
