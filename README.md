# Calculator

A command-line calculator app that logs the history of your previous calculations.

## Features

- Performs four operations: **addition, subtraction, multiplication, and division**
- Divide-by-zero protection (zero inputs are skipped, not crashed on)
- Records **who** used the calculator and **what** they calculated
- Logs every calculation with the **exact date and time**
- Saves history to a file that **persists across sessions** — close the program, reopen it, your history is still there

## How to Run

1. Make sure Python is installed
2. Run the program:
3. Choose an option from the menu — addition, subtraction, multiplication, division, view history, or exit — then enter your numbers.

## Proof of Persistence

Every calculation is saved to `HISTORY.txt` with a username and timestamp. Open that file to see a live log of real calculations, saved across multiple sessions.

## Planned Features

- Support for full mathematical expressions (e.g. solving `3 + 5 * 2` in one go)
- Combining multiple operations in a single equation
