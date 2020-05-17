
import weather
from refrigerator import Refrigerator
from ingredient import Ingredient


def runWeatherCommand():
    print("Where would you like the weather from?\nYou can enter City, (City, State), or Zip Code.")
    loc = input(">")
    weather.getWeather(loc)

def runAddIngredient():
    print("Please follow the prompts to add your ingredient:\n")
    ingredient_to_add = Ingredient()
    print("Please enter ingredient name:")
    ingredient_to_add.name = input(">")
    print("Please enter ingredient type:")
    ingredient_to_add.ingredient_type = input(">")
    print("Please enter ingredient standard unit:")
    ingredient_to_add.std_unit = input(">")
    print("Please enter ingredient amount:")
    ingredient_to_add.amount = input(">")
    print("Please enter ingredient minimum amount:")
    ingredient_to_add.minimumAmount = input(">")

    myFridge = Refrigerator()
    myFridge.add_ingredient(ingredient_to_add)


# def runGetRecipe():
#     voiceEngine.say("What recipe would you like to hear?")
#     voiceEngine.runAndWait()
#     recipe = input(">")
#     refrigerator.printRecipe(recipe)


# def runAddRecipe():
#     voiceEngine.say("What is the name of the recipe you would like to add?")
#     voiceEngine.runAndWait()
#     recipeName = input(">")

#     voiceEngine.say("What are the ingredients of the recipe seperated by a comma")
#     voiceEngine.runAndWait()
#     recipeIngredients = input(">").split(",")

#     refrigerator.addRecipe(recipeName, recipeIngredients)
