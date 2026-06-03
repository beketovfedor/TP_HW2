class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient : Ingredient):
        for element in self.ingredients:
            if element == ingredient:
                element.quantity += ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(ratio: float):
        newRecipe = Recipe(self.title, self.ingredients.copy())
        for element in newRecipe.ingredients:
            element.quantity *= ratio
        return newRecipe
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        print(f"    ❦{self.title}❦")
        for element in self.ingredients:
            print(f"❧ {element}")