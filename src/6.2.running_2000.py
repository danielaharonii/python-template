"""Module for measuring the execution time of a function."""

import time
from collections.abc import Callable
from typing import Any


def timer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Measures and returns the execution time of `func(*args, **kwargs)` in seconds.

    :param func: The callable to benchmark.
    :param args: Positional arguments forwarded to `func`.
    :param kwargs: Keyword arguments forwarded to `func`.
    :return: Elapsed time in seconds.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start_time


if __name__ == "__main__":
    print(timer(sum, range(1_000_000)))