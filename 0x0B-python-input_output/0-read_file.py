#!/usr/bin/python3

"""Module to read a file"""


def read_file(filename=""):
    """function for read_file
    Args:
        filename - file to be read
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
