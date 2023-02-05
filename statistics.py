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
            # Get friend count for user
            friend_count = self.get_friends_count_for_user(user[0])
            friend_counts.append([friend_count, user[0]])
            friend_counts_no_names.append(friend_count)
        friend_counts = sorted(friend_counts)

        # Get the lowest number that isn't 0, if 0 exists.
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

    def get_indirect_relationships(self):
        indirect_friends = []
        # Run through all users to get each of their friends lists
        for friends_array in self.all_users_friends:
            user_friends = []
            for each_friend in friends_array[1]:
                # Get relationships for each of the users friends - convert to list, so we can remove the user themselves
                user_friends = list(self.get_relationships_for_user(each_friend))
                user_friends.remove(friends_array[0])

            # Add indirect friends into a list to return
            indirect_friends.append([friends_array[0], user_friends])

        return indirect_friends