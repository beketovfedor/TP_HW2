from src.Ingredient import Ingredient

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        for element in self.ingredients:
            if element == ingredient:
                element.quantity += ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        scaled_ingredients = [Ingredient(ing.name, ing.quantity * ratio, ing.unit) for ing in self.ingredients]
        return Recipe(self.title, scaled_ingredients)
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        txt =(f" ❦{self.title}❦")
        for element in self.ingredients:
            txt += f"\n❧ {element}"
        return txt