import logging


class Board:

    win_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    move_direction = {
        8: (-1, 0),
        2: (1, 0),
        6: (0, 1),
        4: (0, -1),
    }

    def __init__(self, *args, **kwargs):
        self.zero_pos = [2, 2]
        self.board = list(*args, **kwargs)

    def move(self, from_where: int) -> None:
        board = self.board
        zero_pos = self.zero_pos
        direc = self.move_direction[from_where]
        logging.info(f"zero_pos={zero_pos}")

        # get position of other pirece
        other_pos = zero_pos.copy()
        other_pos[0] += direc[0]
        other_pos[1] += direc[1]
        logging.info(f"other_pos={other_pos}")

        logging.info(f"direc={direc}")

        if self.check_input(other_pos) is False:
            raise IndexError

        # set value at zero_pos to other_val
        board[zero_pos[0]][zero_pos[1]] = board[other_pos[0]][other_pos[1]]
        # set value at other_pos to 0
        board[other_pos[0]][other_pos[1]] = 0

        self.zero_pos = other_pos

    def done(self) -> bool:
        if self.board == self.win_board:
            return True
        return False

    def check_input(self, pos: list):
        for val in pos:
            if val < 0 or val > 2:
                return False
        return True

    def __repr__(self):
        for row in self.board:
            print(row)
        return ""


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d - %(module)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
        # level=logging.INFO,
    )

    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    while True:
        try:
            print("\nState of the game board:")
            print(board, end="")
            i = int(input("Input -> "))
            board.move(i)
            if board.done() is True:
                print("\nYou have won!!!")
                print(board)
                break
        except IndexError:
            print("! Invalid move. Please try again.")
        except ValueError:
            print("! Invalid input please use one of < 2 | 4 | 6 | 8 >")
        except KeyboardInterrupt:
            print("Reveived KeyboardInterrupt")
            break

    print("Game over")
