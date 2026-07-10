#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0

    total = 0
    if "CM" in roman_string:
        total += 900
        roman_string = roman_string.replace("CM", "")
    if "CD" in roman_string:
        total += 400
        roman_string = roman_string.replace("CD", "")
    if "XC" in roman_string:
        total += 90
        roman_string = roman_string.replace("XC", "")
    if "XL" in roman_string:
        total += 40
        roman_string = roman_string.replace("XL", "")
    if "IX" in roman_string:
        total += 9
        roman_string = roman_string.replace("IX", "")
    if "IV" in roman_string:
        total += 4
        roman_string = roman_string.replace("IV", "")

    for char in roman_string:
        if char == "M":
            total += 1000
        elif char == "D":
            total += 500
        elif char == "C":
            total += 100
        elif char == "L":
            total += 50
        elif char == "X":
            total += 10
        elif char == "V":
            total += 5
        elif char == "I":
            total += 1

    return total
