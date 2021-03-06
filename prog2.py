# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
import sys

def display_intro():
    name = input("\33[1m\33[37m\33[40m\nPlease, enter your name:\33[0m\33[0m\33[0m")
    print(f"\33[33m\33[1m\nAlright!\33[0m \33[3m{name.title()}\33[0m\33[32m\33[33m\33[1m, Welcome to Tine's Addition Quiz!\33[0m")
    print("\33[3m\33[37m\33[1m\nAre you ready?\33[0m")
    answer = input("Enter \33[34m\33[1myes\33[0m or \33[1m\33[34mno\33[0m: ")
    if answer.lower() == "yes":
        print("\33[1m\33[3m\33[34m\nPrepare your self!\33[0m")
        return answer
    elif answer.lower() == "no":
        display_separator()
        print("\33[1m\33[3mYou can now exit.\33[0m")
        sys.exit(display_separator())
    else:
        display_separator()
        print("\33[1m\33[31m\33[47mPlease enter yes or no.\33[0m")
        answer = input("\33[1m\33[37mPlease try again:\33[0m ")
        return menu()


def begin():
    title = "\33[33m**\33[0m \33[1mTine's Addition Quiz\33[0m \33[33m**\33[0m"
    print("\n\33[33m**************************\33[0m")
    print(title)
    print("\33[33m*\33[0m" * 26)


def display_menu():
     menu_list = ["\33[3m\33[1m1. Start\33[0m", "\33[3m\33[1m2. Practice\33[0m", "\33[1m\33[3m3. Exit\33[0m"]
     print(menu_list[0])
     print(menu_list[1])
     print(menu_list[2])


def display_separator():
    print("\33[32m\33[1m-\33[0m" * 24)

def get_user_input():
    user_input = int(input("\33[92mEnter your choice:\33[0m "))
    while user_input > 3 or user_input <= 0:
        print("\33[1m\33[31m\nInvalid menu option.\33[0m")
        user_input = int(input("\33[1m\nPlease try again:\33[0m "))
    else:
        return user_input



def menu_option(index):
    question = 0
    score = 0
    total = 10
    if index == 1:
        while question <= 9:
            question += 1
            ops = ['+']
            number_one = random.randrange(0, 99)
            number_two = random.randrange(0, 99)
            operation = random.choice(ops)
            maths = eval(str(number_one) + operation + str(number_two))
            print('\33[1m\nQuestion number:\33[0m \33[1m\33[32m{}\33[0m'.format(question))
            print ("The question is",number_one, operation, number_two)

            d=int(input ("\33[3m\33[1mEnter your answer:\33[0m"))
            if d == maths:
                print ("\33[32m\33[1m\nCorrect! ????????\33[0m")
                score = score + 1
                display_separator()
            else:
                print ("\33[31m\33[1m\nIncorrect.???? \33[0m \33[1m\33[3mThe actual answer is\33[0m",maths)
                display_separator()

    elif index == 2:
       while question <= 9:
            question += 1
            ops = ['+']
            number_one = random.randrange(0, 99)
            number_two = random.randrange(0, 99)
            operation = random.choice(ops)
            maths = eval(str(number_one) + operation + str(number_two))
            print('\33[1m\nQuestion number:\33[0m \33[1m\33[32m{}\33[0m'.format(question))
            print ("The question is",number_one, operation, number_two)

            d=int(input ("\33[3m\33[1mEnter your answer:\33[0m"))
            if d == maths:
                print ("\33[32m\33[1m\nCorrect! ????????\33[0m")
                score = score + 1
                display_separator()
            else:
                print ("\33[31m\33[1m\nIncorrect.???? \33[0m \33[1m\33[3mThe actual answer is\33[0m",maths)
                display_separator()
    
        
    correct = score
    display_separator()
    if correct == 10:
        print(f"\33[3m\33[1mYour score is\33[0m \33[1m\33[34m{correct}/{total}\33[0m.")
        print("\33[1m\33[32mPerfect!????\33[0m")
    elif correct >= 5 or correct == 9:
        print(f"\33[3m\33[1mYour score is\33[0m \33[1m\33[34m{correct}/{total}\33[0m.")
        print("\33[1m\33[33mVery Good! Keep it up!????????\33[0m")
    elif correct >= 1 or correct == 4:
        print(f"\33[3m\33[1mYour score is\33[0m \33[1m\33[34m{correct}/{total}\33[0m.")
        print("\33[1m\33[36mGood! But you need more practice!????\33[0m")
    else:
        print(f"\33[3m\33[1mYour score is\33[0m \33[1m\33[34m{correct}/{total}\33[0m.")
        print("\33[1m\33[31mYou need more practice.????\33[1m")





def menu():
    display_intro()
    begin()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    while option != 3:
        total += 1
        menu_option(option)
        display_separator()
        option = get_user_input()



    print("\33[1m\33[93m\33[3m\nExit the quiz.\33[0m")
    display_separator()

menu()