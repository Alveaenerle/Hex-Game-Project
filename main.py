from game_classes import Hex, HexPlayer, HexMove


def main():
    wrong_coordinates_input = "Wrong coordinates! Try Again"

    wrong_player_char = """\n    Wrong player symbol detected
    Starting game with default players' symbols
    First player - 1
    Second player - 2"""

    player_char_instruction = """\n    Insert each player's character
    Each of them have to be a different, single symbol!
    Otherwise game will automatically assign chars.
    First player will have bottom and uppper side of the board
    Second player will have left and right side of the board\n"""

    print("""
         _     _  _        _   ___ _    ___     _        _       __            _
 \    / |_ |  /  / \ |\/| |_    | / \    | |_| |_   |_| |_ \/   /__  /\  |\/| |_
  \/\/  |_ |_ \_ \_/ |  | |_    | \_/    | | | |_   | | |_ /\   \_| /--\ |  | |_
""")

    print(player_char_instruction)
    first_player_char = input("First player: ")
    second_player_char = input("Second player: ")

    try:
        size = int(input("Board size as an integer value between 2 and 26: "))
        if size <= 1 or size >= 27:
            raise ValueError
    except (TypeError, ValueError):
        size = None

    if (len(first_player_char) != 1 or len(second_player_char) != 1 or
       first_player_char == second_player_char):
        print(wrong_player_char)
        first_player = None
        second_player = None
    else:
        first_player = HexPlayer(first_player_char, True)
        second_player = HexPlayer(second_player_char, False)

    game = Hex(size, first_player, second_player)
    size = len(game.state.board)

    while True:
        print(str(game))
        print(f'\nCurrent player: {game.get_current_player().char}')
        player_input = input("Enter coordinates [column, line]: ")

        if (len(player_input) == 2 and player_input[0].isalpha()
           and player_input[1].isdigit()):
            column = ord(player_input[0]) - 97
            line = int(player_input[1])
        elif (len(player_input) == 3 and player_input[0].isalpha()
              and player_input[1].isdigit() and player_input[2].isdigit):
            column = ord(player_input[0]) - 97
            line = 10*int(player_input[1]) + int(player_input[2])
        else:
            print(wrong_coordinates_input)
            continue

        if line >= 0 and line < size and column >= 0 and column < size:
            move = HexMove((line, column))
            if move in game.get_moves():
                game.make_move(move)
            else:
                print(wrong_coordinates_input)
                continue
        else:
            print(wrong_coordinates_input)
            continue

        if game.is_finished():
            print(str(game))
            print("Game is finished!")
            print(f'Player {game.get_other_player().char} won the game !')
            break


if __name__ == "__main__":
    main()
