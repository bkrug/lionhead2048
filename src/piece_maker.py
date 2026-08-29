import random


class PieceMaker:
    def __init__(self, seed_value: int | None = None):
        if (seed_value!=None):
            random.seed(seed_value)

    def get_next_piece(self) -> int:
        return 1 if random.random() < 0.9 else 2

    def get_next_location(self, free_spaces: int) -> int:
        """Return a 0-based index, chosen uniformly among `free_spaces` options, into the board's currently-empty cells listed in row-major order."""
        return int(random.random() * free_spaces)