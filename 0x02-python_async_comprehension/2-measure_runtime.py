#!/usr/bin/env python3

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """This function runs a coroutine 4 times
    then measures the time
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    stop_time = time.time()
    total_time = stop_time - start_time
    return total_time
