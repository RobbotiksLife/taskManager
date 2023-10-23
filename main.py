from recurrence import Recurrence, RecurrenceType
from datetime import date
from task import Task
import pickle

def create_task():
    name = input("Task name: ")
    description = input("Task description: ")
    deadline = input("Task deadline (YYYY-MM-DD): ")

    print("Define recurrence type:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")
    print("5. None")
    recurrence_mapping_choice = input("Enter the number for recurrence type: ")
    recurrence_mapping = {
        "1": RecurrenceType.DAILY,
        "2": RecurrenceType.WEEKLY,
        "3": RecurrenceType.MONTHLY,
        "4": RecurrenceType.YEARLY,
        "5": None,
    }
    # Get the recurrence_type based on the user's input or default to 'None'
    recurrence_type = recurrence_mapping.get(recurrence_mapping_choice, None)
    if recurrence_mapping_choice != "5" and recurrence_type is None:
        print("Invalid choice for recurrence type. Defaulting to 'None'.")

    # Create a Recurrence object if recurrence is specified
    if recurrence_type:
        interval = int(input("Recurrence interval (default is 1): "))
        recurrence = Recurrence(recurrence_type, interval)
    else:
        recurrence = None

    task = Task(name, description, date.fromisoformat(deadline), recurrence)
    tasks.append(task)
    save_tasks_to_file(tasks, tasksFilePath)

    print("Task created successfully!")

def display_tasks(tasks_defined: [Task]):
    for i, task in enumerate(tasks_defined, start=1):
        print(f"Task {i}: {task}")

def mark_task_completed_or_update_deadline():
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_as_completed_or_update_deadline()
        save_tasks_to_file(tasks, tasksFilePath)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def save_tasks_to_file(tasks, file_name):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(tasks, file)
        print(f'Tasks saved to {file_name}')
    except Exception as e:
        print(f'Error: {e}')

def load_tasks_from_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            tasks = pickle.load(file)
        return tasks
    except Exception as e:
        print(f'Error: {e}')
        return []

def sort_tasks_by_deadline(tasks):
    return sorted(tasks, key=lambda task: task.deadline)

# Example usage:
if __name__ == "__main__":
    # TODO: Uncoment and save file when submiting th code
    # tasks = load_tasks_from_file(tasksFilePath)
    tasks: [Task] = [
        Task("Task 1", "Task 1 Description", date(2024, 7, 5), Recurrence(RecurrenceType.WEEKLY)),
        Task("Task 2", "Task 2 Description", date(2024, 7, 13), Recurrence(RecurrenceType.DAILY)),
        Task("Task 3", "Task 3 Description", date(2024, 7, 22), Recurrence(RecurrenceType.DAILY)),
        Task("Task 4", "Task 4 Description", date(2024, 8, 11)),
        Task("Task 5", "Task 5 Description", date(2024, 8, 16)),
    ]
    tasksFilePath: str = "tasks.pickle"

    while True:
        try:
            print("\nTask Manager Menu:")
            print("1. Create Task")
            print("2. Display Tasks")
            print("3. Complete Task")
            print("4. Display Tasks Sorted by deadline")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_task()
            elif choice == "2":
                display_tasks(tasks)
            elif choice == "3":
                mark_task_completed_or_update_deadline()
            elif choice == "4":
                display_tasks(sort_tasks_by_deadline(tasks))
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f'Error: {e}')