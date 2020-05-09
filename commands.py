
import weather


def runWeatherCommand():
    print("Where would you like the weather from?\nYou can enter City, (City, State), or Zip Code.")
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
