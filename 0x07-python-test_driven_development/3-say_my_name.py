#!/usr/bin/python3
"""
The "3-say_my_name" module.

3-say_my_name module supplies 1 func, say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first name> <last name>

        Args:
            first_name (str): the first name
            last_name (str): the last name
    """


    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
