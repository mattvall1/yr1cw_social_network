"""
    Author: Matthew Vallance 001225832
    Purpose: Getting statistics
    Date: 15/01/22
"""
import friends

class Statistics(friends.Friends):
    def __init__(self):
        super().__init__()

    def get_friends_count_for_user(self, social_nw, name):
        for friend in social_nw:
            # Check if name is equal to inputted name, then check the length of their friends
            if friend[0] == name:
                return len(friend[1])

    def get_users_with_no_friends_at_all(self, social_nw, name):
        pass
    def get_relationships_for_user(self, social_nw, name):
        for friend in social_nw:
            # Check if name is equal to inputted name, then return their friends
            if friend[0] == name:
                return friend[1]

    def get_indirect_relationships(self, social_nw):
        common_friends = friends.Friends.get_common_friends(self, social_nw)
        print(common_friends)