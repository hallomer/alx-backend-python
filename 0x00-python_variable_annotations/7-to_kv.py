#!/usr/bin/env python3
"""Defines a function that returns a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and the square of an int/float."""
    return (k, float(v ** 2))
