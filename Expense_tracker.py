import os
import csv

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.fields = ['Date', 'Category', 'Amount', 'Description']
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()

    def add_expense(self, date, category, amount, description):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writerow({'Date': date, 'Category': category, 'Amount': amount, 'Description': description})
        print("Expense added successfully!")

    def view_expenses(self):
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    def delete_expense(self, description):
        rows = []
        deleted = False
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['Description'] != description]

        if len(rows) < self.get_total_records():
            deleted = True
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fields)
                writer.writeheader()
                writer.writerows(rows)
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    def get_total_records(self):
        with open(self.filename, mode='r') as file:
            return sum(1 for _ in file) - 1


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter Date (YYYY-MM-DD): ")
            category = input("Enter Category (e.g., Food, Transport, Bills): ")
            amount = input("Enter Amount: ")
            description = input("Enter Description: ")
            tracker.add_expense(date, category, amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            description = input("Enter the Description of the Expense to Delete: ")
            tracker.delete_expense(description)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
