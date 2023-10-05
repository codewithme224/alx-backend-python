#!/usr/bin/env python3
"""Annotating the above function's parameters and return values"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """Annotating the above function's parameters and return values"""
    if key in dct:
        return dct[key]
    else:
        return default
