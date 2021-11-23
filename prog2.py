# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
import sys


def display_intro():
    name = input("\nPlease, enter your name: ")
    print(f"Alright! {name}, Welcome to Tine's Addition Quiz!")
    print("\nAre you ready?")
    answer = input("Enter yes or no: ")
    if answer == "yes":
        print("\nPrepare your self!")
    elif answer == "no":
        print("\nYou can now exit.")
        sys.exit(display_separator())
    else:
        print("\nPlease enter yes or no.")


def begin():
    title = "** Tine's Addition Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
     menu_list = ["1. Start", "2. Practice", "3. Exit"]
     print(menu_list[0])
     print(menu_list[1])
     print(menu_list[2])


def display_separator():
    print("-" * 24)

def get_user_input():
    user_input = int(input("\nEnter your choice: "))
    while user_input > 3 or user_input <= 0:
        print("\nInvalid menu option.")
        user_input = int(input("\nPlease try again: "))
    else:
        return user_input

def get_user_solution(problem, question):
    question = 0
    while question <= 4:
        question += 1
        print('\nQuestion number: {}'.format(question))
        print(problem, end="")
        result = int(input(" = "))
        return result

def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct!")
        return count
    else:
        print("Incorrect :(")
        return count 


def menu_option(index, count):
    question = 0
    number_one = random.randrange(0, 5)
    number_two = random.randrange(0, 5)
    if index == 1: 
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem, question)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem, question)
        count = check_solution(user_solution, solution, count)
        return count

def display_result(correct, wrong):
    total = 0
    if correct >= 10 and wrong == 0:
        print(f"Your score is {correct}/{total}.")
        print("Perfect! :)")
    elif correct >= 5 or correct == 9 and wrong >= 1:
        print(f"Your score is {correct}/{total} ")
        print("Very Good! Keep it up! :)")
    elif correct >= 1 or correct == 4 and wrong >= 1:
        print(f"Your score is {correct}/{total} ")
        print("Good! But you need more practice!")
    else:
        print(f"Your score is {correct}/{total} ")
        print("You need more practice. :(")



def menu():
    display_intro()
    begin()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    wrong = 0
    index = 0
    count = 0
    while option != 3:
        total = total + 1
        correct = menu_option(option, correct)
        option = menu_option(index, count)


    print("\nExit the quiz.")
    display_separator()
    display_result(correct, wrong)

menu()