#!/usr/bin/python3
"""MyList, a list subclass prints itself sorted."""


class MyList(list):
    """A list that can print its contents in ascending sorted order."""

    def print_sorted(self):
        """Print the list's elements sorted in ascending order."""
        print(sorted(self))