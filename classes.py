"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for all OOP classes
    Date: 04/12/22
"""
import os

class Data:
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

    def get_common_friends(self, data):
        for item in data:
            self.common_friends.append(item)

        return self.common_friends
        # Example of what common friends should look like:
        #       Adam | Amir | Bob | Chris | Mia | Zia | Liz <-- "Columns" of array
        # Adam ->[1,1,0,0,0,0,0]
        # Amir ->[1,2,1,0,1,0,0]
        # Bob ->[0,1,3,0,1,0,0]
        # Chris->[0,0,0,1,0,0,0]
        # Mia ->[1,1,1,0,2,0,0]
        # Zia ->[0,0,0,0,0,1,0]
        # Liz ->[0,0,0,0,0,0,1]