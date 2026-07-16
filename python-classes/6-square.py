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

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate Area"""
        return self.__size ** 2

    @property
    def position(self):
        """Getter: for setting position value"""
        return self.__position

    @position.getter
    def position(self, value):
        """Setter: for setting position value"""
        if not isinstance(value, tuple) and all(x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
	self.__position = value

    def my_print(self):
        """Prints square with char #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        count = 1
        while count <= self.__size:
            print(" " * self.__position[0] + "#" * self.__size)
            count += 1
