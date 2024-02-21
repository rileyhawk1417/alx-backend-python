#!/usr/bin/env python3
"""This module runs a async function"""
import typing
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """This function runs an async function
    then generates numbers
    """
    return [ran async for ran in async_generator()]
