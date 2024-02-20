#!/usr/bin/python3

"""
    MOdule to print out list of attributes
    and methods of a class
"""


def lookup(obj):
    """Look up attribues and methods.
    Args:
        obj(object): the object to list
    Returns:
        list: the list of attributes
    """

    return dir(obj)
