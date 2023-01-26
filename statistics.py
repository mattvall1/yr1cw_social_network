"""
    Author: Matthew Vallance 001225832
    Purpose: Getting statistics
    Date: 15/01/22
"""
import friends
import numpy

class Statistics(friends.Friends):
    def __init__(self, social_nw):
        self.all_users_friends = social_nw
        super().__init__(social_nw)

    def get_friends_count_for_user(self, name):
        for friend in self.all_users_friends:
            # Check if name is equal to inputted name, then check the length of their friends
            if friend[0] == name:
                return len(friend[1])

    def get_users_with_low_friends(self):
        # Get a list of users and their friend count and sort
        friend_counts = []
        friend_counts_no_names = []
        for user in self.all_users_friends:
            friend_counts.append([len(user[1]), user[0]])
            friend_counts_no_names.append(len(user[1])) # No names, to get second-lowest number later on
        friend_counts = sorted(friend_counts)

        # Get lowest number that isn't 0, if 0 exists.
        friend_counts_no_names = sorted(numpy.unique(friend_counts_no_names))
        if friend_counts_no_names[0] == 0:
            lowest_number = friend_counts_no_names[1]
        else:
            lowest_number = friend_counts_no_names[0]

        # Create list of users with no friends
        users_with_no_friends = []
        for friend in friend_counts:
            # If statements to get users with no/low friends
            if friend[0] == 0:
                users_with_no_friends.append(friend[1])
            if friend[0] == lowest_number:
                users_with_no_friends.append(friend[1])

        return users_with_no_friends

    def get_relationships_for_user(self, name):
        for friend in self.all_users_friends:
            # Check if name is equal to inputted name, then return their friends
            if friend[0] == name:
                return friend[1]

    def get_indirect_relationships(self, social_nw):
        common_friends = friends.Friends.get_common_friends(self, social_nw)
        print(common_friends)