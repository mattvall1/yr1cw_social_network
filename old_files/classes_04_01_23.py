"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for all OOP classes
    Date: 04/12/22
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
                # Remove line endings from users list
                users_cleaned = []
                count = 0
                for user in users:
                    if count == 0:
                        # Get total users
                        self.total_users = int(users[0])
                    else:
                        users_cleaned.append(user.replace("\n", ""))
                    count += 1
            return users_cleaned
        else:
            return False

    def get_user(self):
        return self

    def set_data(self):
        return self

    def set_user(self):
        return self


class SignUp:
    def __init__(self):
        self.user_id = []
        self.username = []

    def get_current_users(self):
        return self

    def set_user_id(self):
        return self

    def set_current_user(self):
        return self

    def get_user_id(self):
        return self


class SignIn:
    def __init__(self):
        self.user_id = []
        self.username = []

    def get_user(self):
        return self

    def set_user(self):
        return self


class User:
    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)

    def get_friends(self):
        return self

    def set_friends(self):
        return self

    def add_friend(self):
        return self

    def remove_friend(self):
        return self


class Friends:
    def __init__(self):
        self.common_friends = []

    # Can get data through inheritance perhaps?
    def get_common_friends(self, data):
        # Setup variables
        split_names = []
        all_users_friends = []
        # print(data): ['Adam Bob', 'Bob Amir', 'Bob Mia', 'Chris Zia', 'Mia Amir', 'Liz']

        for item in data:
            # Split list into individual names
            split_names.append(item.split(' '))

        # print(split_names): [['Adam', 'Bob'], ['Bob', 'Amir'], ['Bob', 'Mia'], ['Chris', 'Zia'], ['Mia', 'Amir'], ['Liz']]

        # Reformat array then remove duplicate entries and sort alphabetically
        individual_names_unsorted = sum(split_names, [])
        individual_names = sorted(numpy.unique(individual_names_unsorted))
        # print(individual_names): ['Adam', 'Amir', 'Bob', 'Chris', 'Liz', 'Mia', 'Zia']

        # Run through array
        for user in individual_names: # Foreach user in the network, COUNT the number of friends they have in common with each of the other users.
            # Start by creating a list of friends for each user
            users_friends = []
            for item in split_names:
                # Exception handling, if item[1] does not exist, continue
                try:
                    # Check first item against user to get users friends and add to list
                    if item[0] == user:
                        users_friends.append(item[1])
                    elif item[1] == user:
                        users_friends.append(item[0])
                except IndexError:
                    continue

            # Create a list of users and their friends
            all_users_friends.append([user, users_friends])

        print(all_users_friends)

        return self.common_friends
        # Example of what common friends should look like:
    #       Adam | Amir | Bob | Chris | Mia | Zia | Liz <-- "Columns" of array
        # Adam ->[1,1,0,0,0,0,0] # Adam has 1 friend in common with amir (it's bob)
        # Amir ->[1,2,1,0,1,0,0]
        # Bob ->[0,1,3,0,1,0,0] # Bob has 1 friend in common with amir
        # Chris->[0,0,0,1,0,0,0]
        # Mia ->[1,1,1,0,2,0,0]
        # Zia ->[0,0,0,0,0,1,0]
        # Liz ->[0,0,0,0,0,0,1]
