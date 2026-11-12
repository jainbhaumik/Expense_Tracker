"""
main.py
Run this file to start the Expense Tracker:
    python main.py
"""

from datetime import datetime

import tracker


def print_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete an expense")
    print("4. Summary by category")
    print("5. Show chart")
    print("6. Export to CSV")
    print("7. Exit")


def ask_amount():
    """Keep asking until the user types a valid positive number."""
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be more than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a number, like 250 or 99.5")


def ask_category():
    """Show the category list and let the user pick by number."""
    print("Categories:")
    for i, cat in enumerate(tracker.CATEGORIES, start=1):
        print(f"  {i}. {cat}")

    while True:
        choice = input("Pick a category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(tracker.CATEGORIES):
            return tracker.CATEGORIES[int(choice) - 1]
        print("Invalid choice, try again.")


def handle_add(expenses):
    amount = ask_amount()
    category = ask_category()
    note = input("Note (optional): ").strip()
    expense = tracker.add_expense(expenses, amount, category, note)
    tracker.save_expenses(expenses)
    print(f"Saved! (id {expense['id']})")


def handle_view(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print(f"\n{'ID':<4} {'Date':<12} {'Amount':>9}  {'Category':<14} Note")
    print("-" * 55)
    for e in expenses:
        print(
            f"{e['id']:<4} {e['date']:<12} {e['amount']:>9.2f}  "
            f"{e['category']:<14} {e['note']}"
        )
    total = sum(e["amount"] for e in expenses)
    print("-" * 55)
    print(f"Total spent: Rs {total:.2f}")


def handle_delete(expenses):
    handle_view(expenses)
    if not expenses:
        return
    choice = input("Enter id to delete: ")
    if not choice.isdigit():
        print("That is not a valid id.")
        return
    if tracker.delete_expense(expenses, int(choice)):
        tracker.save_expenses(expenses)
        print("Deleted.")
    else:
        print("No expense with that id.")


def handle_summary(expenses):
    # default to the current month, or type 'all' for everything
    this_month = datetime.now().strftime("%Y-%m")
    month = input(f"Month (YYYY-MM) [{this_month}], or 'all': ").strip()
    if month == "":
        month = this_month

    data = expenses if month == "all" else tracker.filter_by_month(expenses, month)
    totals = tracker.total_by_category(data)

    if not totals:
        print("No expenses found for that period.")
        return

    print(f"\nSummary for {month}")
    for cat, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<14} Rs {amount:.2f}")
    print(f"  {'TOTAL':<14} Rs {sum(totals.values()):.2f}")


def main():
    expenses = tracker.load_expenses()

    while True:
        print_menu()
        choice = input("Choose (1-7): ").strip()

        if choice == "1":
            handle_add(expenses)
        elif choice == "2":
            handle_view(expenses)
        elif choice == "3":
            handle_delete(expenses)
        elif choice == "4":
            handle_summary(expenses)
        elif choice == "5":
            tracker.show_chart(tracker.total_by_category(expenses))
        elif choice == "6":
            filename = tracker.export_to_csv(expenses)
            print(f"Exported to {filename}")
        elif choice == "7":
            print("Bye! Keep saving money.")
            break
        else:
            print("Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
