"""
Utility functions
"""
# --- Imports

# Standard library
from __future__ import division, absolute_import, unicode_literals, print_function


# --- Functions

def flag_bits(n):
    """
    Return the bits of a byte as a boolean array.

    Arguments
    ---------
    n (charater):
        8-bit character passed

    Returns
    -------
    list (bool):
        boolean list representing the bits in the byte
        (big endian) ['most sig bit', ... , 'least sig bit' ]

    Example
    -------
    >>> flag_bits('A') # ASCII 65, Binary: 01000001
    [False, True, False, False, False, False, False, True]
    """
    return [x == '1' for x in list('{0:08b}'.format(ord(n)))]
