#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """ Function to write a string to a file
        Args:
            filename: name of the file
            text: string to be writen on the file
    """

    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
