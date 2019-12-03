import logging


class Board:

    move_direction = {
        8: (-1, 0),
        2: (1, 0),
        6: (0, 1),
        4: (0, -1),
    }

    def __init__(self, *args, **kwargs):
        board = self.board = list(*args, **kwargs)

        dim = self.dimensions = (len(board), len(board[0]))

        win_board = self.win_board = self.gen_win_board(dim)
        logging.info(f"win_board={win_board}")

        # identify zero_pos
        for row_num in range(dim[0]):
            for col_num in range(dim[1]):
                if board[row_num][col_num] == 0:
                    self.zero_pos = [row_num, col_num]

    def move(self, from_where: int) -> None:
        if self.check_input(from_where) is False:
            raise ValueError

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

        if self.check_pos(other_pos) is False:
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

    def check_pos(self, pos: list):
        dim = self.dimensions
        for i in range(len(dim)):
            if pos[i] < 0 or pos[i] >= dim[i]:
                return False
        return True

    def check_input(self, input: int):
        if input not in [2, 4, 6, 8]:
            return False
        return True

    def gen_win_board(self, dim: (int, int)) -> list:
        nums = [i for i in range(dim[0]*dim[1])]
        nums.append(0)
        i = 1
        ret = []
        for _ in range(dim[0]):
            tmp = []
            for _ in range(dim[1]):
                tmp.append(nums[i])
                i += 1
            ret.append(tmp)
        return ret

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
        [1, 2, 3, 9],
        [4, 5, 6, 10],
        [7, 8, 0, 11],
        [12, 13, 14, 15]
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
