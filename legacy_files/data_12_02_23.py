"""
    Author: Matthew Vallance 001225832
    Purpose: Classes for processing data from the 'nw' files
    Date: 15/01/22
"""

import os
import numpy

class Data:
    def __init__(self):
        self.__file_name = ''
        self.total_users = 0

    def get_data(self, __file_name):
        # Add file extension to fileName
        __file_name = __file_name + '.txt'

        # Get a list of files in the data directory
        data_file_list = os.listdir('data')
        # Check datafile exists against dir list
        if __file_name in data_file_list:
            # Code to open file (use: nw_data1)
            with open('data/' + __file_name, 'r') as file:
                users = file.readlines()
                # Remove line endings from users list and split to get list of lists
                users_cleaned = []
                count = 0
                for user in users:
                    if count == 0:
                        # Get total users
                        self.total_users = int(users[0])
                    else:
                        user = user.replace("\n", "")
                        users_cleaned.append(user.split(" "))
                    count += 1

            # Setup variables
            all_users_friends = []

            # Reformat array then remove duplicate entries and sort alphabetically
            individual_names_unsorted = sum(users_cleaned, [])
            individual_names = sorted(numpy.unique(individual_names_unsorted))

            # Create a list of users and their friends
            for user in individual_names:
                # Start by creating a set of friends for each user
                users_friends = []
                for item in users_cleaned:
                    # Exception handling, if item[1] does not exist, continue
                    try:
                        # Check first item against user to get users friends and add to list
                        if item[0] == user:
                            users_friends.append(item[1])
                        elif item[1] == user:
                            users_friends.append(item[0])
                    except IndexError:
                        continue

                # Add processed users and their friends into an appropriate data structure
                all_users_friends.append([user, users_friends])

            # Check consistency of the network before we return all users friends
            for all_users_outer in all_users_friends:
                user_to_compare = all_users_outer[0]
                # Get indirect friends, so we can check if the user exists in
                for each_friend in all_users_outer[1]:
                    indirect_friends = []
                    for all_users_inner in all_users_friends:
                        if all_users_inner[0] == each_friend:
                            # Add indirect friends into temporary list
                            indirect_friends = indirect_friends + list(all_users_inner[1])

                    # If the network is inconsistent, raise an exception. Continue if not
                    if user_to_compare in indirect_friends:
                        continue
                    else:
                        raise Exception("Network is inconsistent")


            return [all_users_friends, individual_names] # Return both the network and ordered list of individual names
        else:
            return False