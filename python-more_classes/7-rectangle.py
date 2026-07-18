#!/usr/bin/python3
"""Define Rectangle"""


class Rectangle:
    """Represents a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Constructor"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter: Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: Width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: Height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle Area"""
        return self.__height * self.__width

    def perimeter(self):
        """Rectangle Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Print Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rows = []
        count = 1
        while count <= self.__height:
            rows.append(print_symbol * self.__width)
            count += 1
        return "\n".join(rows)

    def __repr__(self):
        """String repr of Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when obj is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
