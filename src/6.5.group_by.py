"""Module for grouping iterable items by a key function."""

from collections import defaultdict
from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def group_by(key_func: Callable[[T], K], iterable: Iterable[T]) -> dict[K, list[T]]:
    """
    Groups elements from `iterable` into a dictionary keyed by `key_func(item)`.

    :param key_func: Callable returning the grouping key for each element.
    :param iterable: Iterable of elements to group.
    :return: Dictionary mapping each key to a list of matching elements.
    """
    grouped: dict[K, list[T]] = defaultdict(list)
    for item in iterable:
        grouped[key_func(item)].append(item)
    return dict(grouped)


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))