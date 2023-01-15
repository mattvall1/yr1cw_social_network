"""
    Author: Matthew Vallance 001225832
    Purpose: Methods for dealing with friends - describe better...
    Date: 15/01/22
"""

class Friends:
    def __init__(self):
        self.common_friends_matrix = []

    # Can get data through inheritance perhaps?
    def get_common_friends(self, all_users_friends):
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