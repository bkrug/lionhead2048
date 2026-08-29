from board2048 import BOARD_SIZE, Board2048
from .builders import FakePieceMakerBuilder

def get_board_location(one_dimensional: int):
    return (int(one_dimensional/4), one_dimensional%4)

def get_board_value(board: list[list[int]], one_dimensional: int):
    return board[int(one_dimensional/4)][one_dimensional%4]

TOTAL_BOARD_POSITIONS = 16

def testGetMax_twoMaxValuesAreDuplicates():
    piece_maker = FakePieceMakerBuilder().build()
    initial_board = [
        5, 0, 3, 1,
        0, 1, 5, 0,
        0, 0, 0, 3,
        0, 4, 0, 0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)

    #Assert
    assert board.get_max_power() == 5
    assert board.get_max_value() == 32  # 2 to the 5th power is 32

def testGetMax_maxValueIsUnique():
    piece_maker = FakePieceMakerBuilder().build()
    initial_board = [
        5,  0, 3, 10,
        0,  1, 5,  0,
        11, 0, 0,  3,
        0,  4, 0,  0,
    ]

    #Act
    board = Board2048(piece_maker, initial_board)

    #Assert
    assert board.get_max_power() == 11
    assert board.get_max_value() == 2048   # 2 to the 11th power is 2048

def testGetMax_maxValueActuallyIndicatesEmptiness():
    piece_maker = FakePieceMakerBuilder().build()
    initial_board = [
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0
    ]

    #Act
    board = Board2048(piece_maker, initial_board)

    #Assert
    assert board.get_max_power() == 0
    # 2 to the 0th power is 1,
    # but "1" is not a valid value on a 2048 board.
    assert board.get_max_value() == 0