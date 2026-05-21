# To-Do List - Python Project 1

> **DecodeLabs Industrial Training Kit | Batch 2026**

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python)
![Build Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

---

## Project Overview

This is Project 1 of the DecodeLabs Python Industrial Training Program. The project demonstrates core data management concepts by building a command-line To-Do List application. The focus is on mastering Python lists and dictionaries as the foundation of all database systems.

---

## Objectives

* **Build** a program where users can add and view tasks through programmatic logic.
* **Master** Python list operations: `append()` and iteration with `enumerate()`.
* **Understand** the IPO model: Input, Process, Output.
* **Model** data using dictionaries (equivalent to a database table row).
* **Implement** data persistence using JSON file serialization.

---

## Key Concepts Covered

* **Python Lists** as dynamic arrays stored in heap memory.
* **Dictionary** as an in-memory database row (`id`, `task`, `status`).
* **`list.append()`** as the equivalent of `INSERT INTO` in SQL.
* **`enumerate()`** for Pythonic indexed iteration.
* **JSON serialization** to persist data from volatile RAM to disk.
* **IPO architecture**: separating data logic from user interface.

---

## Features

* Add a new task with a description.
* View all tasks with status indicators (pending or done).
* Mark a task as completed.
* Delete a task.
* Auto-save to a JSON file for persistence across sessions.

---

## Project Structure

```text
project-1-todo-list/
    ├── todo_list.py       # Main application file
    ├── tasks.json         # Auto-generated data file (created on first run)
    └── README.md          # Project documentation


# Expense Tracker - Python Project 2

> **DecodeLabs Industrial Training Kit | Batch 2026**

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&logo=python)
![Build Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

---

## Table of Contents

* [Project Overview](#project-overview)
* [Objectives](#objectives)
* [Key Concepts Covered](#key-concepts-covered)
* [Features](#features)
* [Project Structure](#project-structure)
* [Requirements](#requirements)
* [How to Run](#how-to-run)
* [Architecture](#architecture)
* [Author](#author)
* [License](#license)

---

## Project Overview

This is Project 2 of the DecodeLabs Python Industrial Training Program. The command-line Expense Tracker is designed to demonstrate core programming logic including data accumulation, strict user input validation, and program flow control. 

---

## Objectives

* **Implement** the Accumulator Pattern to keep a running total of numerical data.
* **Control** program execution flow using a Sentinel Value (Kill Switch).
* **Handle** user input defensively to prevent program crashes from unexpected data.
* **Decouple** application logic (Model) from presentation (View) to maintain clean code architecture.

---

## Key Concepts Covered

* **Defensive Programming:** Using `try-except` blocks to safely handle `ValueError` exceptions when converting strings to floats.
* **Accumulator Pattern:** Continuously updating state variables (`total = total + new_expense`) inside a loop.
* **Sentinel Values:** Using specific keywords (e.g., 'done') to safely exit an infinite `while True` loop.
* **Type Conversion:** Managing data types appropriately to handle decimal amounts effectively.
* **List Appending:** Building an audit trail memory by pushing inputs to a dynamic list.

---

## Features

* Continuously add expenses with real-time feedback on the running total.
* Strict input validation that rejects negative numbers, text strings, and empty inputs without crashing the program.
* Detailed final audit report displaying total spent, number of transactions, and the calculated average expense.
* Itemized breakdown showing every individual expense entered during the session.

---

## Project Structure

```text
project-2-expense-tracker/
    ├── expense_tracker.py       # Main application file
    └── README.md                # Project documentation
