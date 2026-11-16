"""Module for generating a random date between two given dates and checking for Monday."""

from datetime import datetime, timedelta
import random

DATE_FORMAT = "%Y-%m-%d"
MONDAY_WEEKDAY = 0


def no_vinnigret(start_date_str: str, end_date_str: str) -> str:
    """
    Picks a random date between two YYYY-MM-DD date strings and prints a warning
    if it falls on a Monday.

    :param start_date_str: First date in YYYY-MM-DD format.
    :param end_date_str: Second date in YYYY-MM-DD format.
    :return: The randomly selected date string in YYYY-MM-DD format.
    """
    first_date = datetime.strptime(start_date_str, DATE_FORMAT).date()
    second_date = datetime.strptime(end_date_str, DATE_FORMAT).date()
    low_date, high_date = sorted((first_date, second_date))

    days_between = (high_date - low_date).days
    chosen_date = low_date + timedelta(days=random.randint(0, days_between))

    if chosen_date.weekday() == MONDAY_WEEKDAY:
        print("I have no vinaigrette!")

    return chosen_date.strftime(DATE_FORMAT)


if __name__ == "__main__":
    print(no_vinnigret("1912-06-23", "1954-06-07"))