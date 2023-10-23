from datetime import date
from typing import Optional
from recurrence import Recurrence

class Task:
    def __init__(self, name: str, description: str, deadline: date, recurrence: Optional[Recurrence] = None):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False
        self.recurrence = recurrence

    def mark_as_completed_or_update_deadline(self):
        # if task have recurrence than update deadline if not complete
        next_deadline = self.__next_deadline()
        if next_deadline:
            self.deadline = next_deadline
        else:
            self.completed = True

    def __str__(self) -> str:
        status = "Completed" if self.completed else "Not Completed"
        recurrence_info = str(self.recurrence) if self.recurrence else "No Recurrence"
        return f"<Task {self.name}({self.description}) | {status} | {recurrence_info} | {self.deadline.strftime('%Y-%m-%d')}>"

    def __next_deadline(self) -> Optional[date]:
        if self.recurrence:
            return self.recurrence.next_occurrence(self.deadline)
        else:
            return None