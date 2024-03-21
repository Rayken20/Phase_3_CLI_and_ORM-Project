from helper import (
    exit_program,
    list_categories,
    find_category_by_name,
    find_category_by_id,
    create_category,
    update_category,
    delete_category,
    list_ingredients,
    find_ingredient_by_name,
    find_ingredient_by_id,
    create_ingredient,
    update_ingredient,
    delete_ingredient,
    list_recipes,
    find_recipe_by_name,
    find_recipe_by_id,
    create_recipe,
    update_recipe,
    delete_recipe,
    list_recipes_by_category
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
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
        elif choice == "7":
            list_ingredients()
        elif choice == "8":
            find_ingredient_by_name()
        elif choice == "9":
            find_ingredient_by_id()
        elif choice == "10":
            create_ingredient()
        elif choice == "11":
            update_ingredient()
        elif choice == "12":
            delete_ingredient()
        elif choice == "13":
            list_recipes()
        elif choice == "14":
            find_recipe_by_name()
        elif choice == "15":
            find_recipe_by_id()
        elif choice == "16":
            create_recipe()
        elif choice == "17":
            update_recipe()
        elif choice == "18":
            delete_recipe()
        elif choice == "19":
            list_recipes_by_category()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Find category by id")
    print("4. Create category")
    print("5. Update category")
    print("6. Delete category")
    print("7. List all ingredients")
    print("8. Find ingredient by name")
    print("9. Find ingredient by id")
    print("10. Create ingredient")
    print("11. Update ingredient")
    print("12. Delete ingredient")
    print("13. List all recipes")
    print("14. Find recipe by name")
    print("15. Find recipe by id")
    print("16. Create recipe")
    print("17. Update recipe")
    print("18. Delete recipe")
    print("19. List recipes by category")

if __name__ == "__main__":
    main()
