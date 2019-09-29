class Recipe:
    def __init__(self,ingredients):
        self.ingredients = ingredients


class recipes:
    r = {
        "burger": Recipe(("1 ground meat", "1 hamburger bun", "1 slice of cheese","ketchup","Mayo")),
        "steak": Recipe(("1 steak","1tsp olive oil", "1tsp soy sauce","garlic powder","black pepper"))
    }