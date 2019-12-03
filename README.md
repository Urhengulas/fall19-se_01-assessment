# fall19-se_01-assessment

- [excercise 1: Sliding Puzzle](#excercise-1-sliding-puzzle)
  - [How to play](#how-to-play)
  - [Different starting board](#different-starting-board)
  - [Best of <insert_your_number>](#best-of-insertyournumber)
  - [getting started](#getting-started)
- [Think about ...](#think-about)
  - [generate random boards](#generate-random-boards)
  - [check if board is unsolveable](#check-if-board-is-unsolveable)

## excercise 1: Sliding Puzzle

### How to play

Make a move by pressing one of {`2`, `4`, `6`, `8`} on your keyboard. <br>
They are representing the arrow-keys on a num-pad and are determining in which direction the empty field (`0`) will move.

The goal of the game is to reach this board:
```bash
[1,  2,  3,  4 ]
[5,  6,  7,  8 ]
[9,  10, 11, 12]
[13, 14, 15, 0 ]
```

### Different starting board
To start with a different board change the `board` on lines `95-99`. <br>

### Best of <insert_your_number>
To change the amount of rounds you want to play adapt `max_games` in line `101`

### getting started
1. Have python [installed](https://wiki.python.org/moin/BeginnersGuide/Download)
1. Run game
   ```bash
   $ make run-ex1
   ```
1. Play the game (see [instructions](#how-to-play))

## Think about ...

### generate random boards
1. take the solved board as a starting point
1. apply random moves on it

### check if board is unsolveable
1. test if you can reach that board starting from the solved board