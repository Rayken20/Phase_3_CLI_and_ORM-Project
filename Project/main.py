from helper import (
    exit_program,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_all,
    find_recipe_by_name,
    find_recipe_by_id,
    create_recipe,
    update_recipe,
    delete_recipe,
    list_recipes_by_category,
  )

def main():
    while True:
        main_menu()
        main_choice = input("> ")
        if main_choice == "0":
            exit_program()
        elif main_choice == "1":
            category_menu()    
        elif main_choice == "3":
            recipe_menu()
        else:
            print("Invalid choice")

def category_menu():
    while True:
        category_submenu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == "4":
            create_category()
        elif choice == "5":
            update_category()
        elif choice == "6":
            delete_category()
        else:
            print("Invalid choice")

def recipe_menu():
    while True:
        recipe_submenu()
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            list_all()
        elif choice == "2":
            find_recipe_by_name()
        elif choice == "3":
            find_recipe_by_id()
        elif choice == "4":
            create_recipe()
        elif choice == "5":
            update_recipe()
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            list_recipes_by_category()
        else:
            print("Invalid choice")

def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Categories")
    print("3. Recipes")

def category_submenu():
    print("Category Menu:")
    print("0. Back to main menu")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Find category by id")
    print("4. Create category")
    print("5. Update category")
    print("6. Delete category")


def recipe_submenu():
    print("Recipe Menu:")
    print("0. Back to main menu")
    print("1. List all recipes")
    print("2. Find recipe by name")
    print("3. Find recipe by id")
    print("4. Create recipe")
    print("5. Update recipe")
    print("6. Delete recipe")
    print("7. List recipes by category")

if __name__ == "__main__":
    main()
