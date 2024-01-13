#!/usr/bin/env python3
"""
This function augment the following code

        # The types of the elements of the input are not know
        def safe_first_element(lst):
            if lst:
                return lst[0]
            else:
                return None

with the correct duck-typed annotations:
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe first element
    """
    if lst:
        return lst[0]
    else:
        return None
