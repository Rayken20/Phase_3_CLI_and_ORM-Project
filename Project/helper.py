
# Helper functions for CRUD operations
# Recipe
def exit_program():
    print("Bon Appetit!")
    exit()
def list_all():
  recipes = Recipe.list_all()
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
    instructions = input("Enter the recipe's instructions: ")
    category_id = input("Enter the category id for the recipe: ")
    try:
        recipe = Recipe.create(name, description, instructions, category_id)
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
            instructions = input("Enter the recipe's new instructions: ")
            recipe.instructions = instructions
            category_id = input("Enter the new category id for the recipe: ")
            recipe.category_id = category_id 
           
            ingredients = input("Enter the recipe's new ingredients: ")
            
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
    recipes = Recipe.list_by_category(category_id)
    for recipe in recipes:
        print(recipe)

# Categories
def list_categories():
    categories = Category.get_all()
    unique_categories = set()  # Use a set to store unique category names

    for category in categories:
        # Check if the category name is already in the set
        if category.name not in unique_categories:
            print(category)
            unique_categories.add(category.name)  # Add the category name to the set


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
    existing_category = Category.find_by_name(name)
    if existing_category:
        print(f"Category '{name}' already exists.")
    else:
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

# Ingredients
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
    recipe_id = input("Enter the recipe id for the ingredient: ")  # Add this line
    try:
        ingredient = Ingredient.create(name, category, quantity, unit, recipe_id)  
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

def list_ingredients_by_recipe():
    recipe_id = input("Enter the recipe id: ")
    recipe = Recipe.find_by_id(recipe_id)
    if recipe:
        ingredients = recipe.list_ingredients()
        for ingredient in ingredients:
            print(ingredient)
    else:
        print(f"Recipe with id {recipe_id} not found.")

from recipe import Recipe
from category import Category
from ingredient import Ingredient



