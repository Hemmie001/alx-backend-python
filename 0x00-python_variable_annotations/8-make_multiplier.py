#!/usr/bin/env python3
"""
This type-annotated function (make_multiplier) takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float
    """
    def multiplies(n: float):
        """
        multiply two number
        """
        return n * multiplier
    return multiplies
