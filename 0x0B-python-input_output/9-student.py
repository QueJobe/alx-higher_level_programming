#!/usr/bin/python3

"""
Module for a Student class
"""


class Student():
    """ Student Class"""

    def __init__(self, first_name, last_name, age):
        """ Initialization of instance variables """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary representation of Student """
        return self.__dict__
