def root():
    login_page = input("""what would you like to do? 
                        1. Staff login 
                        2. Close App: """).lower()
    if login_page == "staff login":
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        # opening staff.txt file to verify user input
        file = open('staff.txt', 'r')
        if file.read().__contains__(username and password):
            print("Login Successful")
            file.close()
        else:
            print("Incorrect username or password")
            root()
    elif login_page == "close app":
        exit()
    else:
        print("Invalid Entry")
        # recalling the root method after an invalid entry
        root()


import random


# creating a method for staff options after a successful login
def home_page():
    staff_options = input("""What would you like to do?
                         1. Create new bank account
                         2. Check Account Details
                         3. Logout: """).lower()
    if staff_options == "create new bank account":
        acct_name = input("Account name: ")
        opening_bal = input("Opening Balance: ")
        acct_type = input("Account type: ")
        acct_email = input("Account email: ")
        # generating random number to use as acct number
        acct_num = ("017" + random.randrange(0, 10 ** 7).__str__())
        print("Your account number is: " + acct_num)
        # saving variables in the customer.txt file
        file = open('customer.txt', 'a')
        file.write("Account name: " + acct_name + "\n")
        file.write("Account Balance: " + opening_bal + "$\n")
        file.write("Account type: " + acct_type + "\n")
        file.write("Account email: " + acct_email + "\n")
        file.write("Account number: " + acct_num + "\n")
        file.close()
        home_page()
    elif staff_options == "check account details":
        check_acct = input("Please what's your account number: ")
        # reading out saved file from customer.txt file.
        file = open("customer.txt", "r")
        print(file.read())
        home_page()
    elif staff_options == "logout":
        print("Logout successful")
        # recalling the root method
        root()
    else:
        print("Invalid entry")
        # recalling the home page after an invalid entry among staff options
        home_page()


root()
home_page()
