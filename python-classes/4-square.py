#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a Square"""

    @property
    def size(self):
        """Getter: for retrieving size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: for setting size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """Initialize a Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate Area"""
        return self.__size ** 2
