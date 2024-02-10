#!/usr/bin/env python3

"""Module demonstrates on dealing with a mixed list type"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Get the sum from  a list of int's and floats"""
    return float(sum(mxd_lst))
