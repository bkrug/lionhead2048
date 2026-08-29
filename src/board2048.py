from piece_maker import PieceMaker

BOARD_SIZE = 4

class Board2048:
    @staticmethod
    def empty_power():
        return 0

    def __init__(self, piece_maker: PieceMaker, powers_array:list[int] | None=None):
        self._piece_maker = piece_maker
        if not powers_array:
            self._powers = [[self.empty_power()] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            self._add_random_piece()
            self._add_random_piece()
        else:
            self._powers = [
                powers_array[row * BOARD_SIZE:(row + 1) * BOARD_SIZE]
                for row in range(BOARD_SIZE)
            ]

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

    def move_up(self):
        changed = False
        for col in range(BOARD_SIZE):
            column_values = [self._powers[row][col] for row in range(BOARD_SIZE)]
            merged_values = self._slide_and_merge(column_values)
            if merged_values != column_values:
                changed = True
            for row in range(BOARD_SIZE):
                self._powers[row][col] = merged_values[row]
        if changed:
            self._add_random_piece()

    def move_down(self):
        changed = False
        for col in range(BOARD_SIZE):
            column_values = [self._powers[row][col] for row in range(BOARD_SIZE)]
            merged_values = list(reversed(self._slide_and_merge(list(reversed(column_values)))))
            if merged_values != column_values:
                changed = True
            for row in range(BOARD_SIZE):
                self._powers[row][col] = merged_values[row]
        if changed:
            self._add_random_piece()

    def move_left(self):
        changed = False
        for row in range(BOARD_SIZE):
            merged_values = self._slide_and_merge(self._powers[row])
            if merged_values != self._powers[row]:
                changed = True
            self._powers[row] = merged_values
        if changed:
            self._add_random_piece()

    def move_right(self):
        changed = False
        for row in range(BOARD_SIZE):
            merged_values = list(reversed(self._slide_and_merge(list(reversed(self._powers[row])))))
            if merged_values != self._powers[row]:
                changed = True
            self._powers[row] = merged_values
        if changed:
            self._add_random_piece()

    @staticmethod
    def _slide_and_merge(values: list[int]) -> list[int]:
        non_empty_powers = [value for value in values if value != Board2048.empty_power()]
        merged: list[int] = []
        index = 0
        while index < len(non_empty_powers):
            if index + 1 < len(non_empty_powers) and non_empty_powers[index] == non_empty_powers[index + 1]:
                merged.append(non_empty_powers[index] + 1)
                index += 2
            else:
                merged.append(non_empty_powers[index])
                index += 1
        merged.extend([Board2048.empty_power()] * (len(values) - len(merged)))
        return merged

    def get_powers(self):
        return [row.copy() for row in self._powers]

    def get_max_power(self):
        return max(power for row in self._powers for power in row)

    def get_max_value(self):
        found_max = self.get_max_power()
        if found_max == 0:
            # 2 ** 0 results in 1, which is not a valid value on the gameboard.
            return 0
        else:
            return 2 ** found_max