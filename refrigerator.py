import pickle


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients


class Ingredient:
    def __init__(self, name, standard_unit, quantity):
        self.name = name
        self.standard_unit = standard_unit
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity) + " " + self.standard_unit + " of " + self.name


def printRecipe(rec):
    with open("Data/recipeBook.pkl", "rb") as f:
        rb = pickle.load(f)
    listOfIngredients = rb.get(rec).ingredients
    for i in listOfIngredients:
        print(i)
    return 0


def addRecipe(name, ingredients):
    with open("Data/recipeBook.pkl", "rb") as f:
        recipeBook = pickle.load(f)
    recipeBook[name] = Recipe(ingredients)

    with open("Data/recipeBook.pkl", "wb") as f:
        pickle.dump(recipeBook, f)

