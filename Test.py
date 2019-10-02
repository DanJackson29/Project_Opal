import pickle


class Recipe:
    def __init__(self, ingredients):
        self.ingredients = ingredients


RecipeBook = {
    "burger": Recipe(
        ("1 ground meat", "1 hamburger bun", "1 slice of cheese", "ketchup", "Mayo")
    ),
    "steak": Recipe(
        ("1 steak", "1tsp olive oil", "1tsp soy sauce", "garlic powder", "black pepper")
    ),
}

with open("Data/recipeBook.pkl", "rb") as f:
    rb = pickle.load(f)
print(rb)

