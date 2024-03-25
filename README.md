# Phase_3_CLI_and_ORM-Project:
Welcome to the Recipe Manager CLI! This command-line application allows users to manage and organize recipes, ingredients, and categories easily. It includes three model classes: Recipe, category, and Ingredient. 

## One to many relationship
The one-to-many relationship is between recipes and ingredients (each recipe can have multiple ingredients), and between category and recipe( each category can have many recipes)

## Features
- Create, delete, and display categories.
- Create, delete, and display recipes.
- View recipes belonging to a specific category.
- Create, delete, and display ingredients.
- View ingredients used in a specific recipe.
- Search for categories, recipes, and ingredients by name and id.

## Model Classes:
1. category:
Attributes: id, name, description
Methods: create, delete, get_all, find_by_id and name, list_recipes

2. recipe:
Attributes: id, name, description, instructions, category_id
Methods: create, delete, get_all, find_by_id and name, list_ingredients

3. ingredient:
Attributes: id, name, category, quantity, unit, recipe_id
Methods: create, delete, get_all, find_by_id and name

4. helper
Contains functions that abstract away complex and repetitive tasks and provide a simpler user interface
for perfoming basic CRUD operations.

5. Main
contains CLI interface for the recipe application. Has a loop that displays a menu and calls helper functions based on 
users' choice

## CREATING A VIRTUAL ENVIRONMENT
## To get started, run the following commands on the terminal
1. pipenv --python /usr/bin/python3
2. pipenv shell
3. run the file you're in i.e. python3 project/main.py