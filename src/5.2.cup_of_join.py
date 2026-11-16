"""Module for joining multiple lists with a separator element."""

from typing import Any, Optional


def join(*lists: list[Any], sep: Any = "-") -> Optional[list[Any]]:
    """
    Joins any number of lists into a single list separated by `sep`.

    :param lists: Variable number of lists to concatenate.
    :param sep: Element inserted between consecutive lists.
    :return: Combined list, or None if no lists were provided.
    """
    if not lists:
        return None

    result: list[Any] = []
    for index, current_list in enumerate(lists):
        if index > 0:
            result.append(sep)
        result.extend(current_list)
    return result


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep="@"))