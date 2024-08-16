#!/usr/bin/env python3
"""Defines a function that safely gets a value from a dictionary."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value from a dictionary if the key exists,
    otherwise returns default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
