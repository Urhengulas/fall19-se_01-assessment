class Board(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":

    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])
    print(board)
