#!/usr/bin/env python3
"""The module demonstrates the asyncio module"""

import asyncio
import random


async def wait_random(max_delay=10):
    """The function waits for a random number
    to delay the function.
    max_delay: int
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return delay
