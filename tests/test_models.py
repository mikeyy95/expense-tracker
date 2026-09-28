# tests/test_models.py

from cmath import exp

import pytest
from datetime import date, timedelta
from expense_tracker.models import Expense, Category


def test_valid_expense_creates_successfully():
    e = Expense(amount=50.0, category=Category.FOOD, description="Groceries")
    assert e.amount == 50.0
    assert e.category == Category.FOOD
    assert e.description == "Groceries"


def test_negative_amount_raises_value_error():
    with pytest.raises(ValueError):
        Expense(amount=-10, category=Category.FOOD, description="Bad")


def test_empty_description_raises_value_error():
    with pytest.raises(ValueError):
        Expense(amount=20, category=Category.FOOD, description="   ")


def test_future_date_raises_value_error():
    tomorrow = date.today() + timedelta(days=1)
    with pytest.raises(ValueError):
        Expense(amount=20, category=Category.FOOD, description="Test", date_incurred=tomorrow)

def test_is_recent_with_custom_window():
    days_ago = date.today() - timedelta(days=60)
    expense = Expense(amount=20, category=Category.FOOD, description="Test", date_incurred=days_ago)
    assert expense.is_recent(30) is False
    assert expense.is_recent(90) is True