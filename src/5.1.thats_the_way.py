"""Module for finding files starting with a specific prefix in a directory."""

import os

FILE_PREFIX = "deep"


def thats_the_way(folder_path: str) -> list[str]:
    """
    Finds all files in the given directory whose names start with 'deep'.

    :param folder_path: Relative or absolute path to the target directory.
    :return: A list of matching filenames.
    """
    try:
        entries = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Directory '{folder_path}' was not found.")
        return []
    except NotADirectoryError:
        print(f"Error: '{folder_path}' is not a valid directory.")
        return []

    return [
        entry
        for entry in entries
        if entry.startswith(FILE_PREFIX)
        and os.path.isfile(os.path.join(folder_path, entry))
    ]


if __name__ == "__main__":
    # Example usage with a relative path (as recommended in PRACTICES.md)
    SAMPLE_DIR = "./images"
    matching_files = thats_the_way(SAMPLE_DIR)
    print(f"Files starting with '{FILE_PREFIX}' in '{SAMPLE_DIR}': {matching_files}")