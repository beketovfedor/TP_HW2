class ShoppingList:
    def __init__(self, _items):
        self._items = _items
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe.scale(portions)
        for element in recipe.ingredients:
            self._items.append((element, recipe.title))
    def remove_recipe(self, title: str):
        self._items = [element for element in self._items if element[1] != title]
    def get_list(self):
        shoppingList = {}
        for element in self._items:
            shoppingList[(element[0].name, element[0].unit)] += element[0].quantity
        finalList = []
        for key in shoppingList:
            finalList.append(Ingredient(key[0], shoppingList[key], key[1]))
        return sorted(finalList, key= lambda x: x.name)
    def __add__(self, other: ShoppingList):
        newList  = self._items + other._items
        return ShoppingList(newList)
        
