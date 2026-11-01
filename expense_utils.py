import random
import math


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return None

        return amount

    except ValueError:
        return None


def generate_reference(existing_ids):
    while True:
        ref_id = f"EXP-{random.randint(100000, 999999)}"

        if ref_id not in existing_ids:
            return ref_id


def calculate_total(expenses):
    total = math.fsum(
        expense["amount"] for expense in expenses
    )

    return round(total, 2)


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]

        summary[category] = (
            summary.get(category, 0) + expense["amount"]
        )

    return {
        category: round(amount, 2)
        for category, amount in summary.items()
    }