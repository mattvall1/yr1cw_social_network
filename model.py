"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for general functions - to make main.py neater
    Date: 04/12/22
"""
import copy


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

def pretty_print(to_print):
    temporary_matrix = copy.deepcopy(to_print)

    # Loop to get the longest user name
    length_of_longest_name = 0
    for item in temporary_matrix:
        if len(item[0]) > length_of_longest_name:
            length_of_longest_name = len(item[0])

        item_to_string = []
        for list_item in item[1]:
            item_to_string.append(str(list_item))
        item[1] = item_to_string

    for item in temporary_matrix:
        # Calculate the difference in length and add whitespace to name
        whitespace = length_of_longest_name - len(item[0])
        item[0] = item[0] + (whitespace * ' ')

        print(item[0], ' -> ', ', '.join(item[1]))
