from powers_of_two import TILE_COLORS
from piece_maker import PieceMaker

BOARD_SIZE = 4


class Board2048:
    @staticmethod
    def empty_power():
        return 0

    def __init__(self, piece_maker: PieceMaker, powers_array:list[int] | None=None):
        self._piece_maker = piece_maker
        is_new_game = not powers_array
        if is_new_game:
            powers_array = [self.empty_power()] * (BOARD_SIZE * BOARD_SIZE)
        self._powers = [
            powers_array[row * BOARD_SIZE:(row + 1) * BOARD_SIZE]
            for row in range(BOARD_SIZE)
        ]
        if is_new_game:
            self._add_random_piece()
            self._add_random_piece()

    def _add_random_piece(self) -> None:
        free_locations = [
            (row, col)
            for row in range(BOARD_SIZE)
            for col in range(BOARD_SIZE)
            if self._powers[row][col] == self.empty_power()
        ]
        location_index = self._piece_maker.get_next_location(len(free_locations))
        row, col = free_locations[location_index]
        self._powers[row][col] = self._piece_maker.get_next_piece()

    def get_powers(self):
        return self._powers

    def get_values(self):
        return [[2 ** power for power in row] for row in self._powers]

    def get_colors(self):
        return [[TILE_COLORS.get(power) for power in row] for row in self._powers]
