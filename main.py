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
    common_friends = []
    selected_menu_option = 0
    valid_filename = 0
    social_nw = []
    individual_names = []

    # Initialise social network routine
    data_retrieval = data.Data()

    # Ask user to input valid filename, then get data
    while valid_filename == 0:
        data_file = str(input("Insert data filename (or 'n' to quit): "))
        if data_file == "n":
            exit()
        # Separate social_nw and individual names into separate variables
        data_unsplit = data_retrieval.get_data(data_file)
        if data_unsplit:
            valid_filename = 1
            social_nw = data_unsplit[0]
            individual_names = data_unsplit[1]
        else:
            print("Invalid filename")

    while selected_menu_option != 8:
        valid_selection = 0

        # Main menu
        print("Menu: \n 1. Display social network \n 2. Display common friends \n 3. Recommend new friends (option 2 MUST be run FIRST) \n ------ Statistics ------ \n 4. Display number of friends for user \n 5. Display users with the least number of friends/no friends at all \n 6. Display relationships for user \n 7. Display indirect relationships")

        while valid_selection == 0:
            valid_menu_options = [1, 2, 3, 4, 5, 6, 7]
            # Check menu option is correct data type - CAN THIS BE DONE NEATLY?
            try:
                selected_menu_option = int(input("Select an option: "))
                if selected_menu_option in valid_menu_options:
                    valid_selection = 1
                else:
                    print("Invalid selection, try again.")
            except ValueError:
                print('Invalid selection, try again.')
                break

        friends = fr.Friends(social_nw)
        # 1. Display social network
        if int(selected_menu_option) == 1:
            # Pretty print the data
            model.pretty_print(social_nw)

            # Return to main menu
            model.return_to_menu()

        # 2. Display common friends
        elif int(selected_menu_option) == 2:
            common_friends = friends.get_common_friends()
            # Pretty print the data
            model.pretty_print(common_friends)

            # Return to main menu
            model.return_to_menu()

        # 3. Recommend new friends
        elif int(selected_menu_option) == 3:
            user = model.username_input_mgmt(individual_names)
            recommended_friend = friends.get_recommend_friends(common_friends, user)

            # Display message if menu item 2 has not been run
            if recommended_friend != False: # Note: Cannot be simplified, as this can be a blank list
                try:
                    # Print results nicely, first determining whether we need plurals
                    if len(recommended_friend) > 1:
                        print('Recommended friends for ', user, ' are ', ", ".join(recommended_friend))
                    else:
                        print('Recommended friend for ', user, ' is ', recommended_friend[0])
                except IndexError:
                    print('There are no recommended friends for', user)
            else:
                print('You need to run menu option 2 first.')

            # Return to main menu
            model.return_to_menu()

        elif selected_menu_option >= 4:
            # Get stats class for use in all following menu options
            stats = statistics.Statistics(social_nw)

            # 4. Display number of friends for user
            if int(selected_menu_option) == 4:
                user = model.username_input_mgmt(individual_names)
                no_of_friends = stats.get_friends_count_for_user(user)
                if no_of_friends:
                    print(user, " has ", no_of_friends, " friends.")

                # Return to main menu
                model.return_to_menu()
            # 5. Display users with the least number of friends/no friends at all
            elif int(selected_menu_option) == 5:
                users_no_friends = stats.get_users_with_low_friends()
                print("The following users have few or no friends:", ", ".join(users_no_friends))

                # Return to main menu
                model.return_to_menu()
            # 6. Display relationships for user
            elif int(selected_menu_option) == 6:
                user = model.username_input_mgmt(individual_names)
                relationships = stats.get_relationships_for_user(user)
                if relationships:
                    print(user, " -> ", ", ".join(relationships))

                # Return to main menu
                model.return_to_menu()
            # 7. Display indirect relationships
            elif int(selected_menu_option) == 7:
                indirect_friends = stats.get_indirect_relationships()
                # Pretty print the data
                model.pretty_print(indirect_friends)

                # Return to main menu
                model.return_to_menu()

# Run the main function
main()

'''
----------------------------------References------------------------------------
Exception handling - menu check: https://www.educative.io/answers/what-is-valueerror-in-python
'''
