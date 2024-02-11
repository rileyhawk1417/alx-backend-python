#!/usr/bin/env python3
"""
Module implement's callable functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function with callback"""
    return lambda x: x * multiplier
