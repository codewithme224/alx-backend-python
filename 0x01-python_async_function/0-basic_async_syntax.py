#!/usr/bin/env python3
"""Module that waits for a random delay between 0 and max_delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
