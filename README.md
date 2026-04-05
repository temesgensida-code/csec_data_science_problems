# Problem Solutions

Here is a brief description of how some of the problems from the different levels were solved:

## Level One: Factorial
**File:** `LEVEL_ONE/factorial.py`
The factorial problem was solved using a classic recursive function. The base case checks if `n` is 0 or 1, returning 1. For other values, it recursively calls itself with `n - 1`, multiplying the result by `n`.

## Level Two: Fibonacci
**File:** `LEVEL_TWO/fibonacci.py`
The Fibonacci sequence generator was implemented iteratively. It initializes an empty list and adds the first two terms (0 and 1) directly. For subsequent terms up to `n`, it adds the previous two terms stored in the list by keeping track of two index pointers (`i1` and `i2`), which are incremented in each step.

## Level Three: Calculator
**File:** `LEVEL_THREE/calculator.py`
The calculator was built as an interactive console application using a `while True` loop to provide a continuous prompt. It uses a `match` statement (structural pattern matching) to route the user's choice to the corresponding arithmetic operation (addition, subtraction, multiplication, division). The user can gracefully exit the loop by selecting the exit option.
