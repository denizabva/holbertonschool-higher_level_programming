#!/usr/bin/python3
"""
Module that demonstrates mixins with a Dragon class.
"""


class SwimMixin:
    """Provides swimming ability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that combines multiple abilities."""

    def roar(self):
        """Dragon roar method."""
        print("The dragon roars!")
