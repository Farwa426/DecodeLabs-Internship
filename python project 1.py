"""
PROJECT 1: TO-DO LIST APPLICATION
=================================
Intern Name: [Farwa]
Batch: 2026
Company: DecodeLabs

Description:
------------
This program implements a basic To-Do List system as specified in Project 1.
It demonstrates the IPO Model (Input-Process-Output) using Python lists.

Requirements Met:
-----------------
✅ Add tasks using append() method
✅ View tasks using for loop
✅ Store multiple items in a single variable (list)
✅ Clean menu-driven interface

References from Training Material:
----------------------------------
- Page 4: Lists (append & print loops)
- Page 6: IPO Model
- Page 7: Memory Container
- Page 10: Display/Read Operation
"""

# ============================================
# DATA STORAGE (The Memory Container - Page 7)
# ============================================
my_tasks = []  # Empty list - data will live in dynamic memory

# ============================================
# FUNCTION DEFINITIONS
# ============================================

def display_welcome():
    """Display welcome banner and program information"""
    print("\n" + "="*55)
    print("      DecodeLabs TO-DO LIST SYSTEM")
    print("     Batch 2026 | Industrial Training")
    print("="*55)
    print("System Ready: In-Memory Database Active")
    print("="*55)

def show_menu():
    """Display available options to user"""
    print("\n" + "-"*35)
    print("   MAIN MENU")
    print("-"*35)
    print("   1.   Add a new task")
    print("   2.   View all tasks")
    print("   3.   Exit")
    print("-"*35)

def add_task():
    """
    INPUT PHASE: Get data from user
    PROCESS PHASE: Store data in list using append()
    """
    task = input("\n  Enter your task: ").strip()
    
    # Check if user entered something meaningful
    if task:
        my_tasks.append(task)  # Key Operation 1: append()
        print(f"\n Task added successfully!")
        print(f" Your task list now contains {len(my_tasks)} item(s)")
    else:
        print("\n  Cannot add empty task! Please enter valid text.")

def view_tasks():
    """
    OUTPUT PHASE: Display data to user
    Uses for loop to iterate through the list (Page 4 & 10)
    """
    print("\n" + "="*45)
    print("           YOUR TASK LIST")
    print("="*45)
    
    # Check if list is empty
    if len(my_tasks) == 0:
        print("     No tasks found! Your to-do list is empty.")
        print("     Use option 1 to add your first task.")
    else:
        # Key Operation 2: for loop - Iterates through list
        # This creates a temporary view of system's state (Page 10)
        print("   Current Tasks:")
        print("-"*35)
        for task in my_tasks:
            print(f"   •  {task}")
        print("-"*35)
        print(f"     Total tasks: {len(my_tasks)}")
    
    print("="*45)

def main():
    """
    MAIN PROGRAM LOOP
    Implements IPO Model: Input → Process → Output (Page 6)
    """
    display_welcome()
    
    while True:
        show_menu()
        choice = input("\n  Enter your choice (1-3): ")
        
        # PROCESS PHASE: Handle user input
        if choice == '1':
            add_task()      # INPUT + PROCESS
            
        elif choice == '2':
            view_tasks()    # OUTPUT
            
        elif choice == '3':
            # Exit the program
            print("\n" + "="*45)
            print("    SESSION SUMMARY")
            print("="*45)
            print(f"   Total tasks created: {len(my_tasks)}")
            print("   Status: All data was stored in volatile memory")
            print("   Note: Data will not persist after program ends")
            print("="*45)
            print("\n  Thank you for using DecodeLabs To-Do List!")
            print("    Your journey to becoming a Python developer continues!")
            print("    Exiting system... Goodbye! 👨‍💻")
            break
            
        else:
            print("\n  Invalid choice! Please enter 1, 2, or 3.")

# ============================================
# PROGRAM ENTRY POINT
# ============================================
if __name__ == "__main__":
    main()