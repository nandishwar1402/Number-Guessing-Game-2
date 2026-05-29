# 🎯 Number Guessing Game

A simple, fun command-line number guessing game written in Python.

## Features

- 🟢 **3 difficulty levels** — Easy, Medium, and Hard
- 🔥 **Hot / cold hints** — tells you how close your guess is
- 📊 **Scoreboard** — tracks wins, losses, and best round across sessions
- ✅ **Input validation** — handles non-numbers and out-of-range guesses
- 🔁 **Play again** — loop back for as many rounds as you like

## Difficulty Levels

| Level  | Range  | Attempts |
|--------|--------|----------|
| Easy   | 1 – 50  | 10       |
| Medium | 1 – 100 | 7        |
| Hard   | 1 – 200 | 5        |

## Requirements

- Python 3.6 or higher
- No third-party libraries needed

## How to Run

```bash
python number_guessing_game.py
```

## Example Output

```
==========================================
       🎯  NUMBER GUESSING GAME
==========================================

Choose difficulty:
  1. Easy   (1 – 50,   10 attempts)
  2. Medium (1 – 100,   7 attempts)
  3. Hard   (1 – 200,   5 attempts)

Enter choice (1 / 2 / 3): 2

  I've picked a number between 1 and 100.
  You have 7 attempts. Good luck!

  Attempt 1/7 → Your guess: 50
  ✗  Wrong!  Much higher 🔥

  Attempt 2/7 → Your guess: 80
  ✗  Wrong!  A little lower ↓

  Attempt 3/7 → Your guess: 74
  🎉 Correct! The number was 74.
  You guessed it in 3 attempt(s)!
```

## License

This project is open source and available under the [MIT License](LICENSE).
