#!/usr/bin/python3
"""function that writes a string to a txt file and returns the number of characters written."""

def write_file(filename="", text=""):
    """Writes a string to a txt file and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)