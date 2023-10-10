#!/usr/bin/env python3
"""Measure the runtime"""


import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it."""
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = perf_counter()
    return end_time - start_time
