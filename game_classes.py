from two_player_games.game import Game
from two_player_games.move import Move
from two_player_games.player import Player
from two_player_games.state import State


class Hex(Game):
    ''' Class that represents Hex game '''
    FIRST_PLAYER_DEFAULT_CHAR = '1'
    SECOND_PLAYER_DEFAULT_CHAR = '2'

    def __init__(self, size: int = 11,
                 first_player: Player = None, second_player: Player = None):
        '''
        Initializes game.

        Parameters:
            size: size of the board as number of hexes creating each side
            first_player: the player that will go first (if None is passed, a player will be created)
            second_player: the player that will go second (if None is passed, a player will be created)
        '''

        self.first_player = first_player or Player(self.FIRST_PLAYER_DEFAULT_CHAR)
        self.second_player = second_player or Player(self.SECOND_PLAYER_DEFAULT_CHAR)

        starting_board = [[False for j in range(size)] for i in range(size)]

        board_info = {
            self.first_player.char: starting_board,
            self.second_player.char: starting_board
        }

        state = HexState(size, self.first_player, self.second_player, board_info)

        super().__init__(state)


class HexState(State):

    def __init__(self, current_player: Player, other_player: Player,
                 board: dict(str, list(list(bool)))) -> None:
        self.board = board
        super().__init__(current_player, other_player)


class HexMove(Move):
    '''
    Class that represents move in the hex game

    Variables:
        player: player which did the move
        loc: coordinates of hex on the board as a tuple (line, column)
    '''

    def __init__(self, player: Player, loc: tuple[int, int]) -> None:
        self.player = player
        self.loc = loc
