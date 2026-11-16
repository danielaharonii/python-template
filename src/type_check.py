"""Module providing a decorator factory for runtime argument type checking."""

from collections.abc import Callable
import functools
from typing import Any, TypeVar

T = TypeVar("T")


class InvalidArgumentTypeError(TypeError):
    """Custom exception raised when a decorated function receives an invalid type."""


def type_check(expected_type: type) -> Callable[[Callable[[Any], T]], Callable[[Any], T]]:
    """
    Decorator factory that validates the single argument passed to the decorated
    function matches `expected_type`.

    :param expected_type: The expected Python type for the function's argument.
    :return: A decorator enforcing the expected argument type.
    """

    def decorator(func: Callable[[Any], T]) -> Callable[[Any], T]:
        """
        Wraps `func` with runtime type verification for its single parameter.

        :param func: The single-argument function to decorate.
        :return: The wrapped function.
        """

        @functools.wraps(func)
        def wrapper(arg: Any) -> T:
            if not isinstance(arg, expected_type):
                raise InvalidArgumentTypeError(
                    f"Expected argument of type {expected_type.__name__}, "
                    f"got {type(arg).__name__} instead."
                )
            return func(arg)

        return wrapper

    return decorator


@type_check(int)
def square_number(number: int) -> int:
    """
    Returns the square of an integer.

    :param number: Integer to square.
    :return: The squared value.
    """
    return number ** 2


if __name__ == "__main__":
    print(square_number(5))
    try:
        square_number("hello")  # type: ignore[arg-type]
    except InvalidArgumentTypeError as error:
        print(f"Caught expected custom error: {error}")