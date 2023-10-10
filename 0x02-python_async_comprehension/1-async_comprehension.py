#!/usr/bin/env python3
"""Async comprehension"""


import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Async generator that yields random numbers between 0 and 10"""
    return [i async for i in async_generator()]
