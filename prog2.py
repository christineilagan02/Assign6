# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random


def display_intro():
    name = input("Please, enter your name: ")
    print(f"Alright! {name} Welcome to Tine's Addition Quiz!")
    print("\nAre you ready?")
    answer = input("Enter yes or no: ")
    if answer == "yes":
        print("Prepare your self!")
    elif answer == "no":
        print("You can now exit.")
    else:
        print("Please enter yes or no.")
        return answer


def begin():
    title = "** Tine's Addition Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
     menu_list = ["1. Start", "2. Practice", "3. Exit"]
     print(menu_list[0])
     print(menu_list[2])
     print(menu_list[3])


def display_separator():
    print("-" * 24)

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 3 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input



def menu():
    display_intro()
    begin()
    display_menu()
    display_separator()
    get_user_input()



menu()

