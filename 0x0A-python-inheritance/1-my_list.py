#!/usr/bin/python3

"""Mylist class module"""


class Mylist(list):
    """Mylist class body"""

    def print_sorted(self):
        """Mothod tp print sorted list"""

        print(sorted(self))


if __name__ = "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
