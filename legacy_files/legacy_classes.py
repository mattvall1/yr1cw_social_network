"""
    Author: Matthew Vallance 001225832
    Purpose: Holder file for all OOP classes
    Date: 04/12/22
"""

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
