# fun-001-syntax - Python Fundamentals & Problem Solving (Syntax)

## Learning Outcomes assessed

- Basic Python syntax
- Conditional statements
- Functions
- Basic loops
- Simple algorithms (problem solving)

## Setup

```bash
sudo chmod +x setup_environment.sh
./setup_environment.sh
```

## Running the tests

```bash
python3 -m pytest tests/test_fundamentals.py -v
```

Run one test:

```bash
python3 -m pytest tests/test_fundamentals.py::TestFunctions::test_pseudo_squares_output -v
```

## Scoring

```
Coding Score = (P / T) x 100%
```

T = total tests, P = tests passed. Pass mark: 60%.

## Project structure

```
fun-001-syntax/
├── fundamentals.py          # starter code with bugs: fix this file
├── tests/test_fundamentals.py
├── solution/fundamentals.py # complete correct answers
└── README.md
```

To check the solution: `cp solution/fundamentals.py fundamentals.py` (back up your own first).

## Question 1 - `pseudo_squares(n)`

Convert this pseudocode to Python. Print each result on its own line.

```
FOR i FROM 1 TO n INCLUSIVE DO
    PRINT i * i
END FOR
```

## Question 2 - `sum_divisible_by_three(n)`

- Compute the sum of the numbers from 1 to n using a loop
- Return `True` if the sum is divisible by 3, otherwise `False`

Fix the loop, the arithmetic and the return condition.

## Question 3 - `countdown_odd(n)`

- Use a loop
- Print all odd numbers from n down to 1 (inclusive), each on its own line
- Decrease n correctly each iteration
- Print nothing if n is less than 1

## Question 4 - `check_passcode(passcode)`

| Condition                                                        | Return value |
| ---------------------------------------------------------------- | ------------ |
| Passcode is empty                                                | `"Invalid"`  |
| Fewer than 8 characters                                          | `"Weak"`     |
| Contains letters and numbers                                     | `"Medium"`   |
| Contains letters, numbers and symbols (`!@#$%^&*`)               | `"Strong"`   |
| Anything else (8+ characters but only one kind of character)     | `"Weak"`     |

Implement `has_letter`, `has_number` and `has_symbol` using `isalpha()`, `isdigit()` and `in '!@#$%^&*'`.

## Question 5 - `reverse_letters_in_words(sentence)`

Reverse the letters inside each word, keeping the word order. Extra spaces are
collapsed to single spaces and leading/trailing spaces are removed.

```
Input:  "  This   is  a test  "
Output: "sihT si a tset"
```

## Goal

Fix every function in `fundamentals.py` so the code is valid Python and all tests pass.
