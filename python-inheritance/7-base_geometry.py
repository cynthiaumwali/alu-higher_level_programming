#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raise an Exception; area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))