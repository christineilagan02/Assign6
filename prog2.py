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


total = 10

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
    user_input = int(input("Enter your choice: "))
    while user_input > 3 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input

def get_user_solution(problem):
    print("Enter your answer")
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
    for problem in range(1, 11):
        number_one = random.randrange(0, 99)
        number_two = random.randrange(0, 99)
        if index == 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count

def display_result(correct, wrong):
    if correct >= 10 and wrong == 0:
        print(f"Your score is {correct}/{total} ")
    elif correct >= 5 or correct == 9 and wrong >= 1:
        print(f"Your score is {correct}/{total} ")
    elif correct >= 1 or correct == 4 and wrong >= 1:
        print(f"Your score is {correct}/{total} ")
    else:
        print(f"Your score is {correct}/{total} ")


def menu():
    display_intro()
    begin()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 3:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()

menu()

