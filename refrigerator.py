from Data.recipes import recipes as recs

def printRecipe(rec):
    listOfIngredients = recs.r.get(rec).ingredients
    for i in listOfIngredients:
        print(i)
