import datetime as dt
import expense_utils as eu

from report_utils import build_monthly_report, save_report
from tabulate import tabulate


expenses = []

print("\n===== PERSONAL EXPENSE TRACKER =====")

while True:

    print("\nEnter Expense Details")

    description = input("Enter description: ")

    category = input("Enter category: ")

    amount = eu.validate_amount(
        input("Enter amount: ")
    )

    if amount is None:
        print("Invalid amount! Enter a positive number.")
        continue

    date_input = input(
        "Enter date (YYYY-MM-DD, blank for today): "
    )

    if date_input.strip() == "":
        expense_date = dt.date.today()
    else:
        try:
            expense_date = dt.date.fromisoformat(date_input)
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD.")
            continue

    existing_ids = [
        expense["reference"]
        for expense in expenses
    ]

    reference = eu.generate_reference(existing_ids)

    expense = {
        "reference": reference,
        "date": expense_date.isoformat(),
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("\nExpense added successfully!")
    print("Reference ID:", reference)

    choice = input("\nAdd another expense? (yes/no): ")

    if choice.lower() != "yes":
        break



monthly_expenses = build_monthly_report(expenses)

print("\n===== MONTHLY EXPENSE REPORT =====")

if monthly_expenses:

    table_data = [
        [
            e["reference"],
            e["date"],
            e["description"],
            e["category"],
            e["amount"]
        ]
        for e in monthly_expenses
    ]

    print(tabulate(
        table_data,
        headers=[
            "Reference ID",
            "Date",
            "Description",
            "Category",
            "Amount"
        ],
        tablefmt="grid"
    ))

    total = eu.calculate_total(monthly_expenses)

    print("\nTotal Spending: Rs.", total)

    summary = eu.category_summary(monthly_expenses)

    print("\nCategory-wise Expenses:")

    for category, amount in summary.items():
        print(category, ":", amount)

    print(
        "\nReport Month:",
        dt.date.today().strftime("%B %Y")
    )

    report_text = "MONTHLY EXPENSE REPORT\n\n"

    report_text += tabulate(
        table_data,
        headers=[
            "Reference ID",
            "Date",
            "Description",
            "Category",
            "Amount"
        ],
        tablefmt="grid"
    )

    report_text += f"\n\nTotal Spending: Rs. {total}\n"

    for category, amount in summary.items():
        report_text += f"{category}: Rs. {amount}\n"

    choice = input("\nSave report to file? (yes/no): ")

    if choice.lower() == "yes":
        save_report(report_text)

else:
    print("No expenses found for the current month.")

print("\nThank you for using Expense Tracker!")