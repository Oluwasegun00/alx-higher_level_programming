#!/usr/bin/python3

"""Write the Python class MagicClass that does exactly the same as the following Python bytecode."""

import math

class MagicClass:
    """Represent a circle"""
    
    def _init_(self, radius=0):
        """Initialize a MagicClass.

    Arg:
       radius (float or int): The radius of the new MagicClass.
       """
       self._radius = 0
       if type(radius) is not int and type(radius) is not float:
           raise TypeError("radius must be a number")
       self._radius = radius

       def area(self):
           """Return the area of the MagicClass."""
           return (self._radius ** 2 * math.pi)

       def circumference(self):
           """Return the circumference of the MagicClass."""
           return (2 * math.pi * self._radius)
