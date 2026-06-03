from src.Recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients  = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self,ratio: float):
        newRecipe  = super().scale(ratio)
        return DietaryRecipe(newRecipe.title, self.diet_type, newRecipe.ingredients)
    def __str__(self):
        prefix  = f"[{self.diet_type}] "
        return prefix + super().__str__()
    