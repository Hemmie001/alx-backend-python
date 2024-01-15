#!/usr/bin/env python3
"""
This function import wait_random from the previous python file that
I’ve written and write an async routine called wait_n that takes 
n 2 int arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            max_delay: max wait
            n: spawn function

        Return:
            float time random
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
