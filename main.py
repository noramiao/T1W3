from functions import check_stock, add_new_stock, stock_on_hold, return_stock

print ("Welcome to the stock tracker!")

def selection_menu():
    print("1. Enter 1 to check current stock number")
    print("2. Enter 2 to report new arrival stock number")
    print("3. Enter 3 to report stock on hold number")
    print("4. Enter 4 to report return stock number")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_selection = ""

while users_selection!= "5":
    users_selection = selection_menu()
    if (users_selection == "1"):
        check_stock()
    elif (users_selection == "2"):
        add_new_stock()
    elif (users_selection == "3"):
        stock_on_hold()
    elif (users_selection == "4"):
        return_stock()
    elif (users_selection == "5"):
        continue
    else:
        print("Invalid Input")
