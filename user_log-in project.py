# This is a simple project that takes user's log-in information and validates it.

import time

name = input("Create a log-in name: ")
password = input("Create a password: ")

user_name = input("Please enter your name to log-in: ")
user_password = input("Please enter your password to log-in: ")

if user_name == name and user_password == password:
    print("Access granted!")
    print("Wait...")
    print("Loading.....")
    time.sleep(8)
    print(".....")
    time.sleep(5)
    print(".....")
    time.sleep(3)
    print("All clear")
elif user_name == name and user_password != password:
    print("You have entered a wrong user password. Please try again.")
elif user_name != name and user_password == password:
    print("You have entered a wrong user name.")
else:
    print("Access denied! Try again later.")
