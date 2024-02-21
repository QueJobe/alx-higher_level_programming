#!/usr/bin/python3
"""Module to create object from json file"""

import json


def load_from_json_file(filename):
    """function to load from json file
        Args:
            filename - file name argumment
    """
    with open(filename, encoding="utf-8") as file_loaded:
        return json.load(file+loaded)
