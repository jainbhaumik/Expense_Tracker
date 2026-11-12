# 💸 Expense Tracker

A simple command-line app to track daily spending, built with Python.
Made as a learning project to practice file handling, functions, and data
processing.

## Features

- Add expenses with amount, category, and a note
- View all expenses in a neat table
- Delete wrong entries
- Monthly summary grouped by category
- Bar chart of spending (matplotlib)
- Export everything to CSV (opens in Excel)
- Data is saved automatically in `expenses.json`

## Project Structure

```
expense-tracker/
├── main.py            # menu and user input
├── tracker.py         # all the logic (add, delete, totals, chart, export)
├── requirements.txt   # libraries needed
├── .gitignore         # keeps personal data off GitHub
├── LICENSE            # MIT license
└── README.md
```

## How to Run

1. Install Python 3.8 or newer.
2. Clone the repo:
   ```bash
   git clone https://github.com/jainbhaumik/expense-tracker.git
   cd expense-tracker
   ```
3. Install the chart library (only needed for the chart option):
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python main.py
   ```

## Example

```
===== EXPENSE TRACKER =====
1. Add expense
2. View all expenses
...
Choose (1-7): 1
Amount: 250
Categories:
  1. Food
  ...
Pick a category number: 1
Note (optional): lunch with friends
Saved! (id 1)
```

## What I Learned

- Reading and writing JSON files
- Splitting code into modules (`main.py` + `tracker.py`)
- Handling bad user input with `try/except`
- Using dictionaries to group data
- Plotting with matplotlib

## Future Ideas

- Monthly budget limit with warnings
- Search expenses by note
- A GUI version with Tkinter
- Predict next month's spending with scikit-learn

## License

MIT, see the `LICENSE` file.
