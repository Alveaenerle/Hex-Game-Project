from typing import Iterable, Optional
from two_player_games.game import Game
from two_player_games.move import Move
from two_player_games.player import Player
from two_player_games.state import State


class Hex(Game):
    ''' Class that represents Hex game '''
    FIRST_PLAYER_DEFAULT_CHAR = '1'
    SECOND_PLAYER_DEFAULT_CHAR = '2'

    def __init__(self, size: int = 11,
                 first_player: "HexPlayer" = None, second_player: "HexPlayer" = None):
        '''
        Initializes game.

        Parameters:
            size: size of the board as number of hexes creating each side
            first_player: the player that will go first (if None is passed, a player will be created)
            second_player: the player that will go second (if None is passed, a player will be created)
        '''

        self.first_player = first_player or HexPlayer(self.FIRST_PLAYER_DEFAULT_CHAR)
        self.second_player = second_player or HexPlayer(self.SECOND_PLAYER_DEFAULT_CHAR)

        starting_board = [[None for j in range(size)] for i in range(size)]

        state = HexState(size, self.first_player, self.second_player, starting_board)

        super().__init__(state)


class HexState(State):
    ''' Class that represents a state in the Hex Game '''
    def __init__(self, current_player: "HexPlayer", other_player: "HexPlayer",
                 board: list(list(str))) -> None:
        ''' Creates the state. Do not call directly. '''

        self.board = board
        super().__init__(current_player, other_player)

    def get_moves(self) -> Iterable["HexMove"]:
        board = self.board
        size = len(board)
        moves = []
        for i in range(size):
            for j in range(size):
                if board[i][j] is not None and board[i][j] is not None:
                    moves.append(HexMove((i, j)))
        return moves

    def make_move(self, move: "HexMove") -> "HexState":
        line = move.loc[0]
        column = move.loc[1]

        if self.board[line][column] is not None:
            raise ValueError("Invalid move!")

        new_board = self.board
        new_board[line][column] = self._current_player.char

        next_player = self._other_player
        other_player = self._other_player

        return HexState(next_player, other_player, new_board)

    def _take_hexes_around(self, starting_hex: "HexMove", player_char: str,
                           queue: Iterable[tuple(int, int)]) -> Iterable[tuple(int, int)]:

        size = len(self.board)
        line = starting_hex.loc[0]
        column = starting_hex.loc[1]
        board = self.board

        hexes_around = []
        if line >= 1:
            loc = (line-1, column)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)

        if line <= size - 2:
            loc = (line+1, column)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)

        if column >= 1:
            loc = (line, column-1)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)

        if column <= size - 2:
            loc = (line, column+1)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)

        if column <= size - 2 and line <= size - 2:
            loc = (line+1, column+1)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)

        if column >= 1 and line >= 1:
            loc = (line-1, column-1)
            if loc not in queue and board[loc[0]][loc[1]] == player_char:
                hexes_around.append(loc)


class HexMove(Move):
    '''
    Class that represents move in the hex game

    Variables:
        loc: coordinates of hex on the board as a tuple (line, column)
    '''

    def __init__(self, loc: tuple[int, int]) -> None:
        self.loc = loc


class HexPlayer(Player):
    '''
    Class that represents player in the hex game

    Variables:
        char: a single-character string to represent the player in textual
            representations of game state
        up_down: a boolean value that represents which sides of the board
            the player has
    '''

    def __init__(self, char: str, up_down: bool) -> None:
        self.up_down = up_down
        super().__init__(char)
