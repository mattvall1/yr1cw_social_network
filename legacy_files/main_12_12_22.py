"""
	Author: Matthew Vallance 001225832
	Purpose: Main file for running the social network
	Date: 04/12/22
"""
import classes


def main():
    selected_menu_option = 0
    valid_filename = 0

    # Initialise social network routine
    data_retrieval = classes.data()

    # Ask user to input valid filename, then get data
    while valid_filename == 0:
        data_file = input("Insert data filename (or 'n' to quit): ")
        if data_file == "n":
            exit()
        social_NW = data_retrieval.get_data(data_file)
        # print(social_NW)
        if social_NW:
            valid_filename = 1
        else:
            print("Invalid filename")

    while selected_menu_option != 6:
        # Main menu # ASK ANDY: Should menus be inside another class
        print("Menu: \n 1. Display social network \n 2. Display common friends \n 3. Sign in \n 4. Sign up \n 5. Add friend \n 6. Close")
        selected_menu_option = int(input("Select an option: "))

        if selected_menu_option == 1:
            # Pretty print connections
            for user in social_NW:
                print(user.replace(" ", " -> "))

            # Ask if we want to return to main menu
            return_menu = input("Return to main menu (Y/N): ").capitalize()
            if return_menu == 'N':
                exit()

        elif selected_menu_option == 2:
            friends = classes.friends()

            common_friends = friends.get_common_friends(social_NW, 'Bob')
            print(common_friends)

            # Ask if we want to return to main menu
            return_menu = input("Return to main menu (Y/N): ").capitalize()
            if return_menu == 'N':
                exit()


# Run the main function
main()
