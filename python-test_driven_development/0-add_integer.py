#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Function that adds two integers (or floats).

    Parameters:
    - a: The first number (integer or float).
    - b: The second number (integer or float, default is 98).

    Returns:
    The sum of a and b as an integer.
    """
    # Check if 'a' is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if 'b' is an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Return the sum of a and b after converting them to integers
    return int(a) + int(b)

