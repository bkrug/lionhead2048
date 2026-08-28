class FakePieceMaker:
    def __init__(self, pieces: list[int], locations: list[tuple[int, int]]):
        self._pieces = iter(pieces)
        self._locations = iter(locations)

    def get_next_piece(self) -> int:
        return next(self._pieces)

    def get_next_location(self, free_spaces: int) -> int:
        expected_free_spaces, location = next(self._locations)
        assert free_spaces == expected_free_spaces
        return location
