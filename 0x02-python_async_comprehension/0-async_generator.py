#!/usr/bin/env python3

"""The module demonstrates the asyncio module"""
import random
import asyncio


async def async_generator():
    """The function runs a coroutine 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        return random.uniform(0, 10)
