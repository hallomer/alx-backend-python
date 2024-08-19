#!/usr/bin/env python3
"""Asynchronous coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay."""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
