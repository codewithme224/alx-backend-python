#!/usr/bin/env python3
"""Module that takes a float multiplier as argument and returns a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
