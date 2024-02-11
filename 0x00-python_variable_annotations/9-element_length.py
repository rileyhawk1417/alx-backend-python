#!/usr/bin/env python3

"""Module demonstrates type annotation for functions"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Get the length of a list of sequences"""
    return [(i, len(i)) for i in lst]
