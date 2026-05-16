"""
Project 2: Expense Tracker
Batch: 2026 | DecodeLabs
Theme: Data Accumulation | IPO Model | Sentinel Kill Switch
"""

# ===============================
# PHASE 1: THE GATEKEEPER
# Defensive input handling
# ===============================

def get_valid_expense():
    """
    Get and validate expense input from user.
    Converts string to integer/float safely (avoiding '100' + '50' = '10050' disaster)
    """
    while True:
        user_input = input("Enter expense amount (or 'done' to finish): ")

        # SENTINEL VALUE (Kill Switch)
        if user_input.lower() == 'done':
            return None

        # Defensive coding: try converting to number
        try:
            # Convert to float to handle decimals
            amount = float(user_input)
            if amount < 0:
                print("Invalid input! Expense cannot be negative. Please enter a valid amount.")
                continue
            return amount
        except ValueError:
            print("Invalid input! Please enter a number (e.g., 100, 50.75) or 'done'.")

# ===============================
# PHASE 2: THE ACCUMULATOR PATTERN
# total = total + new_expense
# ===============================

def run_expense_tracker():
    """
    Main function implementing the accumulator pattern.
    Continuously adds expenses and maintains state.
    """
    print("\n" + "=" * 50)
    print("   DECODELABS EXPENSE TRACKER (Project 2)")
    print("   Enter expenses one by one. Type 'done' to finish.")
    print("=" * 50 + "\n")

    total_expenses = 0.0      # THE ACCUMULATOR (initial state)
    expense_count = 0
    expenses_list = []        # For detailed audit trail

    # Continuous audit loop
    while True:
        expense = get_valid_expense()

        # KILL SWITCH triggered
        if expense is None:
            break

        # THE ACCUMULATOR PATTERN (core logic)
        total_expenses = total_expenses + expense
        expense_count += 1
        expenses_list.append(expense)

        # Real-time feedback
        print(f"   Added: ${expense:.2f} | Total so far: ${total_expenses:.2f}\n")

    # ===============================
    # PHASE 3: OUTPUT (Model-View separation)
    # ===============================
    display_summary(total_expenses, expense_count, expenses_list)


def display_summary(total, count, expenses):
    """
    PHASE 3: OUTPUT
    Decoupling logic (Model) from display (View)
    """
    print("\n" + "=" * 50)
    print("           FINAL EXPENSE REPORT")
    print("=" * 50)

    if count == 0:
        print("No expenses were recorded.")
    else:
        print(f"Total number of expenses: {count}")
        print(f"TOTAL SPENT: ${total:.2f}")

        # Optional: Show individual entries (audit trail)
        print("\nExpense breakdown:")
        for idx, amount in enumerate(expenses, 1):
            print(f"   {idx}. ${amount:.2f}")

        # Calculate average (bonus: shows accumulator pattern usefulness)
        average = total / count
        print(f"\nAverage expense: ${average:.2f}")

    print("=" * 50)
    print("Transaction complete.")
    print("=" * 50)


# ===============================
# ENTRY POINT (IPO Model)
# ===============================

if __name__ == "__main__":
    run_expense_tracker()