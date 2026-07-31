#!/usr/bin/python3
"""Checks if the object is exactly an instance of the specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the specified class or its subclass."""
    
    return isinstance(obj, a_class)