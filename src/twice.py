"""Module providing a decorator that executes the wrapped function twice."""

from collections.abc import Callable
from typing import Any
import decorator


@decorator.decorator
def twice(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Decorator implemented with `decorator.decorator` that calls the wrapped
    function twice with the given arguments and returns the second result.

    :param func: The target function to execute twice.
    :param args: Positional arguments forwarded to `func`.
    :param kwargs: Keyword arguments forwarded to `func`.
    :return: The return value of the second execution of `func`.
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)


@twice
def greet(name: str) -> None:
    """
    Prints a greeting message for the given name.

    :param name: Name of the person to greet.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("World")