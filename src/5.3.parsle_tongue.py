"""Module for extracting hidden lowercase words from a binary file."""

import re
from typing import Iterator

MIN_WORD_LENGTH = 5
CHUNK_SIZE = 4096
WORD_PATTERN = re.compile(rf"[a-z]{{{MIN_WORD_LENGTH},}}".encode("ascii"))


def parsle_tongue(file_path: str) -> Iterator[str]:
    """
    Yields all sequences of at least 5 consecutive lowercase ASCII
    letters found inside a binary file.

    :param file_path: Path to the binary file to scan.
    :return: Iterator of decoded lowercase strings.
    """
    tail = b""

    with open(file_path, "rb") as binary_file:
        while True:
            chunk = binary_file.read(CHUNK_SIZE)
            if not chunk:
                break
            data = tail + chunk
            matches = list(WORD_PATTERN.finditer(data))

            if matches and matches[-1].end() == len(data):
                tail = matches[-1].group(0)
                matches = matches[:-1]
            else:
                tail = data[-(MIN_WORD_LENGTH - 1):]

            for match in matches:
                yield match.group(0).decode("ascii")

    if tail:
        for match in WORD_PATTERN.finditer(tail):
            yield match.group(0).decode("ascii")


if __name__ == "__main__":
    for word in parsle_tongue("./resources/logo.jpg"):
        print(word)