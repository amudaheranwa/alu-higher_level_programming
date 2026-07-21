#!/usr/bin/python3
"""Defines a function that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line.

    Args:
        my_list (list): A list of integers.
    """
    for number in my_list:
        print(str.format("{}", number))
