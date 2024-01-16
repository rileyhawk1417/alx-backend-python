#!/usr/bin/env python3
"""This module runs a async function"""
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """This function runs an async function
    then generates numbers
    """
    number_list = []
    async for i in async_generator():
        number_list.append(i)
    return number_list
