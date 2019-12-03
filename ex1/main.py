class Board(list):

    win_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        for row in self:
            print(row)
        return ""


if __name__ == "__main__":

    board = Board([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ])

    while True:
        try:
            print(board)
            i = int(input("Input"))
        except KeyboardInterrupt:
            print("Reveived KeyboardInterrupt")
            break
