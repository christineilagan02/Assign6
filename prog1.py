# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
third = float(input("Enter your third number: "))
fourth = float(input("Enter your fourth number: "))

def highest_to_lowest(first, second, third, fourth):
    if highest == first:
        if second > third and third > fourth:
            print("The numbers are in the following order: {first}, {second}, {third}, and {fourth}.")
        elif second < third and third > fourth:
            print("The numbers are in the following order: {first}, {third}, {second}, and {fourth}.")
        elif second < third and third < fourth:
            print("The numbers are in the following order: {first}, {third}, {fourth}, and {second}.")
        else:
            print("The numbers are in the following order: {first}, {fourth}, {second}, and {third}.")


highest = highest_to_lowest(first, second, third, fourth)