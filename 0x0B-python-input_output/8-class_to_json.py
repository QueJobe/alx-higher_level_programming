#!/usr/bin/python3

"""
Module with class_to_json function
"""


def class_to_json(obj):
    """
    Returns the the dictionary description object
    """

    return obj.__dict__
