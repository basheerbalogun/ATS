# todo: A signup and sign-in program that take basic info:
# todo: On signup, username, first name, last name, password and confirm password and saves it in a csv file.
# todo: On signin, it takes username and password and return whether a message saying login successful or invalid
# todo: login credentials. Add validation. Password must be minimum of 8 characters.
# For your task today, duplicate your program from yesterday into another file and modify it as thus:
# 1. After successful signup, it should prompt the user to signin.
# 2. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
# 3. Edit profile should ask for more information like phone_number (required), address (optional), date of birth
#  (optional) and gender (compulsory) 
# Happy coding!!!

import csv,sys


header=['username','firstname','lastname','password','confirm_password']
header_2 = ['username','firstname','lastname','password','confirm_password','phone_number','address','gender','date_of_birth']
edited_data={}

def portfolio():
    options = "\n\t1)Edit profile\n\t2)Change password\n\t3)Log out"
    prompt = input(f'{options} Choose option')

    if prompt == "1":
        edit_profile()
    elif prompt == "2":
        change_password()
    elif prompt == "3":
        log_out()

def log_out():

    return sys.exit()



def get_data():
    with open('sign_in.csv', "r") as rf:
        file = csv.DictReader(rf)
        return list(file)




def sign_up():
    data={}
    print("\n\t\tWelcome to sign up page ")
    data["username"] = input("Enter your username : ")
    data['firstname'] = input("Enetr you firstname : ")
    data['lastname'] = input("Enter your lastname : ")
    password = input("Enter your password (with characters not less than 8) : ")
    password_2 = input("Please confirm your password : ")
    data["password"] = password
    data['confirm_password']= password_2

    if len(password) != 8:
        print("your password is strong!")
        if password_2 == password:
            print("Your password is correct")
            print("Succesfull!")
            print("you will be redirected to log in page ...")
            log_in()
        else:
            print("your paasword is in correct")
    elif len(password) < 8:
        print("your password is week, sorry enter the strong one to be secured")

    with open('sign_in.csv', "w") as f:
        handler = csv.DictWriter(f, fieldnames=header)
        if len(get_data()) == 0:
            handler.writeheader()
            handler.writerow(data)
        else:
            handler.writerow(data)

        print("Now you can log in")
        log_in()

def edit_profile():
    my_portfolio = get_data()
    previous_password = input("Enter your paasword to proceed profile editing : ")
    for portfolio in my_portfolio:
        if portfolio["password"] == previous_password:
            profile_editing()
        else:
            return 'password incorrect!'
        edit_profile()



def profile_editing():
        data = get_data()

        
        edited_data["username"] = input("Enter your username  to proceed : ")
        edited_data['phone_number']= input('Enter your phone number : ')
        edited_data['address']= input('Enter your home address: ')
        edited_data['gender']= input("Choose your gender (M/F) : ")
        edited_data['date_of_birth'] = input("enter your age : ")

        for profile in data:
            if profile['username'] == edited_data['username']:
               new_edited_profile()


def new_edited_profile():
    with open('sign_in.csv', "w") as rw:
        handler = csv.DictWriter(rw, fieldnames=header_2)
        if len(get_data()) ==0:
            handler.writeheader()
            handler.writerow(edited_data)
        else:
            handler.writerow(edited_data)
        print("You have successfully edited your profile ")
        portfolio()


def log_in():
    print("\n\t\tWelcome to login page ")
    login_validation = get_data()

    u_password = input("Enter your password here : ")

    for account in login_validation:
        if account['password'] == u_password:
            print("login succesfull")
            portfolio()
        else:
            print("wrong password ! , try again")
            log_in()

def func_old_password():
    previous_password = new_edited_profile()
    old_password = input("Enter your old password : ")

    for data in previous_password:
        if data['password'] == old_password:
            change_password()
        else:
            func_old_password()


def change_password():
    passw = new_edited_profile()
    new_password =input("Enter new password : ")
    for ch_pass in passw:
        ch_pass['password'] == new_password



def home():
    welcome="Welcome to AFEX "
    wel= welcome.center(20, "=")
    print(wel)
    print("Do you have AFEX user account? if yes prss 1 to login else press 2 to sign up ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        log_in()
    elif choice == 2:
        sign_up()

home()
