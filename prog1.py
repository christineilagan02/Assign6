# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

import sys

first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
third = float(input("Enter your third number: "))
fourth = float(input("Enter your fourth number: "))



def highest_to_lowest(first, second, third, fourth):
    if first >= second and first >= third and first >= fourth: 
        if second >= third and third >= fourth:
            sys.exit(f"The numbers are in the following order: {first}, {second}, {third}, and {fourth}.")
        elif second >= fourth and fourth >= third:
            sys.exit(f"The numbers are in the following order: {first}, {second}, {fourth}, and {third}.")
        elif second <= third and second >= fourth:
            sys.exit(f"The numbers are in the following order: {first}, {third}, {second}, and {fourth}.")
        elif third >= fourth and fourth >= second:
            sys.exit(f"The numbers are in the following order: {first}, {third}, {fourth}, and {second}.")
        elif second <= fourth and second >= third:
            sys.exit(f"The numbers are in the following order: {first}, {fourth}, {second}, and {third}.")
        else:
               sys.exit(f"The numbers are in the following order: {first}, {fourth}, {third}, and {second}.")

    if second >= first and second >= third and second >= fourth:
        if first >= third and third >= fourth:
            sys.exit(f"The numbers are in the following order: {second}, {first}, {third}, and {fourth}.")
        elif first >= fourth and fourth >= third:
            sys.exit(f"The numbers are in the following order: {second}, {first}, {fourth}, and {third}.")
        elif first <= third and first >= fourth:
            sys.exit(f"The numbers are in the following order: {second}, {third}, {first}, and {fourth}.")
        elif third >= fourth and fourth >= first:
            sys.exit(f"The numbers are in the following order: {second}, {third}, {fourth}, and {first}.")
        elif first <= fourth and first >= third:
            sys.exit(f"The numbers are in the following order: {second}, {fourth}, {first}, and {third}.")
        else:
                sys.exit(f"The numbers are in the following order: {second}, {fourth}, {third}, and {first}.")
                

    if third >= first and third >= second and third >= fourth:
        if first >= second and second >= fourth:
            sys.exit(f"The numbers are in the following order: {third}, {first}, {second}, and {fourth}.")
        elif first >= fourth and fourth >= second:
            sys.exit(f"The numbers are in the following order: {third}, {first}, {fourth}, and {second}.")
        elif first <= second and first >= fourth:
            sys.exit(f"The numbers are in the following order: {third}, {second}, {first}, and {fourth}.")
        elif fourth <= second and first <= fourth:
            sys.exit(f"The numbers are in the following order: {third}, {second}, {fourth}, and {first}.")
        elif fourth >= first and first >= second:
            sys.exit(f"The numbers are in the following order: {third}, {fourth}, {first}, and {second}.")
        else:
                sys.exit(f"The numbers are in the following order: {third}, {fourth}, {second}, and {first}.")
                

    if fourth >= first and fourth >= second and fourth >= third:
        if first >= second and second >= third:
            sys.exit(f"The numbers are in the following order: {fourth}, {first}, {second}, and {third}.")
        elif first >= third and third >= second:
            sys.exit(f"The numbers are in the following order: {fourth}, {first}, {third}, and {second}.")
        elif second >= first and first >= third:
            sys.exit(f"The numbers are in the following order: {fourth}, {second}, {first}, and {third}.")
        elif second >= third and third >= first:
            sys.exit(f"The numbers are in the following order: {fourth}, {second}, {third}, and {first}.")
        elif first <= third and first >= second:
            sys.exit(f"The numbers are in the following order: {fourth}, {third}, {first}, and {second}.")
        else:
               sys.exit(f"The numbers are in the following order: {fourth}, {third}, {second}, and {first}.")
               
            

highest = highest_to_lowest(first, second, third, fourth)