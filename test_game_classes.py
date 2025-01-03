from game_classes import Hex, HexState, HexMove, HexPlayer
from pytest import raises


def test_Hex_create_typical():
    hex = Hex(3)
    starting_board = hex.state.board
    assert hex.first_player.char == '1'
    assert hex.second_player.char == '2'
    assert starting_board == [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


def test_HexState_get_moves():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1', True), HexPlayer('2', False), board)
    moves = state.get_moves()
    correct_moves = [HexMove((0, 0)), HexMove((1, 1)),
                     HexMove((1, 2)), HexMove((2, 2))]
    assert len(moves) == len(correct_moves)
    for i in range(len(correct_moves)):
        assert correct_moves[i].loc == moves[i].loc


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
    state = HexState(HexPlayer('1', True), HexPlayer('2', False), board)
    new_state = state.make_move(HexMove((1, 2)))
    assert new_state.board == correct_board


def test_HexState_make_move_incorrect_index():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1', True), HexPlayer('2', False), board)
    with raises(IndexError):
        state.make_move(HexMove((3, 2)))


def test_HexState_make_move_incorrect_hex():
    board = [
        [None, '1', '2'],
        ['1', None, None],
        ['2', '1', None]
    ]
    state = HexState(HexPlayer('1', True), HexPlayer('2', False), board)
    with raises(ValueError):
        state.make_move(HexMove((0, 2)))


def test_HexState_take_hexes_around():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        ['2', '1', None]
    ]
    queue = []
    state = HexState(HexPlayer('1', True), HexPlayer('2', False), board)
    hexes_around = state._take_hexes_around((1, 1), '2', queue, [])
    assert (hexes_around[0] in [(0, 2), (2, 0)] and
            hexes_around[1] in [(0, 2), (2, 0)])
    queue.append((0, 2))
    hexes_around = state._take_hexes_around((1, 1), '2', queue, [])
    assert hexes_around[0] in [(2, 0)]


def test_HexState_get_winner_typical():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        ['2', '1', None]
    ]
    player1 = HexPlayer('1', True)
    player2 = HexPlayer('2', False)
    state = HexState(player2, player1, board)
    assert state.get_winner() == player2


def test_HexState_get_winner_wrong_sides_connected():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        ['1', '2', None]
    ]
    player1 = HexPlayer('1', True)
    player2 = HexPlayer('2', False)
    state = HexState(player2, player1, board)
    assert state.get_winner() is None


def test_HexState_get_winner_no_winner_typical():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        [None, None, None]
    ]
    player1 = HexPlayer('1', True)
    player2 = HexPlayer('2', False)
    state = HexState(player2, player1, board)
    assert state.get_winner() is None


def test_HexState_is_finishe_player_won():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        ['2', '1', None]
    ]
    player1 = HexPlayer('1', True)
    player2 = HexPlayer('2', False)
    state = HexState(player2, player1, board)
    assert state.is_finished() is True


def test_HexState_is_finished_game_not_ended():
    board = [
        [None, '1', '2'],
        ['1', '2', None],
        [None, None, None]
    ]
    player1 = HexPlayer('1', True)
    player2 = HexPlayer('2', False)
    state = HexState(player2, player1, board)
    assert state.is_finished() is False
