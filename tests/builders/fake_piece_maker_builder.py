from ..fake_piece_maker import FakePieceMaker

class FakePieceMakerBuilder:
    def __init__(self):
        self._powers_of_two: list[int] = []
        self._locations: list[tuple[int, int]] = []

    def add_expected_powers(self, random_exponent: int) -> "FakePieceMakerBuilder":
        self._powers_of_two.append(random_exponent)
        return self

    def add_expected_locations(self, free_spaces: int, random_location: int) -> "FakePieceMakerBuilder":
        self._locations.append((free_spaces, random_location))
        return self

    def build(self) -> FakePieceMaker:
        return FakePieceMaker(
            pieces=list(self._powers_of_two),
            locations=list(self._locations),
        )
