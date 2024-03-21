from recipe import Recipe
from ingredient import Ingredient
from category import Category
import sqlite3

# Database connection
CONN = sqlite3.connect('recipes.db')
CURSOR = CONN.cursor()

# Functions for CLI operations
def main_menu():
    print("Welcome to Recipe Management System!")
    while True:
        print("1. Recipes Menu")
        print("2. Ingredients Menu")
        print("3. Categories Menu")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            recipes_menu()
        elif choice == "2":
            ingredients_menu()
        elif choice == "3":
            categories_menu()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def recipes_menu():
    # Implement recipes menu options
    pass

def ingredients_menu():
    # Implement ingredients menu options
    pass

def categories_menu():
    # Implement categories menu options
    pass

def exit_program():
    print("Goodbye!")
    CONN.close()
    exit()

if __name__ == "__main__":
    main_menu()
