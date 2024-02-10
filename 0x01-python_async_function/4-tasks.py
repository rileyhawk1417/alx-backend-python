#!/usr/bin/env python3

"""The module is a remix of wait_n function
Except that it uses task_wait_random
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks.py").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The function runs coroutines n number of times
    n: int
    max_delay: int
    """
    number_list = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)
                   )))

    return sorted(number_list)
