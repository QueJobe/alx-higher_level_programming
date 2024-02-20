#!/usr/bin/python3
"""Module to check if instance of a class"""


def is_same_class(obj, a_class):
    """ check if object is instance of a class
    Args:
        obj (object): object to check
        a_class : class argument
    Return:
        True: if obj is a instance of the class
        False: if obj is not an instance
    """

    if type(obj) == a_class:
        return True
    return False
