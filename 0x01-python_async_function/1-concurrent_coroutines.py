#!/usr/bin/env python3
"""The module demonstrates the use of
multiple coroutines
"""

wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n, max_delay):
    """The function runs coroutines n number of times
    n: int
    max_delay: int
    """
    number_list = []
    for _ in range(n):
        number_list.append(await wait_random(max_delay))

    return number_list.sort()
