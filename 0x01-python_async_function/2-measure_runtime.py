#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Your function
should return a float.

The time module to measure an approximate elapsed time.
"""
import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
        Args:
            max_delay: max wait
            n: spawn function

        Return:
            float measure time
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
