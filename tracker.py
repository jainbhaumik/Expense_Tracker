"""
tracker.py
All the logic for the expense tracker lives here.
main.py only handles the menu and user input.
"""

import csv
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

CATEGORIES = ["Food", "Travel", "Books", "Entertainment", "Rent", "Other"]


def load_expenses():
    """Read expenses from the JSON file. Returns an empty list if no file yet."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # file is empty or broken, so start fresh instead of crashing
        print("Warning: data file was corrupted. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Write the whole expense list back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses, amount, category, note):
    """Create a new expense dict and add it to the list."""
    # give each expense a unique id (last id + 1)
    new_id = expenses[-1]["id"] + 1 if expenses else 1

    expense = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "note": note,
    }
    expenses.append(expense)
    return expense


def delete_expense(expenses, expense_id):
    """Remove an expense by id. Returns True if found, False otherwise."""
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            return True
    return False


def filter_by_month(expenses, month):
    """Keep only expenses from a month like '2026-11'."""
    return [e for e in expenses if e["date"].startswith(month)]


def total_by_category(expenses):
    """Returns a dict like {'Food': 450.0, 'Travel': 120.0}."""
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals


def export_to_csv(expenses, filename="expenses_export.csv"):
    """Save all expenses to a CSV file that Excel can open."""
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "date", "amount", "category", "note"]
        )
        writer.writeheader()
        writer.writerows(expenses)
    return filename


def show_chart(totals):
    """Draw a bar chart of spending per category (needs matplotlib)."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib is not installed.")
        print("Run: python -m pip install matplotlib")
        return

    if not totals:
        print("Nothing to plot yet.")
        return

    plt.bar(list(totals.keys()), list(totals.values()), color="teal")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs)")
    plt.tight_layout()
    plt.show()
