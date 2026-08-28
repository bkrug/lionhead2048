from powers_of_two import TILE_COLORS
from piece_maker import PieceMaker

BOARD_SIZE = 4


class Board2048:
    def empty_power(self):
        return 0


    def __init__(self, piece_maker: PieceMaker, powers_array:list[int] | None=None):
        self._piece_maker = piece_maker
        if not powers_array:
            powers_array = [self.empty_power()] * (BOARD_SIZE * BOARD_SIZE)
        self._powers = [
            powers_array[row * BOARD_SIZE:(row + 1) * BOARD_SIZE]
            for row in range(BOARD_SIZE)
        ]

    def get_powers(self):
        return self._powers

    def get_values(self):
        return [[2 ** power for power in row] for row in self._powers]

    def get_colors(self):
        return [[TILE_COLORS.get(power) for power in row] for row in self._powers]
