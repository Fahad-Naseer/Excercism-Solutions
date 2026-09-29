"""Functions used in preparing Guido's gorgeous lasagna.

This module contains functions to calculate preparation, baking,
and total elapsed cooking time for a lasagna recipe.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time (in minutes) needed.

    Function that takes the number of lasagna layers as an argument
    and returns how many minutes it takes to prepare them, based on
    the `PREPARATION_TIME` per layer.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The time the lasagna has been baking.

    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    Function that takes the number of lasagna layers and the elapsed
    baking time as arguments, and returns the total elapsed minutes
    spent cooking (preparation + baking).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time