from board2048 import BOARD_SIZE, Board2048
from .builders import FakePieceMakerBuilder


def testNewGame_firstRandomLocationIsLaterThanSecond_ExpectPiecesInMatchingPositions():
    # Randomly generate locations at the 14th and 3rd empty locations on the board.
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(16, 14)
        .add_expected_powers(2)
        .add_expected_locations(15, 3)
        .build()
    )

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
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(16, 3)
        .add_expected_powers(2)
        # Since the 3rd location is filled in first, the 13th empty location is the 14th location.
        .add_expected_locations(15, 13)
        .build()
    )

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
