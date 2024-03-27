
# Helper functions for CRUD operations

def exit_program():
    print("Bon Appetit!")
    exit()

    # Recipe
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
    unique_categories = set()  

    for category in categories:
        # Check if the category name is already in the set
        if category.name not in unique_categories:
            print(category)
            unique_categories.add(category.name)  


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

            if category.update():
                print(f'Category {id_} updated successfully.')
            else:
                print(f'Failed to update category {id_}.')
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f'Category {id_} not found')


def delete_category():
    category_id = input("Enter the ID of the category you want to delete: ")
    try:
        category_id = int(category_id)
    except ValueError:
        print("Invalid input. Please enter a valid integer ID.")
        return

    category = Category.find_by_id(category_id)
    if category:
        if Category.delete(category_id):
            print(f"Category with ID {category_id} deleted successfully.")
        else:
            print(f"Failed to delete category with ID {category_id}.")
    else:
        print(f"No category found with ID {category_id}.")


from recipe import Recipe
from category import Category
