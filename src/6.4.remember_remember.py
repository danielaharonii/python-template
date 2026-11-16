"""Module for decoding a hidden ASCII message from dark pixels in an image."""

from PIL import Image

BLACK_PIXEL = (0, 0, 0)


def remember_remember(image_path: str) -> str:
    """
    Scans the image column by column and decodes characters whose ASCII code
    equals the row index of the first black pixel (0, 0, 0) in each column.

    :param image_path: Path to the image file.
    :return: Decoded hidden string.
    """
    with Image.open(image_path) as img:
        rgb_img = img.convert("RGB")
        width, height = rgb_img.size
        pixels = rgb_img.load()

        chars: list[str] = []
        for col in range(width):
            for row in range(height):
                if pixels[col, row] == BLACK_PIXEL:
                    chars.append(chr(row))
                    break

    return "".join(chars)


if __name__ == "__main__":
    print(remember_remember("./resources/code.png"))