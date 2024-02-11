#!/usr/bin/env python3

"""Module demonstrates on returning a typed tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert the key & value to a tuple
    Then get the square of the value
    """
    return (k, float(v**2))
