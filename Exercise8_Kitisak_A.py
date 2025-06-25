cappuccino = 65
latte = 75
mocha = 85
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin" and passwordInput == "1234":
    print("===================================================")
    print("         --- Welcome to COFFEE Shop---             ")
    print("===================================================")
    print("My menu")
    print("<<1>>Cappuccino ",cappuccino,"$")
    print("<<2>>Latte ",latte,"$")
    print("<<3>>Mocha ",mocha,"$")
    print("===================================================")
    menu = int(input("Please select your drink. >>"))
    if menu == 1:
        print("Your chosen drink is : Cappuccino")
        qty = int(input("How many orders would you like? >>"))
        amount = cappuccino * qty
        print("Cappuccino x",qty,"=",amount,"$")
    elif menu == 2:
        print("Your chosen drink is : Latte")
        qty = int(input("How many orders would you like? >>"))
        amount = latte * qty
        print("Latte x", qty, "=", amount, "$")
    elif menu == 3:
        print("Your chosen drink is : Mocha")
        qty = int(input("How many orders would you like? >>"))
        amount = mocha * qty
        print("Mocha x", qty, "=", amount, "$")
    else:
        print("Sorry, the drink you selected is not available.")

else:
    print("Wrong password or username")