---
name: wordle
description: |
  Python Wordle game helper and developer skill. Use when the user wants to play Wordle,
  understand how the game works, extend or modify the code, debug issues, or run the game
  in a Jupyter Notebook environment. Covers the full wordle.py implementation: random word
  selection, guess validation, letter-matching logic (exact/exists/absent), pandas DataFrame
  display with color formatting, and the 6-attempt game loop.
  Trigger on: wordle, play wordle, wordle game, word guessing game, wordle python, wordle notebook.
---

# Wordle Game Skill

Python implementation of the Wordle word-guessing game, designed to run in a Jupyter Notebook.

## Repository Layout

```
wordle.py        — Full game implementation (import this)
Wordle.ipynb     — Jupyter Notebook to play interactively
README.md        — Setup and gameplay instructions
```

## How to Play

1. Open `Wordle.ipynb` in Jupyter Notebook (required for colored DataFrame display)
2. Run `from wordle import *` then call `play_wordle()`
3. The game picks a random 5-letter English noun/verb/adjective
4. You have **6 attempts** to guess the word
5. After each guess, letters are color-coded:
   - **GREEN** (uppercase, length 1) — correct letter, correct position
   - **ORANGE** (length 2, letter + space) — correct letter, wrong position
   - **black / lowercase** — letter not in the word

## Key Functions

| Function | Description |
|---|---|
| `play_wordle()` | Main entry point — runs a full game loop |
| `pick_random_word()` | Picks a random 5-letter word via `RandomWords` API |
| `ask_user_input()` | Prompts user, validates 5-letter string input |
| `mark_letters(guess_idx)` | Applies YES/EX/None match tags to each letter |
| `build_df(attempt, guess_arr)` | Builds a single-row pandas DataFrame for the guess grid |
| `color_positive(val)` | Pandas styler function — maps letter format to color |

## Matching Logic

1. **Exact match** (`YES`) — letter and position both match the target word
2. **Exists** (`EX`) — letter is in the word but at a different position; only counted up to the frequency of that letter in the target word
3. **Absent** — letter is not in the remaining unmatched letters of the target

## Dependencies

```
random_word     — random word API
numpy           — array operations for letter comparison
pandas          — guess grid display
matplotlib      — (imported, available for extensions)
IPython.display — display() for styled DataFrames in Jupyter
```

Install with:
```bash
pip install random_word numpy pandas matplotlib ipython
```

## Common Tasks

### Run a game
```python
from wordle import *
play_wordle()
```

### Test the matching logic manually
```python
from wordle import *
import numpy as np

true_word = "CRANE"
guess_word = "CARES"
true_arr = np.array(list(true_word))
guess_arr = np.array(list(guess_word))
# step through mark_letters to inspect match output
```

### Extend with a custom word list
Replace `pick_random_word()` with a function that draws from your own list:
```python
import random
MY_WORDS = ["FLAME", "CRISP", "BLUNT", "GLOOM", "VIVID"]
def pick_random_word():
    return random.choice(MY_WORDS)
```

## Known Constraints

- Must run in **Jupyter Notebook** for color output — terminal mode shows guesses but without color
- `RandomWords` API requires an internet connection and occasionally returns `None`; the `pick_random_word()` function retries until a valid word is returned
- Words are uppercased internally; user input is case-insensitive
