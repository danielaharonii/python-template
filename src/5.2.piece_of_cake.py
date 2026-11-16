"""Module for calculating the total price of recipe ingredients."""

from typing import Optional


def get_recipe_price(
    prices: dict[str, float],
    optionals: Optional[list[str]] = None,
    **ingredients: float,
) -> float:
    """
    Calculates total cost of ingredients per 100g, ignoring optional items.

    :param prices: Mapping of ingredient names to price per 100 grams.
    :param optionals: List of optional ingredient names to exclude.
    :param ingredients: Ingredient names mapped to required amounts in grams.
    :return: Total recipe price.
    """
    ignored = set(optionals) if optionals else set()
    return sum(
        (grams / 100.0) * prices[item]
        for item, grams in ingredients.items()
        if item not in ignored and item in prices
    )


if __name__ == "__main__":
    print(get_recipe_price({"chocolate": 18, "milk": 8}, chocolate=200, milk=100))