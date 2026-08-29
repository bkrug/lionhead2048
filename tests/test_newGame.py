from board2048 import BOARD_SIZE, Board2048
from .builders import FakePieceMakerBuilder

def get_board_location(one_dimensional: int):
    return (int(one_dimensional/4), one_dimensional%4)

def get_board_value(board: list[list[int]], one_dimensional: int):
    return board[int(one_dimensional/4)][one_dimensional%4]

def testNewGame_secondTileIndexBeforeFirstTileIndex_ExpectNoShiftNeeded():
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
                assert powers[row][col] == Board2048.empty_power()


def testNewGame_secondTileIndexAfterFirstTileIndex_ExpectShiftedPastFilledCell():
    # Randomly generate locations at the 3rd and 13th empty locations on the board.
    index_3 = 3;
    index_14 = 14;
    # The 3rd empty cell is filled first, so among the remaining empty cells,
    # index_14's cell is now the 13th (index_14 - 1) empty one, not the 14th.
    index_14_after_index_3_filled = index_14 - 1
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(16, index_3)
        .add_expected_powers(2)
        .add_expected_locations(15, index_14_after_index_3_filled)
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
                assert powers[row][col] == Board2048.empty_power()
