import json
from datetime import datetime

expenses = []

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Invalid amount. Please enter a number.")
    category = input("Enter category: ")
    description = input("Enter description: ")
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        for expense in expenses:
            print(expense)

def delete_expense():
    if len(expenses) == 0:
        print("No expenses found")
        return

    for expense in expenses:
        print(expense)

    while True:
        try:
            delete_id = int(input("Enter expense number to delete: "))

            if delete_id >= 1 and delete_id <= len(expenses):
                expenses.pop(delete_id - 1)
                save_expenses()
                print("Expense deleted successfully!")
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

def show_total():
    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print("Total spending:", total)

def filter_by_category():
    category_name = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category_name.lower():
            print(expense)
            found = True

    if found == False:
        print("No expenses found for this category")

def filter_by_month():
    month = input("Enter month (YYYY-MM): ")

    found = False

    for expense in expenses:
        if expense["date"].startswith(month):
            print(expense)
            found = True

    if found == False:
        print("No expenses found for this month")

load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total")
    print("5. Filter by Category")
    print("6. Filter by Month")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        show_total()

    elif choice == "5":
        filter_by_category()

    elif choice == "6":
        filter_by_month()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")