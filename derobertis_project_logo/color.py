import random

from colour import Color



def random_color_hex() -> str:
    return Color(pick_for=random.randint(1, 1000000)).get_hex()
