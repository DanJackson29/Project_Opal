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


def runAddRecipe():
    voiceEngine.say("What is the name of the recipe you would like to add?")
    voiceEngine.runAndWait()
    recipeName = input(">")

    # name,unit,quantity
    voiceEngine.say(
        "Enter Ingredient in the form name,unit,quantity. Type done when there are no more ingredeints"
    )
    voiceEngine.runAndWait()
    ingredients = []
    recipeIngredient = input(">").strip().lower().split(",")

    while recipeIngredient[0] != "done":
        ingredients.append(refrigerator.Ingredient(*recipeIngredient))
        recipeIngredient = input(">").strip().lower().split(",")

    refrigerator.addRecipe(recipeName, ingredients)

