import itertools

from .board import gen_board


POSSIBLE_MOVES = [2, 4, 6, 8]


def solve_game(board, depth: int):
    paths = generate_paths(depth)
    for path in paths:
        logging.info(f"Trying path={path}")
        if try_path(board, path) is True:
            return True
    return False


def generate_paths(depth: int):
    return itertools.combinations_with_replacement(POSSIBLE_MOVES, depth)


def try_path(board, path: tuple) -> bool:
    try:
        for move in path:
            board.move(move)
        if board.done() is True:
            return True
    except Exception:
        pass
    return False


if __name__ == "__main__":
    import logging

    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d - %(module)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    b = gen_board()

    depth = 1
    while True:
        logging.info(f"Trying depth={depth}")
        if solve_game(b, depth) is True:
            break
        depth += 1

    print(f"Min moves is {depth}")
