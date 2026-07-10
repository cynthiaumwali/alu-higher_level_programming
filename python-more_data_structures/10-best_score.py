#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return a_dictionary
    max_value = list(a_dictionary.values())[0]
    max_key = list(a_dictionary)[0]
    for key, value in a_dictionary.items():
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            max_key = key
    return max_key

