#!/usr/bin/python3

"""Mylist class module"""


class Mylist(list):
    """Mylist class body"""

    def print_sorted(self):
        print(sorted(self))


if __name__ = "__main__":
    import doctest
    doctest.testfile("test/1-my_list.txt")