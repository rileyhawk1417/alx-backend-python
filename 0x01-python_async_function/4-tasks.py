#!/usr/bin/env python3

"""The module is a remix of wait_n function
Except that it uses task_wait_random
"""

task_wait_random = __import__("3-tasks.py").task_wait_random


async def task_wait_n(n, max_delay):
    """The function runs coroutines n number of times
    n: int
    max_delay: int
    """
    number_list = []
    for _ in range(n):
        number_list.append(await task_wait_random(max_delay))

    return number_list.sort()
