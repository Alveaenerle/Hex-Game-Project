from two_player_games.game import Game
from two_player_games.move import Move
from two_player_games.player import Player
from two_player_games.state import State


class Hex(Game):
    ''' Class that represents Hex game '''
    FIRST_PLAYER_DEFAULT_CHAR = '1'
    SECOND_PLAYER_DEFAULT_CHAR = '2'

    def __init__(self, size: int=11,
                 first_player: Player=None, second_player: Player=None):
        '''
        Initializes game.

        Parameters:
            size: size of the board as number of hexes creating each side
            first_player: the player that will go first (if None is passed, a player will be created)
            second_player: the player that will go second (if None is passed, a player will be created)
        '''

        self.first_player = first_player or Player(self.FIRST_PLAYER_DEFAULT_CHAR)
        self.second_player = second_player or Player(self.SECOND_PLAYER_DEFAULT_CHAR)

        state = HexState(size, self.first_player, self.second_player)

        super().__init__(state)

    pass


class HexState(State):
    pass


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
