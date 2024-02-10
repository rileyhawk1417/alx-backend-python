#!/usr/bin/env python3
"""The module demonstrates the use of
multiple coroutines
"""

from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """The function runs coroutines n number of times
    n: int
    max_delay: int
    """
    number_list = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(number_list)
