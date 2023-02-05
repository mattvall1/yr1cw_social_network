"""
    Author: Matthew Vallance 001225832
    Purpose: Class with methods for processing the friends and accompanying data - F2
    Date: 15/01/22
"""

class Friends:
    def __init__(self, social_nw):
        self.common_friends_matrix = []
        self.all_users_friends = social_nw

    def get_common_friends(self):
        # Run through the list of users and their friends
        for user in self.all_users_friends:
            common_friends = []
            user_to_compare_friends = set(user[1])

            # Run through the list of users and their friends again, to work out common friends for each other user
            for friend in self.all_users_friends:
                user_to_compare_friends_2 = set(friend[1])

                # Intersection of the two sets of friends - gets a count of the common friends
                common_friends.append(len(user_to_compare_friends & user_to_compare_friends_2))
            # Put the commons friends matrix into an appropriate data structure
            self.common_friends_matrix.append([user[0], common_friends])

        return self.common_friends_matrix

    def get_recommend_friends(self, common_friends, user):
        # Check to see if the common friends matrix is filled
        if len(common_friends) == 0:
            return False

        # Setup variables
        user_friends = []

        # Find a match for the given user and get common friends count
        for friends in common_friends:
            if friends[0] == user:
                user_friends = friends[1]

        # Split into a sorted/unsorted user_friends array to use later
        user_friends_unsorted = user_friends
        user_friends = sorted(user_friends)

        # Get second-highest number in common friends
        user_to_add = user_friends[-2]

        # Get a list of users friends, to compare later on
        users_current_friends = []
        for users_friends_names in self.all_users_friends:
            if users_friends_names[0] == user:
                users_current_friends = users_friends_names[1]

        # Get the name(s) of the recommended friend(s)
        recommended_friends = []
        count = 0
        for number in user_friends_unsorted:
            # Make sure we don't recommend any of current friends - first,
            if number == user_to_add and common_friends[count][0] != user and common_friends[count][0] not in users_current_friends:
                recommended_friends.append(common_friends[count][0])
            count += 1

        return recommended_friends