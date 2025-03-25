class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = 'Done' if task['completed'] else 'Pending'
                print(f"{i}. {task['task']} - [{status}]")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter Task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                todo.mark_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                todo.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
