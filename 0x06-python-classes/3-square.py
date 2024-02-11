#!/usr/bin/python3
"""Square class definition"""


class Square:
    """body of the class"""
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size(int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Function to return area"""
        return(self.__size * self.__size)
