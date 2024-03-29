"""
    Author: Matthew Vallance 001225832
    Purpose: Main file for running the social network
    Date: 04/12/22
"""
import data
import friends as fr
import model
import statistics


def main():
    global common_friends
    selected_menu_option = 0
    valid_filename = 0

    # Initialise social network routine
    data_retrieval = data.Data()

    # Ask user to input valid filename, then get data
    while valid_filename == 0:
        data_file = input("Insert data filename (or 'n' to quit): ")
        if data_file == "n":
            exit()
        # Separate social_nw and individual names into separate variables
        data_unsplit = data_retrieval.get_data("nw_data2") # REMOVE FILENAME AFTER TESTING
        social_nw = data_unsplit[0]
        individual_names = data_unsplit[1]
        if social_nw:
            valid_filename = 1
        else:
            print("Invalid filename")

    while selected_menu_option != 6:
        valid_selection = 0

        # Main menu
        print("Menu: \n 1. Display social network \n 2. Display common friends \n 3. Recommend new friends (option 2 MUST be run FIRST) \n ------ Statistics ------ \n 4. Get number of friends for user \n 5. Get users with the least number of friends/no friends at all: \n 6. Add friend \n 7. Close")

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

        friends = fr.Friends()
        # 1. Display social network
        if int(selected_menu_option) == 1:
            # Pretty print connections
            for user in social_nw:
                # Convert set into comma seperated string
                try:
                    print(user[0], " -> ", ", ".join(user[1]))
                except IndexError:
                    print(user[0], " -> ")

            # Return to main menu
            model.return_to_menu()

        # 2. Display common friends
        elif int(selected_menu_option) == 2:

            common_friends = friends.get_common_friends(social_nw)
            for common_friends_for_user in common_friends:
                print(common_friends_for_user[0], " -> ", common_friends_for_user[1])

            # Return to main menu
            model.return_to_menu()

        # 3. Recommend new friends
        elif int(selected_menu_option) == 3:
            user = model.username_input_mgmt(individual_names)
            recommended_friend = friends.recommend_friend(common_friends, user)

            # Print results nicely, first determining whether we need plurals
            if len(recommended_friend) > 1:
                print('Recommended friends for ', user, ' are ', ", ".join(recommended_friend))
            else:
                print('Recommended friend for ', user, ' is ', recommended_friend[0])
            # Return to main menu
            model.return_to_menu()

        if selected_menu_option >= 4:
            # Get stats class for use in all following menu options
            stats = statistics.Statistics()

            if int(selected_menu_option) == 4:
                user = model.username_input_mgmt(individual_names)
                no_of_friends = stats.get_friends_count_for_user(social_nw, user)
                if no_of_friends:
                    print(user, " has ", no_of_friends, " friends.")
                else:
                    print("Inputted name does not exist")

                # Return to main menu
                model.return_to_menu()
            elif int(selected_menu_option) == 5:
                users_no_friends = stats.get_users_little_no_friends(social_nw)
                print("The following users have few or no friends ", users_no_friends)
                continue
            elif int(selected_menu_option) == 6:
                user = model.username_input_mgmt(individual_names)
                relationships = stats.get_relationships_for_user(social_nw, user)
                print(user, " -> ", ", ".join(relationships))

# Run the main function
main()

'''
----------------------------------References------------------------------------
Exception handling - menu check: https://www.educative.io/answers/what-is-valueerror-in-python
'''
