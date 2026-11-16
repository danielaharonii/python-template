"""Module for counting alphabetic word lengths in a text string."""

import re

NON_ALPHA_PATTERN = re.compile(r"[^a-zA-Z]")


def count_words(text: str) -> dict[str, int]:
    """
    Cleans non-alphabetic characters from words and maps each lowercase word
    to its character length.

    :param text: Input text string.
    :return: Dictionary mapping cleaned lowercase words to their lengths.
    """
    cleaned_words = [
        NON_ALPHA_PATTERN.sub("", token).lower() for token in text.split()
    ]
    return {word: len(word) for word in cleaned_words if word}


if __name__ == "__main__":
    print(count_words("You see, wire telegraph is a kind of a very, very long cat."))