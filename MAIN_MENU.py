import sqlite3
def main_menu():
    print("Welcome to Cafe Management System")
    print("Choose what you would like to do!")
    main_menu_options = [
        '1. Recipe Book',
        '2. Menu Management',
        '3. Ingredients Stock',
        '4. Machines Condition',
        '5. Order Management',
        '6. Staff Management',
        '7. Sales and Reports',
        '8. Exit the Application'
    ]
    print(*main_menu_options, end="\n")
    print("Enter the number of your choice : ", end="")
    main_menu_choice = int(input())
    while not (1 <= main_menu_choice <= 8):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        main_menu_choice = int(input())
    else:
        if main_menu_choice == 1:               # Recipe Book Options
            print('Recipe Book')
            recipe_book()
        elif main_menu_choice == 2:                 # Menu Management Options
            print('Menu Management')
            menu_management()
        elif main_menu_choice == 3:                 # Ingredients Stock Options
            print('Ingredients Stock')
            ingredients_stock()
        elif main_menu_choice == 4:                 # Machines Conditions Options
            print('Machines Condition')
        elif main_menu_choice == 5:                 # Order Management Options
            print('Order Management')
            order_management()
        elif main_menu_choice == 6:                 # Staff Management Options
            print('Staff Management')
            staff_management()
        elif main_menu_choice == 7:                 # Sales Options
            print('Sales')
        else:
            print('Exiting the Application.......')
task = main_menu()


