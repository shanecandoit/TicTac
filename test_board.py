
from board import Board

def test_new_board():
    b = Board()
    assert b.__str__() == '''_, _, _
_, _, _
_, _, _'''
    assert not b.won
    assert b.turn == 1


def test_prompt_turn():
    b = Board()
    x, y = b.prompt_turn('1 1')
    print(x, y)
    assert x, y == (1, 1)


def test_move():
    b = Board()
    b.move(1, 1, Board.X)
    assert str(b) == '''x, _, _
_, _, _
_, _, _'''
    b.move(2, 2, Board.O)
    assert str(b) == '''x, _, _
_, o, _
_, _, _'''


def test_uppercase():
    assert "test".upper() == 'TEST'