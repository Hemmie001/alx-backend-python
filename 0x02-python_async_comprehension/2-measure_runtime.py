#!/usr/bin/env python3
"""
The Import async_comprehension is from the previous file

This measure_runtime coroutine will execute async_comprehension four times
in parallel using asyncio.gather.

The measure_runtime measures the total runtime and return it.

Notice that the total runtime is roughly 10 seconds.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel
        and measure_runtime should measure the total runtime and return it"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
