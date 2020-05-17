class Ingredient:

    name = None
    ingredient_type = None
    std_unit = None
    amount = None
    minimumAmount = None

    def __init__(self):
        self.name = None
        self.ingredient_type = None
        self.std_unit = None
        self.amount = None
        self.minimumAmount = None

    def __str__(self):
        if self.amount != 1:
            return (
                str(self.amount)
                + " "
                + str(self.std_unit).lower()
                + "s of "
                + str(self.name).lower()
            )

        else:
            return (
                str(self.amount)
                + " "
                + (self.std_unit).lower()
                + " of "
                + str(self.name).lower()
            )
