from enum import Enum
from datetime import date, timedelta
from typing import Optional


class RecurrenceType(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

class Recurrence:
    DEFAULT_INTERVAL = 1  # Default interval for recurrences

    def __init__(self, recurrence_type: RecurrenceType, interval: int = DEFAULT_INTERVAL):
        if not isinstance(recurrence_type, RecurrenceType):
            raise ValueError("recurrence_type must be a valid RecurrenceType")
        self.recurrence_type = recurrence_type
        self.interval = interval  # Number of units for the recurrence (default is 1)

    def __str__(self):
        if self.interval == 1:
            return f"Recurrence: {self.recurrence_type.value}"
        else:
            return f"Recurrence: {self.interval} {self.recurrence_type.value}(s)"

    def next_occurrence(self, last_occurrence: date) -> Optional[date]:
        if self.recurrence_type == RecurrenceType.DAILY:
            new_date = last_occurrence + timedelta(days=self.interval)
        elif self.recurrence_type == RecurrenceType.WEEKLY:
            new_date = last_occurrence + timedelta(weeks=self.interval)
        elif self.recurrence_type == RecurrenceType.MONTHLY:
            new_date = self.add_months(last_occurrence, self.interval)
        elif self.recurrence_type == RecurrenceType.YEARLY:
            new_date = last_occurrence.replace(year=last_occurrence.year + self.interval)
        else:
            return None

        return new_date

    @staticmethod
    def add_months(source_date, months):
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day, [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month])
        return source_date.replace(year=year, month=month, day=day)