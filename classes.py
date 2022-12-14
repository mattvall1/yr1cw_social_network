"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for all OOP classes
    Date: 04/12/22
"""
import os

class data():
    def __init__(self):
        self.__fileName = ''

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
                for user in users:
                    users_cleaned.append(user.replace("\n", ""))
            return users_cleaned
        else:
            return False

    def set_data(self):
        print('A')


class sign_up():
    def __init__(self):
        self.social_NW = []

    def get_common_friends(self, social_NW, user):
        return social_NW


class sign_in():
    def __init__(self):
        self.social_NW = []


class user():
    def __init__(self, name, age):  # The constructor
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)

    # Example getters and setters.
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name.title()
        else:
            print('This is not a valid name.')

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print('Please enter a whole number.')
