"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for repeated functions - to make main.py neater
    Date: 04/12/22
"""

def return_to_menu():
    # Ask if we want to return to main menu
    return_menu = input("Return to main menu (Y/N): ").capitalize()
    if return_menu == 'N':
        exit()

def username_input_mgmt(individual_names):
    # Ask for an input and clean
    user = str(input("Insert username: "))
    # Check the name exists in the network
    if user in individual_names:
        return user
    else:
        print("This username does not exist.")
        return_to_menu()
