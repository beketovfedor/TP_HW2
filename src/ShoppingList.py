from src.Ingredient import Ingredient
from src.Recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        newRecipe = recipe.scale(portions)
        for element in newRecipe.ingredients:
            self._items.append((element, recipe.title))
    def remove_recipe(self, title: str):
        self._items = [element for element in self._items if element[1] != title]
    def get_list(self):
        shoppingList = {}
        for element in self._items:
            shoppingList[(element[0].name, element[0].unit)] = shoppingList.get((element[0].name, element[0].unit), 0) + element[0].quantity
        finalList = []
        for key in shoppingList:
            finalList.append(Ingredient(key[0], shoppingList[key], key[1]))
        return sorted(finalList, key= lambda x: x.name)
    def __add__(self, other: ShoppingList):
        newList  = self._items + other._items
        newShoppingList = ShoppingList()
        newShoppingList._items = newList
        return newShoppingList
        