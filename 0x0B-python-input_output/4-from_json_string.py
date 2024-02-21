#!/usr/bin/python3

"""Module to represent a json string"""

import json


def from_json_string(my_str):
    """function that returns an object
        by a json string.
        Args:
            my_str: sting to convert.
    """

    return json.loads(my_str)
