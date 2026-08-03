#!/usr/bin/python3
"""function that converts a JSON string representation to an object."""


import json


def from_json_string(json_string):
    """Converts a JSON string representation to an object."""
    return json.loads(json_string)
