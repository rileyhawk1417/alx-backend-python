#!/usr/bin/env python3
"""The module creates a asyncio.Task using coroutines"""

import asyncio


wait_random = __import__("0-basic_async_syntax.py").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function creates a asyncio task and returns it"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
