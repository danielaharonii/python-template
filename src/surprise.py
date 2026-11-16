"""Module providing a decorator that replaces a function's behavior with a surprise."""

from collections.abc import Callable
import functools
from typing import Any

SURPRISE_MESSAGE = "surprise!"


def surprise(func: Callable[..., Any]) -> Callable[..., None]:
    """
    Decorator that overrides the decorated function so that calling it
    prints 'surprise!' instead of executing its original logic.

    :param func: The function to decorate.
    :return: A wrapper function that prints 'surprise!'.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print(SURPRISE_MESSAGE)

    return wrapper


@surprise
def add_numbers(first: int, second: int) -> int:
    """
    Adds two numbers (overridden by the surprise decorator).

    :param first: First integer.
    :param second: Second integer.
    :return: Sum of first and second.
    """
    return first + second


if __name__ == "__main__":
    add_numbers(3, 4)