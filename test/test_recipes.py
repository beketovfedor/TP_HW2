import pytest

from src.Ingredient import Ingredient
from src.Recipe import Recipe
from src.ShoppingList import ShoppingList
from src.DietaryRecipe import DietaryRecipe

def test_recipeInit():
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    assert recipe.title == "Салат \"Змейка\""
    assert recipe.ingredients[0].name == "Майонез"
    assert recipe.ingredients[1].quantity == 1
    assert recipe.ingredients[1].unit == "шт"

def test_recipeAddNew():
    recipe = Recipe("Салат \"Змейка-альбинос\"", [Ingredient("Майонез", 50, "г")])
    recipe.add_ingredient(Ingredient("Перец красный целый", 1, "шт"))
    assert recipe.ingredients[1].name == "Перец красный целый"

def test_recipeAddExisting():
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    recipe.add_ingredient(Ingredient("Перец черный целый", 1, "шт"))
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[1].quantity == 2

def test_recipeScaleCorrect():
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    newRecipe = recipe.scale(2)
    assert recipe.ingredients[1].quantity == 1
    assert newRecipe.ingredients[1].quantity == 2

def test_recipeScaleInorrect():
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"),    Ingredient("Перец черный целый", 1, "шт")])
    with pytest.raises(ValueError): 
        newRecipe = recipe.scale(-2)
    
def test_recipeLen():
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    assert len(recipe) == 2

def test_shoppingListAddRecipeCorrect():
    shoppingList = ShoppingList()
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    shoppingList.add_recipe(recipe, 2)
    assert shoppingList._items[0][0].quantity == 100
    assert shoppingList._items[1][0].quantity == 2

def test_shoppingListAddRecipeIncorrect():
    shoppingList = ShoppingList()
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    with pytest.raises(ValueError):
        shoppingList.add_recipe(recipe, -2)

def test_shoppingListRemoveRecipeExisting():
    shoppingList = ShoppingList()
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    shoppingList.add_recipe(recipe, 2)
    shoppingList.remove_recipe("Салат \"Змейка\"")
    assert len(shoppingList._items) == 0

def test_shoppingListRemoveRecipeNonExisting():
    shoppingList = ShoppingList()
    recipe = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    shoppingList.add_recipe(recipe, 2)
    shoppingList.remove_recipe("Салат \"Змейка-альбинос\"")
    assert len(shoppingList._items) == 2

def test_shoppingListGetList():
    shoppingList = ShoppingList()
    recipe1 = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    recipe2 = Recipe("Салат \"Змейка-альбинос\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец красный целый", 1, "шт")])
    shoppingList.add_recipe(recipe1, 2)
    shoppingList.add_recipe(recipe2, 3)
    finalList = shoppingList.get_list()
    assert len(finalList) == 3
    assert finalList[0].name == "Майонез"
    assert finalList[1].name == "Перец красный целый"
    assert finalList[0].quantity == 250

def test_shoppingListAdd():
    shoppingList1 = ShoppingList()
    shoppingList2 = ShoppingList()
    recipe1 = Recipe("Салат \"Змейка\"", [Ingredient("Майонез", 50, "г"), Ingredient("Перец черный целый", 1, "шт")])
    recipe2 = Recipe("Салат \"Змейка-альбинос\"", [Ingredient("Майонез", 30, "г"), Ingredient("Перец красный целый", 1, "шт")])
    shoppingList1.add_recipe(recipe1, 2)
    shoppingList2.add_recipe(recipe2, 3)
    newList = shoppingList1 + shoppingList2
    assert len(newList._items) == 4
    assert len(shoppingList1._items) == 2
    assert len(shoppingList2._items) == 2

