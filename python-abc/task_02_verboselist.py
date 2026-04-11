#!/usr/bin/python3
"""
Module that defines VerboseList, a subclass of list that prints
messages when modified.
"""


class VerboseList(list):
    """A list that prints messages on modifications."""

    def append(self, item):
        """Add item and print message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print number of items added."""
        length = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{length}] items.")

    def remove(self, item):
        """Print message then remove item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print message then pop item."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
