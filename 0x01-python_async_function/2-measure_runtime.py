#!/usr/bin/env python3
"""The module measures the runtime for the coroutine"""

import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """The function measures the runtime
    n: int
    max_delay: int
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    stop_time = time.time()
    return (stop_time - start_time) / n
