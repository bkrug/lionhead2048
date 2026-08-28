import random


class PieceMaker:
    def __init__(self, seed_value: int | None):
        if (seed_value!=None):
            random.seed(seed_value)

    def get_next_piece(self) -> int:
        return 1 if random.random() < 0.9 else 2

    # Really generates a random number that the caller has to then translate into a free location
    def get_next_location(self, free_spaces: int) -> int:
        random.random() * free_spaces