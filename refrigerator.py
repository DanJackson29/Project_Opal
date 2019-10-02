import pickle


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients


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

