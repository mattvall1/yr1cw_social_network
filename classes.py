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
        self.common_friends_matrix = []

    # Can get data through inheritance perhaps?
    def get_common_friends(self, data):
        # Setup variables
        all_users_friends = []

        # Reformat array then remove duplicate entries and sort alphabetically
        individual_names_unsorted = sum(data, [])
        individual_names = sorted(numpy.unique(individual_names_unsorted))

        # Run through array
        for user in individual_names:
            # Start by creating a set of friends for each user
            users_friends = set()
            for item in data:
                # Exception handling, if item[1] does not exist, continue
                try:
                    # Check first item against user to get users friends and add to list
                    if item[0] == user:
                        users_friends.add(item[1])
                    elif item[1] == user:
                        users_friends.add(item[0])
                except IndexError:
                    continue

            # Create a list of users and their friends
            all_users_friends.append([user, users_friends])

        # Run through the list of users and their friends
        for user in all_users_friends:
            common_friends = []
            user_to_compare_friends = user[1]

            # Run through the list of users and their friends again, to work out common friends for each other user
            for friend in all_users_friends:
                user_to_compare_friends_2 = friend[1]

                # Intersection of the two sets of friends - gets a count of the common friends
                friends_intersection = user_to_compare_friends & user_to_compare_friends_2
                common_friends.append(len(friends_intersection))
            # Put the commons friends matrix into an appropriate data structure
            self.common_friends_matrix.append([user[0], common_friends])

        return self.common_friends_matrix

    def recommend_friend(self, common_friends, user): # HOW TO GET THIS FROM CLASS, NOT PASS
        # Check to see if the common friends matrix is filled
        if len(common_friends) == 0:
            print("You need to run menu option 2 first.")
            return False

        if user == '': # ADD PROPER CHECKS HERE
            print("Invalid username.")
            return False

        # Setup variables
        user_friends = 0
        found_friend = 0
        recommended_friend = ''

        # Find a match for the given user and get common friends count
        for friends in common_friends:
            if friends[0] == user:
                user_friends = friends[1]

        # Get position of second highest number in common friends count
        user_friends.sort()
        highest_count_position = user_friends.index(user_friends[-2])

        # Get the name of the recommended friend(s)
        recommended_friend = common_friends[highest_count_position][0]

        print(highest_count_position)
        print(user_friends)

        return recommended_friend
