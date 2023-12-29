from game_classes import Hex


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
