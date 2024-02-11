#!/usr/bin/env python3

"""Demonstrate type annotation this this module"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Create many copies in a tuple"""
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_4x = zoom_array(array, 3)
