import os
import datetime as dt


def build_monthly_report(expenses):
    current_month = dt.date.today().strftime("%Y-%m")

    monthly_expenses = [
        expense for expense in expenses
        if expense["date"].startswith(current_month)
    ]

    return monthly_expenses


def save_report(report_text):
    folder = "reports"

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(
        folder,
        f"report_{dt.date.today().strftime('%Y_%m')}.txt"
    )

    if os.path.exists(file_path):
        print("Existing report will be updated.")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    print("Report saved at:", file_path)