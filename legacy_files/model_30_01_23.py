"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for repeated functions - to make main.py neater
    Date: 04/12/22
"""

def return_to_menu():
    # Ask if we want to return to main menu, in a loop in case of wrong input
    valid_return = 0
    while valid_return == 0:
        return_menu = input("Return to main menu (Y/N): ").capitalize()
        if return_menu == 'N':
            exit()
        elif return_menu != 'Y':
            print('Invalid option, try again.')
        else:
            valid_return = 1

def username_input_mgmt(individual_names):
    # Ask for an input and clean
    user = str(input("Insert username: "))
    # Check the name exists in the network
    if user in individual_names:
        return user
    else:
        print("This username does not exist.")
        return_to_menu()
