from game_classes import Hex, HexState, HexMove
from two_player_games.player import HexPlayer
from pytest import raises


def test_Hex_create_typical():
    hex = Hex(3)
    starting_board = hex.state.board
    assert hex.first_player.char == '1'
    assert hex.second_player.char == '2'
    assert starting_board == [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]


def test_HexState_get_moves():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1'), HexPlayer('2'), board)
    moves = state.get_moves()
    correct_moves = [HexMove((0, 0)), HexMove((1, 1)),
                     HexMove((1, 2)), HexMove((2, 2))]
    assert moves == correct_moves


def test_HexState_make_move_typical():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    correct_board = [
        [None, '1', '2'],
        ['1', None, '1'],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1'), HexPlayer('2'), board)
    new_state = state.make_move(HexMove((1, 2)))
    assert new_state.board == correct_board


def test_HexState_make_move_incorrect_index():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1'), HexPlayer('2'), board)
    with raises(IndexError):
        state.make_move(HexMove((3, 2)))


def test_HexState_make_move_incorrect_hex():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1'), HexPlayer('2'), board)
    with raises(ValueError):
        state.make_move(HexMove((0, 2)))
