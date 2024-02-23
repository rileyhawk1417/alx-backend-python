#!/usr/bin/env python3
"""
Module measures runtimes
"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """This function runs a coroutine 4 times
    then measures the time
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop_time = time.time()
    return stop_time - start_time
