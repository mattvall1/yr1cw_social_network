"""
    Author: Matthew Vallance 001225832
    Purpose: Classes for processing data from the 'nw' files
    Date: 15/01/22
"""

import os
import numpy

class Data:
    def __init__(self):
        self.__fileName = ''
        self.total_users = 0

    def get_data(self, __fileName):
        # Add file extension to fileName
        __fileName = __fileName + '.txt'

        # Get a list of files in the data directory
        data_file_list = os.listdir('data')
        # Check datafile exists against dir list
        if __fileName in data_file_list:
            # Code to open file (use: nw_data1)
            with open('data/' + __fileName, 'r') as f:
                users = f.readlines()
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
                users_friends = set()
                for item in users_cleaned:
                    # Exception handling, if item[1] does not exist, continue
                    try:
                        # Check first item against user to get users friends and add to list
                        if item[0] == user:
                            users_friends.add(item[1])
                        elif item[1] == user:
                            users_friends.add(item[0])
                    except IndexError:
                        continue

                # Add processed users and their friends into an appropriate data structure
                all_users_friends.append([user, users_friends])

            return all_users_friends
        else:
            return False

    def get_user(self):
        return self

    def set_data(self):
        return self

    def set_user(self):
        return self