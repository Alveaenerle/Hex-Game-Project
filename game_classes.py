from typing import Iterable
from two_player_games.game import Game
from two_player_games.move import Move
from two_player_games.player import Player
from two_player_games.state import State


class Hex(Game):
    '''
    Class that represents Hex game

    Attributes:
        size : int
            Size of the board as the number of hexes creating each side

        first_player : HexPlayer
            Player that started the game
            This player will have upper and bottom sides of the board

        second_player : HexPlayer
            Player that moved after first player
            This player will have left and right sides of the board

        state : HexState
            Current state of the game
    '''
    FIRST_PLAYER_DEFAULT_CHAR = '1'
    SECOND_PLAYER_DEFAULT_CHAR = '2'

    def __init__(self, size: int = 11, first_player: "HexPlayer" = None,
                 second_player: "HexPlayer" = None):
        '''
        Initializes game.

        Parameters:
            size : int
                Size of the board as the number of hexes creating each side

            first_player : HexPlayer
                Player that will go first
                (if None is passed, a player will be created)

            second_player : HexPlayer
                Player that will go second
                (if None is passed, a player will be created)
        '''

        size = size or 11
        self.first_player = first_player or HexPlayer(
            self.FIRST_PLAYER_DEFAULT_CHAR, True)
        self.second_player = second_player or HexPlayer(
            self.SECOND_PLAYER_DEFAULT_CHAR, False)

        starting_board = [[None for j in range(size)] for i in range(size)]

        state = HexState(self.first_player, self.second_player, starting_board)

        super().__init__(state)

    def get_other_player(self):
        '''
        Returns other player
        '''
        return self.state._other_player


class HexState(State):
    '''
    Class that represents a state in the Hex Game

    Attributes:
        _current_player : HexPlayer
            Player that is making move in this state

        _other_player : HexPlayer
            Player that waits in this state

        board : list[list[str]]
            Current state of the board
            First list contains lines which contain chars
            Chars symbolizes which player taken hex
            If None hex is not taken
    '''
    def __init__(self, current_player: "HexPlayer", other_player: "HexPlayer",
                 board: list[list[str]]) -> None:
        '''
        Creates the state. Do not call directly.

        Parameters:
            _current_player : HexPlayer
                Player that is making move in this state

            _other_player : HexPlayer
                Player that waits in this state

            board : list[list[str]]
                Current state of the board
                First list contains lines which contain chars
                Chars symbolizes which player taken hex
                If None hex is not taken
        '''

        self.board = board
        super().__init__(current_player, other_player)

    def get_moves(self) -> Iterable["HexMove"]:
        board = self.board
        size = len(board)
        moves = []
        for i in range(size):
            for j in range(size):
                if board[i][j] is None:
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
        other_player = self._current_player

        return HexState(next_player, other_player, new_board)

    def is_finished(self) -> bool:
        return self.get_winner() is not None

    def get_winner(self) -> Player | None:
        size = len(self.board)
        board = self.board
        queue = []
        visited = []
        if self._other_player.up_down:
            for i in range(size):
                if board[0][i] == self._other_player.char:
                    queue.append((0, i))
            while len(queue):
                curr_hex = queue.pop(0)
                if curr_hex[0] == size-1:
                    return self._other_player
                around = self._take_hexes_around(curr_hex,
                                                 self._other_player.char,
                                                 queue, visited)
                visited.append(curr_hex)
                queue += around
        else:
            for i in range(size):
                if board[i][0] == self._other_player.char:
                    queue.append((i, 0))
            while len(queue):
                curr_hex = queue.pop(0)
                if curr_hex[1] == size-1:
                    return self._other_player
                around = self._take_hexes_around(curr_hex,
                                                 self._other_player.char,
                                                 queue, visited)
                visited.append(curr_hex)
                queue += around
        return None

    def __str__(self) -> str:
        text = ['    ']

        size = len(self.board)
        board = self.board
        player_hex_dict = {
            self.get_current_player().char: '\033[91m⬢\033[00m'
            if self.get_current_player().up_down else '\033[96m⬢\033[00m',
            self._other_player.char: '\033[96m⬢\033[00m'
            if self.get_current_player().up_down else '\033[91m⬢\033[00m'
        }

        for i in range(size):
            text[0] += f'\033[4;31m {chr(i+97)}\033[0m'
            line = f'\033[96m{i*" "} {i:2} \033[96m⧵\033[00m'
            for j in range(size):
                if board[i][j] is not None:
                    line += f'{player_hex_dict[board[i][j]]} '
                else:
                    line += '⬢ '
            line += "\033[96m⧵\033[00m"
            text.append(line)

        text[0] += '\033[4;31m \033[0m'
        overbar = "\u0305" * size
        line = f'{size*" "}    \033[91m{overbar*2}\033[0m'
        text.append(line)

        return '\n'.join(text)

    # Helper methods

    def _take_hexes_around(self, starting_loc: tuple[int, int],
                           player_char: str, queue: list[tuple[int, int]],
                           visited: list[tuple[int, int]]):
        '''
        Takes all hexes around given hex that belong to the player

        Parammeters:
            starting_loc : tuple[int, int]
                Coordinates of starting hex

            player_char : str
                Which player's hexes we want to take

            queue : list[tuple[int, int]]
                Used in BFS algorithm
                Hexes that will be taken the same method

            visited list[tuple[int, int]]
                Used in BFS algorithm
                Hexes that was taken before and cannot be taken
        '''

        line = starting_loc[0]
        column = starting_loc[1]
        board = self.board
        size = len(board)

        hexes_around = []
        if line >= 1:
            loc = (line-1, column)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        if line <= size - 2:
            loc = (line+1, column)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        if column >= 1:
            loc = (line, column-1)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        if column <= size - 2:
            loc = (line, column+1)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        if column >= 1 and line <= size - 2:
            loc = (line+1, column-1)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        if column <= size - 2 and line >= 1:
            loc = (line-1, column+1)
            if (loc not in queue and loc not in visited and
               board[loc[0]][loc[1]] == player_char):
                hexes_around.append(loc)

        return hexes_around


class HexMove(Move):
    '''
    Class that represents move in the hex game

    Attributes:
        loc : tuple[int, int]
            Coordinates of the hex on the board as a tuple[line, column]
    '''

    def __init__(self, loc: tuple[int, int]) -> None:
        '''
        Creates the move

        Parameters:
            loc : tuple[int, int]
                Coordinates of the hex on the board as a tuple[line, column]
        '''
        self.loc = loc

    def __eq__(self, __value: "HexMove") -> bool:
        return self.loc[0] == __value.loc[0] and self.loc[1] == __value.loc[1]


class HexPlayer(Player):
    '''
    Class that represents player in the hex game

    Attributes:
        char: str
            A single-character string to represent the player in textual
            representations of game state
        up_down: bool
            A boolean value that represents which sides of the board
            the player has
    '''

    def __init__(self, char: str, up_down: bool) -> None:
        '''
        Initializes a player

        Parameters;
            char: str
                A single-character string to represent the player in textual
                representations of game state
            up_down: bool
                A boolean value that represents which sides of the board
                the player has
        '''
        self.up_down = up_down
        super().__init__(char)
