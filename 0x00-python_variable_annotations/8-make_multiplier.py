#!/usr/bin/env python3
"""Defines a function that returns another function for multiplication."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier."""
    return lambda x: x * multiplier
