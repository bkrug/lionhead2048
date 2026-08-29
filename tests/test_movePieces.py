from board2048 import BOARD_SIZE, Board2048
from .builders import FakePieceMakerBuilder

def get_board_location(one_dimensional: int):
    return (int(one_dimensional/4), one_dimensional%4)

def get_board_value(board: list[list[int]], one_dimensional: int):
    return board[int(one_dimensional/4)][one_dimensional%4]

TOTAL_BOARD_POSITIONS = 16

def testMoveUp_noPiecesCanMerge_expectExistingPiecesToMove_expectOneNewPiece():
    # Randomly generate locations at the 14th and 3rd empty locations on the board.
    index_13 = 13;
    #
    filled_positions = 7
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(2)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            index_13 - filled_positions)
        .build()
    )
    initial_board = [
        5, 0, 3, 1,
        0, 1, 5, 0,
        0, 0, 0, 3,
        0, 4, 0, 0,
    ]
    expected_board = [
        5, 1, 3, 1,
        0, 4, 5, 3,
        0, 0, 0, 0,
        0, 2, 0, 0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_up()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]