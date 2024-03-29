"""
    Author: Matthew Vallance 001225832
    Purpose: Main file for running the social network
    Date: 04/12/22
"""
import classes
import model


def main():
    global common_friends
    selected_menu_option = 0
    valid_filename = 0

    # Initialise social network routine
    data_retrieval = classes.Data()

    # Ask user to input valid filename, then get data
    while valid_filename == 0:
        data_file = input("Insert data filename (or 'n' to quit): ")
        if data_file == "n":
            exit()
        social_nw = data_retrieval.get_data("nw_data1") # REMOVE FILENAME AFTER TESTING
        if social_nw:
            valid_filename = 1
        else:
            print("Invalid filename")

    while selected_menu_option != 6:
        valid_selection = 0

        # Main menu
        print("Menu: \n 1. Display social network \n 2. Display common friends \n 3. Recommend new friends (option 2 MUST be run FIRST) \n 4. Sign in \n 5. Sign up \n 6. Add friend \n 7. Close")

        while valid_selection == 0:
            valid_menu_options = [1, 2, 3, 4, 5, 6]
            # Check menu option is correct data type - CAN THIS BE DONE NEATLY?
            try:
                selected_menu_option = int(input("Select an option: "))
                if selected_menu_option in valid_menu_options:
                    valid_selection = 1
                else:
                    print("Invalid selection, try again. IFF")
            except ValueError:
                print('Invalid selection, try again.')
                break

        friends = classes.Friends()
        # 1. Display social network
        if int(selected_menu_option) == 1:
            # Pretty print connections
            for user in social_nw:
                print(user.replace(" ", " -> "))

            # Return to main menu
            model.return_to_menu()

        # 2. Display common friends
        elif int(selected_menu_option) == 2:

            common_friends = friends.get_common_friends(social_nw)
            for common_friends_for_user in common_friends:
                print(common_friends_for_user[0], " -> ", common_friends_for_user[1])

            # Return to main menu
            model.return_to_menu()

        elif int(selected_menu_option) == 3:
            user = str(input("Insert username: ")) # ERROR MANAGEMENT HERE
            friends.recommend_friend(common_friends, user)

            # Return to main menu
            model.return_to_menu()


# Run the main function
main()

'''
----------------------------------References------------------------------------
Exception handling - menu check: https://www.educative.io/answers/what-is-valueerror-in-python
'''
