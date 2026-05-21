"""
DecodeLabs Industrial Training Kit - Batch 2026
Project 1: To-Do List
Author: [Your Name]
Description: A command-line To-Do List application demonstrating
             Python list operations, dictionary-based data modeling,
             and the IPO (Input-Process-Output) architecture pattern.
"""

import json
import os


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file for persistence across sessions."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file (RAM to Disk serialization)."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks, task_description):
    """
    Add a new task to the list using a dictionary to model a database row.
    Dictionary  -> Table Row
    'id' key    -> Primary Key
    append()    -> INSERT INTO (SQL equivalent)
    """
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "task": task_description,
        "status": "pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask added successfully: [{task_id}] {task_description}")


def view_tasks(tasks):
    """
    Display all tasks using enumerate() for professional Pythonic indexing.
    Iteration creates a temporary view of the system state (Read Operation).
    """
    if not tasks:
        print("\nNo tasks found. Start by adding a task.")
        return

    print("\n" + "=" * 45)
    print("         YOUR TO-DO LIST")
    print("=" * 45)
    for index, task in enumerate(tasks, start=1):
        status_marker = "[x]" if task["status"] == "done" else "[ ]"
        print(f"  {index}. {status_marker} {task['task']}")
    print("=" * 45)
    print(f"  Total tasks: {len(tasks)}")
    print("=" * 45)


def mark_done(tasks, task_number):
    """Mark a task as completed by its display number."""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "done"
        save_tasks(tasks)
        print(f"\nTask {task_number} marked as done.")
    else:
        print("\nInvalid task number. Please try again.")


def delete_task(tasks, task_number):
    """Remove a task from the list by its display number."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        for index, task in enumerate(tasks, start=1):
            task["id"] = index
        save_tasks(tasks)
        print(f"\nTask deleted: {removed['task']}")
    else:
        print("\nInvalid task number. Please try again.")


def show_menu():
    """Display the main application menu."""
    print("\n" + "-" * 45)
    print("  DecodeLabs To-Do List - Project 1")
    print("-" * 45)
    print("  1. Add a new task")
    print("  2. View all tasks")
    print("  3. Mark a task as done")
    print("  4. Delete a task")
    print("  5. Exit")
    print("-" * 45)


def main():
    """
    Main application entry point.
    Follows the IPO model:
      - Input  : User enters tasks and choices
      - Process: List operations (append, enumerate, pop)
      - Output : Formatted task display
    """
    print("\nWelcome to DecodeLabs To-Do List Manager")
    print("Project 1 - Industrial Training Kit, Batch 2026")

    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            description = input("\n  Enter task description: ").strip()
            if description:
                add_task(tasks, description)
            else:
                print("\n  Task description cannot be empty.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    num = int(input("\n  Enter task number to mark done: "))
                    mark_done(tasks, num)
                except ValueError:
                    print("\n  Please enter a valid number.")

        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                try:
                    num = int(input("\n  Enter task number to delete: "))
                    delete_task(tasks, num)
                except ValueError:
                    print("\n  Please enter a valid number.")

        elif choice == "5":
            print("\nExiting. Your tasks have been saved. Goodbye.\n")
            break

        else:
            print("\n  Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
