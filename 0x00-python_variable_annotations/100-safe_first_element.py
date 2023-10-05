#!/usr/bin/env python3
"""Module for duck-typed annotations"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augmentation"""
    if lst:
        return lst[0]
    else:
        return None
