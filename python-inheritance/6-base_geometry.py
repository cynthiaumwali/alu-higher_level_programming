#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raise an Exception; area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")