# Import necessary modules

# Helper functions for CRUD operations
def exit_program():
    print("Bon Appetit!")
    exit()
def list_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)

def find_recipe_by_name():
    name = input("Enter the recipe's name: ")
    recipe = Recipe.find_by_name(name)
    print(recipe) if recipe else print(f'Recipe {name} not found')

def find_recipe_by_id():
    id_ = input("Enter the recipe's id: ")
    recipe = Recipe.find_by_id(id_)
    print(recipe) if recipe else print(f'Recipe {id_} not found')

def create_recipe():
    name = input("Enter the recipe's name: ")
    description = input("Enter the recipe's description: ")
    ingredients = input("Enter the recipe's ingredients: ")
    instructions = input("Enter the recipe's instructions: ")
    category_id = input("Enter the category id for the recipe: ")
    try:
        recipe = Recipe.create(name, description, ingredients, instructions, category_id)
        print(f'Success: {recipe}')
    except Exception as exc:
        print("Error creating recipe: ", exc)

def update_recipe():
    id_ = input("Enter the recipe's id: ")
    if recipe := Recipe.find_by_id(id_):
        try:
            name = input("Enter the recipe's new name: ")
            recipe.name = name
            description = input("Enter the recipe's new description: ")
            recipe.description = description
            ingredients = input("Enter the recipe's new ingredients: ")
            recipe.ingredients = ingredients
            instructions = input("Enter the recipe's new instructions: ")
            recipe.instructions = instructions
            category_id = input("Enter the new category id for the recipe: ")
            recipe.category = category_id

            recipe.update()
            print(f'Success: {recipe}')
        except Exception as exc:
            print("Error updating recipe: ", exc)
    else:
        print(f'Recipe {id_} not found')

def delete_recipe():
    id_ = input("Enter the recipe's id: ")
    if recipe := Recipe.find_by_id(id_):
        recipe.delete()
        print(f'Recipe {id_} deleted')
    else:
        print(f'Recipe {id_} not found')

def list_recipes_by_category():
    category_id = input("Enter the category id: ")
    recipes = Recipe.find_by_category(category_id)
    for recipe in recipes:
        print(recipe)

# Define other CRUD functions for ingredients and categories
# Helper functions for CRUD operations

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    print(category) if category else print(f'Category {name} not found')

def find_category_by_id():
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    print(category) if category else print(f'Category {id_} not found')

def create_category():
    name = input("Enter the category's name: ")
    description = input("Enter the category's description: ")
    try:
        category = Category.create(name, description)
        print(f'Success: {category}')
    except Exception as exc:
        print("Error creating category: ", exc)

def update_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        try:
            name = input("Enter the category's new name: ")
            category.name = name
            description = input("Enter the category's new description: ")
            category.description = description

            category.update()
            print(f'Success: {category}')
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f'Category {id_} not found')

def delete_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        category.delete()
        print(f'Category {id_} deleted')
    else:
        print(f'Category {id_} not found')

def list_ingredients():
    ingredients = Ingredient.get_all()
    for ingredient in ingredients:
        print(ingredient)

def find_ingredient_by_name():
    name = input("Enter the ingredient's name: ")
    ingredient = Ingredient.find_by_name(name)
    print(ingredient) if ingredient else print(f'Ingredient {name} not found')

def find_ingredient_by_id():
    id_ = input("Enter the ingredient's id: ")
    ingredient = Ingredient.find_by_id(id_)
    print(ingredient) if ingredient else print(f'Ingredient {id_} not found')

def create_ingredient():
    name = input("Enter the ingredient's name: ")
    category = input("Enter the ingredient's category: ")
    quantity = float(input("Enter the ingredient's quantity: "))
    unit = input("Enter the ingredient's unit: ")
    try:
        ingredient = Ingredient.create(name, category, quantity, unit)
        print(f'Success: {ingredient}')
    except Exception as exc:
        print("Error creating ingredient: ", exc)

def update_ingredient():
    id_ = input("Enter the ingredient's id: ")
    if ingredient := Ingredient.find_by_id(id_):
        try:
            name = input("Enter the ingredient's new name: ")
            ingredient.name = name
            category = input("Enter the ingredient's new category: ")
            ingredient.category = category
            quantity = float(input("Enter the ingredient's new quantity: "))
            ingredient.quantity = quantity
            unit = input("Enter the ingredient's new unit: ")
            ingredient.unit = unit

            ingredient.update()
            print(f'Success: {ingredient}')
        except Exception as exc:
            print("Error updating ingredient: ", exc)
    else:
        print(f'Ingredient {id_} not found')

def delete_ingredient():
    id_ = input("Enter the ingredient's id: ")
    if ingredient := Ingredient.find_by_id(id_):
        ingredient.delete()
        print(f'Ingredient {id_} deleted')
    else:
        print(f'Ingredient {id_} not found')

from recipe import Recipe
from category import Category
from ingredient import Ingredient



# Define other CRUD functions for categories