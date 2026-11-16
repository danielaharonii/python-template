"""Module for interleaving elements from multiple iterables."""

from collections.abc import Iterable, Iterator
from typing import Any


def interleave(*iterables: Iterable[Any]) -> Iterator[Any]:
    """
    Generator yielding elements from each iterable in round-robin order
    until all iterables are exhausted.

    :param iterables: Any number of iterables to interleave.
    :yield: Next interleaved element.
    """
    active_iterators = [iter(it) for it in iterables]
    while active_iterators:
        remaining_iterators = []
        for iterator in active_iterators:
            try:
                yield next(iterator)
                remaining_iterators.append(iterator)
            except StopIteration:
                pass
        active_iterators = remaining_iterators


if __name__ == "__main__":
    print(list(interleave("abc", [1, 2, 3, 4], ("!", "@"))))