import json
import os

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✔" if task.completed else "✘"
            print(f"{i+1}. [{status}] {task.title}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task: ")
            manager.add_task(title)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            index = int(input("Task number: ")) - 1
            manager.complete_task(index)

        elif choice == "4":
            index = int(input("Task number: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()