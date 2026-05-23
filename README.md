# To-Do List - Python Project 1

DecodeLabs Industrial Training Kit | Batch 2026

---

## Project Overview

This is Project 1 of the DecodeLabs Python Industrial Training Program. The project demonstrates core data management concepts by building a command-line To-Do List application. The focus is on mastering Python lists and dictionaries as the foundation of all database systems.

---

## Objectives

- Build a program where users can add and view tasks through programmatic logic
- Master Python list operations: `append()` and iteration with `enumerate()`
- Understand the IPO model: Input, Process, Output
- Model data using dictionaries (equivalent to a database table row)
- Implement data persistence using JSON file serialization

---

## Key Concepts Covered

- Python Lists as dynamic arrays stored in heap memory
- Dictionary as an in-memory database row (`id`, `task`, `status`)
- `list.append()` as the equivalent of `INSERT INTO` in SQL
- `enumerate()` for Pythonic indexed iteration
- JSON serialization to persist data from volatile RAM to disk
- IPO architecture: separating data logic from user interface

---

## Features

- Add a new task with a description
- View all tasks with status indicators (pending or done)
- Mark a task as completed
- Delete a task
- Auto-save to a JSON file for persistence across sessions

---

## Project Structure

```
project-1-todo-list/
    todo_list.py       - Main application file
    tasks.json         - Auto-generated data file (created on first run)
    README.md          - Project documentation
```

---

## Requirements

- Python 3.6 or higher
- No external libraries required (uses built-in `json` and `os` modules only)

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/project-1-todo-list.git
```

2. Navigate into the project directory:

```bash
cd project-1-todo-list
```

3. Run the application:

```bash
python todo_list.py
```

---

## Usage

On launch, a menu is displayed:

```
------------------------------------------
  DecodeLabs To-Do List - Project 1
------------------------------------------
  1. Add a new task
  2. View all tasks
  3. Mark a task as done
  4. Delete a task
  5. Exit
------------------------------------------
```

Enter the number corresponding to your desired action and follow the on-screen prompts.

---

## Data Persistence

Tasks are saved automatically to `tasks.json` after every add, update, or delete operation. This demonstrates the concept of moving data from volatile memory (RAM) to permanent storage (disk) using JSON serialization.

---

## Architecture

This project follows the IPO model used in every backend system:

| Stage   | Role              | Code Element              |
|---------|-------------------|---------------------------|
| Input   | Data entry        | `input()` function        |
| Process | Logic/modification| List and dictionary ops   |
| Output  | Display/view      | `print()` with `enumerate`|

---

## Author

Name: [Your Full Name]  
Internship Program: DecodeLabs Industrial Training Kit  
Batch: 2026  
Contact: decodelabs.tech@gmail.com  
Website: www.decodelabs.tech

---

## License

This project is submitted as part of the DecodeLabs Internship Program. All rights reserved by the respective author.

# Expense Tracker

**Project 2 | DecodeLabs Internship | Batch 2026**

---

## Overview

A command-line Expense Tracker built in Python that demonstrates the Accumulator Pattern, Sentinel Value (Kill Switch) mechanism, and the Input-Process-Output (IPO) architectural model. The program collects expense entries from the user one at a time, shows a running total after each entry, and produces a detailed final report with breakdown and average calculation.

---

## Features

- Continuous expense entry with real-time running total feedback
- Sentinel value ('done') to cleanly terminate input collection
- Defensive input validation - rejects non-numeric and negative values
- Detailed final report with itemized breakdown and average
- Handles edge case of zero expenses entered
- No external dependencies - standard library only

---

## Architecture

The program follows a strict three-phase IPO model with Model-View separation:

| Phase | Function | Responsibility |
|-------|----------|----------------|
| Input | `get_valid_expense()` | Validate each expense entry and detect sentinel |
| Process | `run_expense_tracker()` | Accumulate totals and maintain state |
| Output | `display_summary()` | Present final formatted report |

---

## Key Concepts

### Accumulator Pattern

The core design pattern of this project. A running total is maintained throughout the session rather than summing a list at the end:

```python
total_expenses = 0.0                          # Initial state
total_expenses = total_expenses + expense     # Accumulation step
```

### Sentinel Value (Kill Switch)

The string `'done'` signals end of input. It is checked before any numeric conversion, making the loop termination clean and explicit:

```python
if user_input.lower() == 'done':
    return None
