from powers_of_two import TILE_COLORS

BOARD_SIZE = 4


class Board2048:
    def __init__(self, powers_array=None):
        if not powers_array:
            powers_array = [0] * (BOARD_SIZE * BOARD_SIZE)
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
