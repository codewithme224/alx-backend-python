#!/usr/bin/env python3
"""Module that takes a list and returns their sum as a float"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples"""
    return [(i, len(i)) for i in lst]
