import json
from ingredient import Ingredient

class Refrigerator:

    def __init__(self):
        curr_ingredients = open("my_ingredients.json")
        curr_ingredients = json.load(curr_ingredients)["ingredients"]
        self.ingredient_list = self.get_current_ingredients(curr_ingredients)

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
    
    def get_current_ingredients(self, curr_ingredients):
        list_of_ingredients = []
        for ingred in curr_ingredients.keys():
            my_ingredient = Ingredient()
            my_ingredient.name = ingred
            my_ingredient.ingredient_type = curr_ingredients[ingred]["ingredient_type"]
            my_ingredient.std_unit = curr_ingredients[ingred]["std_unit"]
            my_ingredient.amount = curr_ingredients[ingred]["amount"]
            my_ingredient.minimumAmount = curr_ingredients[ingred]["minimum_amount"]
            list_of_ingredients.append(my_ingredient)
        return list_of_ingredients

    def print_current_ingredients(self):
        for ingred in self.ingredient_list:
            print(ingred)



















# class Recipe:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients


# class Ingredient:
#     def __init__(self, name, standard_unit, quantity):
#         self.name = name
#         self.standard_unit = standard_unit
#         self.quantity = quantity

#     def __str__(self):
#         return str(self.quantity) + " " + self.standard_unit + " of " + self.name


# def printRecipe(rec):
#     with open("Data/recipeBook.pkl", "rb") as f:
#         rb = pickle.load(f)
#     listOfIngredients = rb.get(rec).ingredients
#     for i in listOfIngredients:
#         print(i)
#     return 0


# def addRecipe(name, ingredients):
#     with open("Data/recipeBook.pkl", "rb") as f:
#         recipeBook = pickle.load(f)
#     recipeBook[name] = Recipe(ingredients)

#     with open("Data/recipeBook.pkl", "wb") as f:
#         pickle.dump(recipeBook, f)


# def convert(convertStr, amount):
#     return fd.CONVERSION[convertStr] * amount


# def deleteRecipe(name):
#     with open("Data/recipeBook.pkl", "rb") as f:
#         recipeBook = pickle.load(f)
#     del recipeBook[name]

#     with open("Data/recipeBook.pkl", "wb") as f:
#         pickle.dump(recipeBook, f)


# def writeRecipe(name, ingredients):
#     recipeBook = open("Data/recipeBook.py", "r+")
#     for line in recipeBook:
#         print(line)


# writeRecipe("test", "test")

