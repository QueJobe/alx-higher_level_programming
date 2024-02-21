#!/usr/bin/python3
"""Module t write object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """
    write to an object to a text file
    using json.
    Args:
        my_obj (object)- object to write
        filename - file to write to
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
