#!/usr/bin/python3
"""
Module containing the add_integer function.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number (must be an int or float).
        b: The second number (must be an int or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
