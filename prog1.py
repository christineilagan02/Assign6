# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
third = float(input("Enter your third number: "))
fourth = float(input("Enter your fourth number: "))

def highest_to_lowest(first, second, third, fourth):
    if highest == first:
        if second > third and third > fourth:
            print(f"The numbers are in the following order: {first}, {second}, {third}, and {fourth}.")
        elif second < third and third > fourth:
            print(f"The numbers are in the following order: {first}, {third}, {second}, and {fourth}.")
        elif second < third and third < fourth:
            print(f"The numbers are in the following order: {first}, {third}, {fourth}, and {second}.")
        else:
            print(f"The numbers are in the following order: {first}, {fourth}, {second}, and {third}.")
            return highest

    if highest == second:
        if first > third and third > fourth:
             print(f"The numbers are in the following order: {second}, {first}, {third}, and {fourth}.")
        elif first < third and third > fourth:
            print(f"The numbers are in the following order: {second}, {third}, {first}, and {fourth}.")
        elif first < third and third < fourth:
            print(f"The numbers are in the following order: {second}, {third}, {fourth}, and {first}.")
        else:
            print(f"The numbers are in the following order: {second}, {fourth}, {first}, and {third}.")
            return highest

    if highest == third:
        if first > second and second > fourth:
             print(f"The numbers are in the following order: {third}, {first}, {second}, and {fourth}.")
        elif first < second and second > fourth:
            print(f"The numbers are in the following order: {third}, {second}, {first}, and {fourth}.")
        elif first < second and second < fourth:
            print(f"The numbers are in the following order: {third}, {second}, {fourth}, and {first}.")
        else:
            print(f"The numbers are in the following order: {third}, {fourth}, {first}, and {second}.")
            return highest

    if highest == fourth:
        if first > second and second > third:
             print(f"The numbers are in the following order: {fourth}, {first}, {second}, and {third}.")
        elif first < second and second > third:
            print(f"The numbers are in the following order: {fourth}, {second}, {first}, and {third}.")
        elif first < second and second < third:
            print(f"The numbers are in the following order: {fourth}, {second}, {third}, and {first}.")
        else:
            print(f"The numbers are in the following order: {fourth}, {third}, {first}, and {second}.")
            return highest

highest = highest_to_lowest(first, second, third, fourth)