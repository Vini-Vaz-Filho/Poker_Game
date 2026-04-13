# Budget Tracker Application
# Meets requirements: loops, data types, lists, tuples, dictionaries,
# functions, exceptions, OOP

import json
from datetime import datetime

# ---------------------- OOP CLASSES ----------------------

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

class BudgetTracker:
    def __init__(self):
        self.expenses = []  # list

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, exp in enumerate(self.expenses):
            print(f"{i+1}. ${exp.amount} | {exp.category} | {exp.description} | {exp.date}")

    def delete_expense(self, index):
        try:
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed.description}")
        except IndexError:
            print("Invalid index.")

    def total_spent(self):
        total = 0
        for exp in self.expenses:
            total += exp.amount
        print(f"Total spent: ${total}")

    def category_summary(self):
        summary = {}  # dictionary
        for exp in self.expenses:
            if exp.category in summary:
                summary[exp.category] += exp.amount
            else:
                summary[exp.category] = exp.amount

        for cat, amt in summary.items():
            print(f"{cat}: ${amt}")

    def save_to_file(self, filename="expenses.json"):
        data = [exp.to_dict() for exp in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Data saved.")

    def load_from_file(self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.expenses = []
                for item in data:
                    exp = Expense(item["amount"], item["category"], item["description"], item["date"])
                    self.expenses.append(exp)
            print("Data loaded.")
        except FileNotFoundError:
            print("No saved data found.")

# ---------------------- FUNCTIONS ----------------------

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")


def get_string_input(prompt):
    value = input(prompt)
    return value.strip()


def main_menu():
    print("\n--- Budget Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spent")
    print("5. Category Summary")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

# ---------------------- MAIN PROGRAM ----------------------

def main():
    tracker = BudgetTracker()

    while True:  # loop
        main_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            amount = get_float_input("Enter amount: ")
            category = get_string_input("Enter category: ")
            description = get_string_input("Enter description: ")
            date = datetime.now().strftime("%Y-%m-%d")

            expense = Expense(amount, category, description, date)
            tracker.add_expense(expense)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            try:
                index = int(input("Enter expense number to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            tracker.total_spent()

        elif choice == "5":
            tracker.category_summary()

        elif choice == "6":
            tracker.save_to_file()

        elif choice == "7":
            tracker.load_from_file()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# ---------------------- EXTRA FEATURES ----------------------

def sample_data(tracker):
    sample = [
        (10.5, "Food", "Lunch"),
        (25.0, "Transport", "Gas"),
        (15.75, "Entertainment", "Movie"),
    ]

    for amount, category, desc in sample:  # tuple usage
        tracker.add_expense(Expense(amount, category, desc, datetime.now().strftime("%Y-%m-%d")))


if __name__ == "__main__":
    main()
