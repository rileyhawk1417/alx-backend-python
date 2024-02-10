#!/usr/bin/env python3
"""The module demonstrates the asyncio module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """The function waits for a random number
    to delay the function.
    max_delay: int
    """
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
