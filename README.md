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

Name: Farwa 
Internship Program: DecodeLabs Industrial Training Kit  
Batch: 2026  
Contact: decodelabs.tech@gmail.com  
Website: www.decodelabs.tech

---

## License

This project is submitted as part of the DecodeLabs Internship Program. All rights reserved by the respective author.

# Expense Tracker - Python Project 2

**DecodeLabs | Batch 2026**

---

## Project Overview

A simple command-line expense tracker built in Python. This project demonstrates core programming logic, including the Accumulator Pattern, strict user input validation, and program flow control using a Sentinel Value.

## Features

* Add expenses continuously with real-time feedback on the running total.
* Defensive input validation that safely rejects negative numbers and text strings without crashing the program.
* A final summary report displaying the total amount spent, total number of transactions, and the average expense.
* An itemized breakdown of all individual expenses entered during the session.

## Requirements

* Python 3.6 or higher
* No external libraries required (uses standard built-in Python features).

## How to Run

1. Clone this repository to your local machine.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the Python script:

```bash
python "Python Project 2.py"

# Enterprise Random Password Generator

## Project 3 - DecodeLabs Python Internship (Batch 2026)

A cryptographically secure password generator that follows NIST SP 800-63-4 guidelines and implements the Input-Process-Output architectural scaffold. Built with Python's `secrets` and `string` modules for enterprise-grade security.

## Features

- Cryptographically secure randomness using `secrets.choice()` (not `random`)
- Character pool: ASCII letters (A-Z, a-z) + digits (0-9) – 62 characters total
- Input validation with NIST length advisory
- Information entropy calculation (bits)
- Brute-force crack time estimation (1 billion guesses/second)
- Memory-efficient generation using `list` + `''.join()` (O(n) time complexity)
- Interactive regeneration loop

## Requirements

- Python 3.6 or higher (for `secrets` module)
- No external dependencies – uses only Python standard library

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/random-password-generator.git

# Navigate into the directory
cd random-password-generator

# (Optional) Make the script executable on Linux/macOS
chmod +x password_generator.py
