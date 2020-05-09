def root():
    import json
    login_page = input("""what would you like to do? Enter 1 or 2 to choose
                        1. Staff login 
                        2. Close App: """).lower()
    if login_page == "1":
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        # opening staff.txt file to verify user input
        with open('staff.txt', 'r') as f_obj:
            staff_details = json.load(f_obj)
        if username == (staff_details['Staff1']['username']) and password == (
                staff_details['Staff1']['password']) or \
                username == (staff_details['Staff2']['username']) and password == (
                staff_details['Staff2']['password']):
            print("Login Successful")
            staff_home_page()
        else:
            print("Incorrect username or password")
            root()
    elif login_page == "2":
        exit()
    else:
        print("Invalid Entry")
        # recalling the root method after an invalid entry
        root()


# creating a method for staff options after a successful login
def staff_home_page():
    staff_options = input("""What would you like to do? Enter 1, 2 0r 3 to choose
                         1. Create a new bank account
                         2. Check Account Details
                         3. Logout: """).lower()
    if staff_options == "1":
        import random
        import json
        import os
        acct_name = input("Account name: ")
        opening_bal = input("Opening Balance: ")
        acct_type = input("Account type: ")
        acct_email = input("Account email: ")
        # generating random number to use as acct number
        acct_num = ("017" + random.randrange(0, 10 ** 7).__str__())
        print("Your account number is: " + acct_num)
        # creating dictionaries to save in the customer.txt file
        overall_data = {}
        banking_details = {
            'Account name': acct_name, 'Opening Balance': opening_bal + '$',
            'Account type': acct_type, 'Account email': acct_email
        }
        overall_data[acct_num] = banking_details
        # check if customer.txt is empty by doing this, the essence of this is to enable the smooth reading of text from the file.
        if os.stat('customer.txt').st_size == 0:
            with open('customer.txt', 'w') as f_obj:
                json.dump(overall_data, f_obj)
        else:
            # i.e. if the customer.txt is not empty
            with open('customer.txt') as f_obj:
                # it will load the contents of customer.txt to the variable overall_data
                overall_data = json.load(f_obj)
                # Then append the present user details
                overall_data[acct_num] = banking_details
                # Then open the customer file in write mode and dump the overall_data to it
                with open('customer.txt', 'w') as f:
                    json.dump(overall_data, f)
        staff_home_page()
    elif staff_options == "2":
        import json
        check_acct = input('Enter account number to check: ')
        # So to check it on the customer.txt file
        with open('customer.txt') as file_obj:
            data = json.load(file_obj)
            if check_acct in data:
                print('\nAccount Found ! See details below:')
                for keys, values in data[check_acct].items():
                    print('\n\t' + keys + ' : ' + str(values))
                staff_home_page()
            else:
                print('Account does not exist! You can register a new one if you wish. Choose by entering 1 below')
                staff_home_page()
    elif staff_options == "3":
        print("Logout successful")
        # recalling the root method
        root()
    else:
        print("Invalid entry")
        # recalling the home page after an invalid entry among staff options
        staff_home_page()


root()
