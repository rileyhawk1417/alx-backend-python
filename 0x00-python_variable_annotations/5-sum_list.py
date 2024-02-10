#!/usr/bin/env python3

"""Module demonstrates on annotating list types"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Get the sum in the List
    then return the sum value
    Args:
        List[float]: input_list
    Returns:
        float
    """
    return float(sum(input_list))
