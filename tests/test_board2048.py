import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from board2048 import BOARD_SIZE, Board2048


class FakePieceMaker:
    def __init__(self, pieces: list[int], locations: list[int]):
        self._pieces = iter(pieces)
        self._locations = iter(locations)

    def get_next_piece(self) -> int:
        return next(self._pieces)

    def get_next_location(self, free_spaces: int) -> int:
        return next(self._locations)


def testNewGame_firstRandomLocationIsLaterThanSecond_ExpectPiecesInMatchingPositions():
    # Randomly generate locations at the 14th and 3rd empty locations on the board.
    piece_maker = FakePieceMaker(pieces=[1, 2], locations=[14, 3])

    #Act
    board = Board2048(piece_maker)
    powers = board.get_powers()

    #Assert
    assert powers[3][2] == 1
    assert powers[0][3] == 2

    filled = {(3, 2), (0, 3)}
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row, col) not in filled:
                assert powers[row][col] == Board2048.empty_piece()


def testNewGame_firstRandomLocationIsEarlierThanSecond_ExpectPiecesInMatchingPositions():
    # Randomly generate locations at the 3rd and 13th empty locations on the board.
    # Since the 3rd location is filled in first, the 13th empty location is the 14th location.
    piece_maker = FakePieceMaker(pieces=[1, 2], locations=[3, 13])

    #Act
    board = Board2048(piece_maker)
    powers = board.get_powers()

    #Assert
    assert powers[0][3] == 1
    assert powers[3][2] == 2

    filled = {(0, 3), (3, 2)}
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row, col) not in filled:
                assert powers[row][col] == Board2048.empty_piece()
