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

def testMoveDown_noPiecesCanMerge_expectExistingPiecesToMove_expectOneNewPiece():
    # After the move, every free cell is in rows 0-1, so a free cell's
    # position in the free list is just its flat index.
    index_1 = 1;
    #
    filled_positions = 7
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(2)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            index_1)
        .build()
    )
    initial_board = [
        5, 0, 3, 1,
        0, 1, 5, 0,
        0, 0, 0, 3,
        0, 4, 0, 0,
    ]
    expected_board = [
        0, 2, 0, 0,
        0, 0, 0, 0,
        0, 1, 3, 1,
        5, 4, 5, 3,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_down()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]

def testMoveLeft_noPiecesCanMerge_expectExistingPiecesToMove_expectOneNewPiece():
    # The new piece lands at the 4th free cell (flat index 9, i.e. row 2, column 1).
    free_cell_position = 3
    filled_positions = 8
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(2)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            free_cell_position)
        .build()
    )
    initial_board = [
        5, 0, 3, 1,
        0, 1, 5, 0,
        0, 0, 0, 3,
        0, 4, 0, 2,
    ]
    expected_board = [
        5, 3, 1, 0,
        1, 5, 0, 0,
        3, 2, 0, 0,
        4, 2, 0, 0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_left()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]

def testMoveUp_somePiecesCanMerge_expectMergedPieces_expectOneNewPiece():
    # Randomly generate locations at the 14th and 3rd empty locations on the board.
    index_8 = 8;
    #
    filled_positions = 5
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            index_8 - filled_positions)
        .build()
    )
    # Column 0: New piece should not auto-merge with old piece
    # Column 1: Non-consecutive pieces can merge
    # Column 2: Consecutive pieces can merge
    # Column 3: Four identical pieces will only become two identical pieces
    initial_board = [
        1, 0, 3, 2,
        0, 1, 3, 2,
        0, 0, 0, 2,
        0, 1, 0, 2,
    ]
    expected_board = [
        1, 2, 4, 3,
        0, 0, 0, 3,
        1, 0, 0, 0,
        0, 0, 0, 0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_up()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]

def testMoveDown_somePiecesCanMerge_expectMergedPieces_expectOneNewPiece():
    # After the move, every free cell is in rows 0-2 (column-wise
    # from the top), so a free cell's position in the free list is
    # just its flat index.
    index_4 = 4;
    #
    filled_positions = 5
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            index_4)
        .build()
    )
    # Column 0: New piece should not auto-merge with old piece
    # Column 1: Non-consecutive pieces can merge
    # Column 2: Consecutive pieces can merge
    # Column 3: Four identical pieces will only become two identical pieces
    initial_board = [
        1, 0, 3, 2,
        0, 1, 3, 2,
        0, 0, 0, 2,
        0, 1, 0, 2,
    ]
    expected_board = [
        0, 0, 0, 0,
        1, 0, 0, 0,
        0, 0, 0, 3,
        1, 2, 4, 3,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_down()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]

def testMoveLeft_somePiecesCanMerge_expectMergedPieces_expectOneNewPiece():
    # The new piece lands at the 4th free cell (flat index 5, i.e. row 1, column 1).
    free_cell_position = 3
    filled_positions = 5
    piece_maker = (
        FakePieceMakerBuilder()
        .add_expected_powers(1)
        .add_expected_locations(
            TOTAL_BOARD_POSITIONS - filled_positions,
            free_cell_position)
        .build()
    )
    # Row 0: New piece should not auto-merge with old piece
    # Row 1: Non-consecutive pieces can merge
    # Row 2: Consecutive pieces can merge
    # Row 3: Four identical pieces will only become two identical pieces
    initial_board = [
        1, 0, 0, 0,
        0, 1, 0, 1,
        3, 3, 0, 0,
        2, 2, 2, 2,
    ]
    expected_board = [
        1, 0, 0, 0,
        2, 1, 0, 0,
        4, 0, 0, 0,
        3, 3, 0, 0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)
    board.move_left()
    actual_board = [power for row in board.get_powers() for power in row]

    #Assert
    for flattend_index in range(TOTAL_BOARD_POSITIONS):
        assert expected_board[flattend_index] == actual_board[flattend_index]