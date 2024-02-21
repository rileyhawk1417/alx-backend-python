#!/usr/bin/env python3

"""The module demonstrates the asyncio module"""
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """The function runs a coroutine 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
