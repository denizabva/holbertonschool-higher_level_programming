#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """Custom list that can print sorted version."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