def recipe_book():
    recipe_book = sqlite3.connect(
        "C:\\Users\\JANARDHANA RAO\\PycharmProjects\\CAFE_MANAGEMENT_SYSTEM\\Recipe_Book.db")
    # Creating / Opening the recipe book database
    cursor = recipe_book.cursor()
    print('Choose what you would like to do!')
    recipe_book_options = [
        '1. Read recipe book',
        '2. Update recipe book',
        '3. Close'
    ]
    print(*recipe_book_options, end="\n")
    print("Enter the number of your choice : ", end="")
    recipe_book_choice = int(input())
    while not (1 <= recipe_book_choice <= 3):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        recipe_book_choice = int(input())
    else:
        if recipe_book_choice == 1:  # Reading Recipe Book
            print("Opening the Recipe Book.......")
            for recipes in recipe_book.execute('''SELECT * FROM recipes'''):
                print(recipes)
        elif recipe_book_choice == 2:  # Updating Recipe Book
            print("Accessing the Recipe Book.......")
            print('Choose what you would like to do!')
            recipe_book_updating_options = [
                '1. Add a new recipe',
                '2. Delete a recipe'
            ]
            print(*recipe_book_updating_options, end="\n")
            print("Enter the number of your choice : ", end="")
            recipe_book_updating_choice = int(input())
            while not (1 <= recipe_book_updating_choice <= 2):
                print("Please enter a valid choice!")
                print("Enter the number of your choice : ", end="")
                recipe_book_updating_choice = int(input())
            else:
                if recipe_book_updating_choice == 1:  # Adding new recipe
                    print("Enter the recipe name : ")
                    recipe_name = input()
                    print(f"Enter the recipe of {recipe_name} : ")
                    new_recipe = input()
                    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(name TEXT, details TEXT)''')
                    cursor.execute('''INSERT INTO recipes VALUES(?, ?)''', [recipe_name, new_recipe])
                    # Using ? to prevent SQL injection
                    recipe_book.commit()
                    print("Recipe book updated!")
                elif recipe_book_updating_choice == 2:  # Deleting a recipe
                    print("Enter the recipe to be deleted : ")
                    delete_recipe = input()
                    if delete_recipe in recipe_book.execute('''SELECT name FROM recipes'''):
                        print("Deleting the recipe.......")
                        # Recipe should be deleted here
                        print("Recipe deleted!")
                    else:
                        print("Entered Recipe is not present in recipe book!")
        else:
            print("Closing the Recipe Book")
    # recipe_book.close()                 # Close connection
    # cursor.close()              # Close cursor


def menu_management():
    menu_management = sqlite3.connect(
        "C:\\Users\\JANARDHANA RAO\\PycharmProjects\\CAFE_MANAGEMENT_SYSTEM\\Menu_Management.db")
    # Creating \ Opening Menu Management database
    cursor = menu_management.cursor()
    print('Choose what you would like to do!')
    menu_management_options = [
        '1. Read the Menu',
        '2. Update the Menu',
        '3. Close'
    ]
    print(*menu_management_options, end="\n")
    print("Enter the number of your choice : ", end="")
    menu_management_choice = int(input())
    while not (1 <= menu_management_choice <= 3):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        menu_management_choice = int(input())
    else:
        if menu_management_choice == 1:  # Reading Menu
            print("Opening the Menu.......")
            for item in menu_management.execute('''SELECT item from menu_options'''):
                print(item)
        elif menu_management_choice == 2:  # Updating the Menu
            print("Accessing the Menu.......")
            print('Choose what you would like to do!')
            menu_updating_options = [
                '1. Add a new item',
                '2. Delete an item'
            ]
            print(*menu_updating_options, end="\n")
            print("Enter the number of your choice : ", end="")
            menu_updating_choice = int(input())
            while not (1 <= menu_updating_choice <= 2):
                print("Please enter a valid choice!")
                print("Enter the number of your choice : ", end="")
                menu_updating_choice = int(input())
            else:
                if menu_updating_choice == 1:  # Adding new item to Menu
                    print("Enter the item : ")
                    new_item = input()
                    menu_management.execute('''CREATE TABLE IF NOT EXISTS menu_options(item TEXT)''')
                    menu_management.execute('''INSERT INTO menu_options VALUES(?)''', [new_item])
                    menu_management.commit()
                    print(f"{new_item} updated on menu!")
                elif menu_updating_choice == 2:  # Deleting an item in Menu
                    print("Enter item to be deleted : ")
                    delete_item = input()
                    if delete_item in menu_management.execute('''SELECT item from menu_options'''):
                        print("Deleted item on menu")
                        # Delete item from menu
                    else:
                        print("Entered item is not present in the menu!")
        else:
            print("Closing the Menu")
    # menu_management.close()
    # cursor.close()


def ingredients_stock():
    ingredients_stock = sqlite3.connect(
        "C:\\Users\\JANARDHANA RAO\\PycharmProjects\\CAFE_MANAGEMENT_SYSTEM\\Ingredients_Stock.db")
    cursor = ingredients_stock.cursor()
    print('Choose what you would like to do!')
    ingredients_stock_options = [
        '1. Check the Stock',
        '2. Update the Stock',
        '3. Close'
    ]
    print(*ingredients_stock_options, end="\n")
    print("Enter the number of your choice : ", end="")
    ingredients_stock_choice = int(input())
    while not (1 <= ingredients_stock_choice <= 3):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        ingredients_stock_choice = int(input())
    else:
        if ingredients_stock_choice == 1:  # Stock Checking
            print("Checking the Stock.......")
            for ingredient in ingredients_stock.execute('''SELECT ingredient FROM stock'''):
                print(ingredient)
        elif ingredients_stock_choice == 2:
            print("Accessing the Stock.......")
            print('Choose what you would like to do!')
            ingredients_stock_updating_options = [
                '1. Add more ingredients',
                '2. Delete an ingredient'
            ]
            print(*ingredients_stock_updating_options, end="\n")
            print("Enter the number of your choice : ", end="")
            ingredients_stock_updating_choice = int(input())
            while not (1 <= ingredients_stock_updating_choice <= 2):
                print("Please enter a valid choice!")
                print("Enter the number of your choice : ", end="")
                ingredients_stock_updating_choice = int(input())
            else:
                if ingredients_stock_updating_choice == 1:  # Adding new ingredient to stock
                    print("Enter the ingredient : ")
                    new_ingredient = input()
                    ingredients_stock.execute('''CREATE TABLE IF NOT EXISTS stock(ingredient TEXT)''')
                    ingredients_stock.execute('''INSERT INTO stock VALUES(?)''', [new_ingredient])
                    ingredients_stock.commit()
                    print("Ingredient Added!")
                elif ingredients_stock_updating_choice == 2:  # Deleting an ingredient from stock
                    print("Enter ingredient to be deleted : ")
                    delete_item = input()
                    if delete_item in ingredients_stock.execute('''SELECT ingredient in stock'''):
                        print("Deleted item on menu")
                    else:
                        print("Entered item is not present in the menu!")
        else:
            print("Closing the Stock")
    # ingredients_stock.close()
    # cursor.close()


def order_management():
    print('Choose what you would like to do!')
    order_management_options = [
        '1. Check previous order status',
        '2. Add a new order',
        '3. Close'
    ]
    print(order_management_options)
    print("Enter the number of your choice : ", end="")
    order_management_choice = int(input())
    while not (1 <= order_management_choice <= 3):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        order_management_choice = int(input())
    else:
        if order_management_choice == 1:
            print("Checking the order status.......")
        elif order_management_choice == 2:
            print("Add the order!")
        else:
            print("Closing")


def staff_management():
    print('Choose what you would like to do!')
    staff_management_options = [
        '1. Check available staff',
        '2. Check staff details',
        '3. Close'
    ]
    print(staff_management_options)
    print("Enter the number of your choice : ", end="")
    staff_management_choice = int(input())
    while not (1 <= staff_management_choice <= 3):
        print("Please enter a valid choice!")
        print("Enter the number of your choice : ", end="")
        staff_management_choice = int(input())
    else:
        if staff_management_choice == 1:
            print("Checking the available status.......")
        elif staff_management_choice == 2:
            print("Fetching staff data........")
        else:
            print("Closing")