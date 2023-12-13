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
        print ("check stock level")
    elif (users_selection == "2"):
        print("add new arrival stock")
    elif (users_selection == "3"):
        print ("report stock on hold")
    elif (users_selection == "4"):
        print ("report return stock")
    elif (users_selection == "5"):
        continue
    else:
        print("Invalid Input")
