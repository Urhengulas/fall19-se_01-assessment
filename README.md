# fall19-se_01-assessment

- [excercise 1: Sliding Puzzle](#excercise-1-sliding-puzzle)
  - [How to play](#how-to-play)
  - [Different starting board](#different-starting-board)
  - [getting started](#getting-started)

## excercise 1: Sliding Puzzle

### How to play

Make a move by pressing one of {`2`, `4`, `6`, `8`} on your keyboard. <br>
They are representing the arrow-keys on a num-pad and are determining in which direction the empty field (`0`) will move.

The goal of the game is to reach this board:
```bash
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
```

### Different starting board
To start with a different board change the `board` on lines `79-82`. <br>
Be aware to also change the `zero_pos` in line `20`.

### getting started
1. Have python [installed](https://wiki.python.org/moin/BeginnersGuide/Download)
1. Run game
   ```bash
   $ make run-ex1
   ```
1. Play the game (see [instructions](#how-to-play))
