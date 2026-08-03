#!/usr/bin/python3
"""function that converts an object to a JSON string representation."""


import json


def to_json_string(my_obj):
    """Converts an object to a JSON string representation."""
    return json.dumps(my_obj)
