#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """Custom list that can print sorted values."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
