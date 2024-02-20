#!/usr/bin/python3
"""Module to append a text to a file"""


def append_write(filename="", text=""):
    """ Append a string to end pf file
        Args:
            filename: nme of the file to append
            text: text to append to file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
