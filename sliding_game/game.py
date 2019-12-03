
from .board import Board, gen_board


def play_games(max_games: int):
    game_results = []
    for _ in range(max_games):
        b = gen_board()
        r = play_game(b)
        game_results.append(r)

    print(f"Game over.\nYou took {min(game_results)} moves in your best game")


def play_game(board: Board):
    print("### NEW GAMES IS STARTING ###")

    moves_counter = 0
    while True:
        try:
            print("\nState of the game board:")
            print(board, end="")
            i = int(input("Input -> "))
            if Board.check_input(i) is False:
                raise ValueError
            board.move(i)
            moves_counter += 1
            if board.done() is True:
                print(
                    f"\nYou have won!!! (and took {moves_counter} moves)"
                )
                print(board)
                return moves_counter
        except IndexError:
            print("! Invalid move. Please try again.")
        except ValueError:
            print("! Invalid input please use one of < 2 | 4 | 6 | 8 >")
        except KeyboardInterrupt:
            print("Received KeyboardInterrupt")
            break


if __name__ == "__main__":
    import logging

    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d - %(module)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
        # level=logging.INFO,
    )

    play_games(int(input("How many games do you want to play?")))
