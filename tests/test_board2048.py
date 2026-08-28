from board2048 import BOARD_SIZE, Board2048
from .builders import FakePieceMakerBuilder

def get_board_location(one_dimensional: int):
    return (int(one_dimensional/4), one_dimensional%4)

def get_board_value(board: list[list[int]], one_dimensional: int):
    return board[int(one_dimensional/4)][one_dimensional%4]

def testNewGame_firstRandomLocationIsLaterThanSecond_ExpectPiecesInMatchingPositions():
    # Randomly generate locations at the 14th and 3rd empty locations on the board.
    index_14 = 14;
    index_3 = 3;
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(16, index_14)
        .add_expected_powers(2)
        .add_expected_locations(15, index_3)
        .build()
    )

    #Act
    board = Board2048(piece_maker)
    powers = board.get_powers()

    #Assert
    assert get_board_value(powers, index_14) == 1
    assert get_board_value(powers, index_3) == 2

    filled = { get_board_location(index_14), get_board_location(index_3) }
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row, col) not in filled:
                assert powers[row][col] == Board2048.empty_piece()


def testNewGame_firstRandomLocationIsEarlierThanSecond_ExpectPiecesInMatchingPositions():
    # Randomly generate locations at the 3rd and 13th empty locations on the board.
    index_3 = 3;
    index_14 = 14;
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(16, index_3)
        .add_expected_powers(2)
        # Since the 3rd location is filled in first, the 13th empty location is the 14th location.
        .add_expected_locations(15, index_14-1)
        .build()
    )

    #Act
    board = Board2048(piece_maker)
    powers = board.get_powers()

    #Assert
    assert get_board_value(powers, index_3) == 1
    assert get_board_value(powers, index_14) == 2

    filled = { get_board_location(index_3), get_board_location(index_14) }
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row, col) not in filled:
                assert powers[row][col] == Board2048.empty_piece()
