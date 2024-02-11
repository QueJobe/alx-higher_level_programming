#!/usr/bin/python3
"""Square class definition"""


class Square:
    """body of the class"""

    def __init__(self, size=0):
        """Initialize a square
        Args:
            size(int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """Function to return area"""
        return(self.__size * self.__size)
