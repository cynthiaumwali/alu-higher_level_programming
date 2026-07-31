#!/usr/bin/python3
""" function that returns the list of available attributes and methods of an object"""
def lookup(obj):
    """Return the attributes/methods of obj."""
    return dir(obj)
