"""
    Author: Matthew Vallance 001225832
    Purpose: Getting statistics
    Date: 15/01/22
"""
import numpy
import friends

class Statistics(friends.Friends):
    def __init__(self):
        super().__init__()

    def get_friends_count_for_user(self, social_nw, name):
        for friend in social_nw:
            # Check if name is equal to inputted name, then check the length of their friends
            if friend[0] == name:
                return len(friend[1])

    def get_users_little_no_friends(self, social_nw):
        # Get a list of users and their friend count
        friend_counts = []
        for user in social_nw:
            friend_counts.append([len(user[1]), user[0]])

        friend_counts = sorted(friend_counts)
        print(friend_counts)

        # Get lowest number that isn't 0, if 0 exists
        if friend_counts[0][0] == 0:
            lowest_number = friend_counts[1]
        else:
            lowest_number = friend_counts[0]


        users_with_no_friends = []
        for friend in social_nw:
            if len(friend[1]) == 0:
                users_with_no_friends.append(friend[0])

            if len(friend[1]) == lowest_number:
                users_with_no_friends.append(friend[0])

        return users_with_no_friends

    def get_relationships_for_user(self, social_nw, name):
        for friend in social_nw:
            # Check if name is equal to inputted name, then return their friends
            if friend[0] == name:
                return friend[1]

    def get_indirect_relationships(self, social_nw):
        common_friends = friends.Friends.get_common_friends(self, social_nw)
        print(common_friends)