```

### Defensive Input Handling

- Type conversion via `float()` prevents string concatenation errors
- Negative value rejection with user-friendly error messages
- `ValueError` exception handling for non-numeric input

---

## Requirements

- Python 3.x
- No external packages required

All functionality relies on Python built-in features (`input()`, `float()`, `enumerate()`, `try/except`).

---

## Usage

```bash
python Python_Project_2.py
```

**Sample interaction:**

```
==================================================
   DECODELABS EXPENSE TRACKER (Project 2)
   Enter expenses one by one. Type 'done' to finish.
==================================================

Enter expense amount (or 'done' to finish): 150
   Added: $150.00 | Total so far: $150.00

Enter expense amount (or 'done' to finish): 75.50
   Added: $75.50 | Total so far: $225.50

Enter expense amount (or 'done' to finish): done

==================================================
           FINAL EXPENSE REPORT
==================================================
Total number of expenses: 2
TOTAL SPENT: $225.50

Expense breakdown:
   1. $150.00
   2. $75.50

Average expense: $112.75
==================================================
Transaction complete.
==================================================
```

---

## File Structure

```
Project2/
├── Python_Project_2.py        # Main program file
├── README.md                  # This file
└── Project2_Documentation.docx   # Full technical documentation
```

---

## Functions

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `get_valid_expense()` | None | `float` or `None` | Validates input; returns None on sentinel |
| `run_expense_tracker()` | None | None | Main accumulator loop and flow control |
| `display_summary(total, count, expenses)` | `float, int, list` | None | Renders final report |

---

## Input Validation Rules

| Input | Behavior |
|-------|----------|
| Positive number (e.g. `100`, `50.75`) | Accepted and accumulated |
| `done` (any case) | Triggers kill switch, ends input phase |
| Negative number (e.g. `-20`) | Rejected with error message |
| Non-numeric string (e.g. `abc`) | Rejected with error message |
| Empty input | Rejected (caught by ValueError) |

*DecodeLabs Internship | Batch 2026*

# Enterprise Random Password Generator

**Project 3 | DecodeLabs Internship | Batch 2026**

---

## Overview

A command-line tool that generates cryptographically secure passwords using Python's `secrets` module. The program follows NIST SP 800-63-4 password security guidelines and implements the Input-Process-Output (IPO) architectural model. After generating a password, it displays a full security analysis including entropy in bits and estimated brute-force crack time.

---

## Features

- Cryptographically secure password generation via the `secrets` module
- Input validation with NIST-based security advisories
- Information entropy calculation using `entropy = length * log2(pool_size)`
- Brute-force crack time estimation at 1 billion guesses per second
- Password regeneration loop with clean exit
- No external dependencies - standard library only

---

## Architecture

The program follows a strict three-phase IPO model:

| Phase | Function | Responsibility |
|-------|----------|----------------|
| Input | `get_password_length()` | Validate user-provided password length |
| Process | `generate_password(length)` | Generate password using CSPRNG |
| Output | `main()` | Display password and security metrics |

---

## How It Works

1. The user enters a desired password length (positive integer)
2. The program validates the input and warns if below NIST minimums
3. A password is generated from a 62-character pool (a-z, A-Z, 0-9)
4. Security statistics are computed and displayed

---

## Security

- Uses `secrets.choice()` - backed by the OS cryptographic random number generator
- Character pool: 62 characters (`string.ascii_letters` + `string.digits`)
- At length 12: entropy exceeds 71 bits (above NIST 64-bit minimum for moderate security)
- At length 16: entropy exceeds 95 bits

---

## Requirements

- Python 3.6 or higher
- No external packages required

All modules used (`secrets`, `string`, `math`, `sys`) are part of the Python standard library.

---

## Usage

```bash
python Python_Task_3.py
```

**Sample interaction:**

```
Enter desired password length (positive integer): 16

----------------------------------------
GENERATED PASSWORD:
aB3rTz9mKd2xLpQ7
----------------------------------------
Password Length: 16 characters
Character Pool Size: 62
Total Possibilities: 47,672,401,706,823,533,450,263,330,816
Information Entropy: 95.27 bits
Estimated Crack Time (1B guesses/sec): 1.51e+18 years
----------------------------------------

Generate another password? (y/n):
```

---

## File Structure

```
Project3/
├── Python_Task_3.py       # Main program file
├── README.md              # This file
└── Project3_Documentation.docx   # Full technical documentation
```

---

## Functions

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `get_password_length()` | None | `int` | Validates and returns password length |
| `calculate_entropy(pool_size, length)` | `int, int` | `float` | Calculates entropy in bits |
| `estimate_crack_time(entropy_bits, guesses_per_second)` | `float, float` | `str` | Human-readable crack time |
| `generate_password(length)` | `int` | `tuple` | Returns (password, pool) |
| `main()` | None | None | Orchestrates all phases |

---

*DecodeLabs Internship | Batch 2026*
