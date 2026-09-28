# expense_tracker/models.py

from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum


class Category(str, Enum):
    """Fixed set of valid expense categories — prevents typo garbage."""
    FOOD = "Food"
    TRANSPORT = "Transport"
    UTILITIES = "Utilities"
    ENTERTAINMENT = "Entertainment"
    OTHER = "Other"


@dataclass
class Expense:
    amount: float
    category: Category
    description: str
    date_incurred: date = field(default_factory=date.today)

    def __post_init__(self):
        if self.date_incurred > date.today():
            raise ValueError("Date incurred cannot be in the future")
        if self.amount <= 0:
            raise ValueError("Expense amount must be positive")
        if not isinstance(self.category, Category):
            raise ValueError(f"Invalid category: {self.category}")
        if not self.description.strip():
            raise ValueError("Description cannot be empty")

    def __str__(self) -> str:
        return f"[{self.date_incurred}] {self.category.value}: ${self.amount:.2f} - {self.description}"

    def is_recent(self, days) -> bool:
        return self.date_incurred >= date.today() - timedelta(days=days)