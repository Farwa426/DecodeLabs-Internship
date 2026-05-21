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
