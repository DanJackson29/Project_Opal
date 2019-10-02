import pyttsx3
import weather
from refrigerator import Recipe
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


def runAddRecipe():
    voiceEngine.say("What is the name of the recipe you would like to add?")
    voiceEngine.runAndWait()
    recipeName = input(">")

    voiceEngine.say("What are the ingredients of the recipe seperated by a comma")
    voiceEngine.runAndWait()
    recipeIngredients = input(">").split(",")

    refrigerator.addRecipe(recipeName, recipeIngredients)
