class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the list.')
        else:
            print(f'Task "{task}" not found in the list.')

    def show_tasks(self):
        if self.tasks:
            print("Tasks in the list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        else:
            print("No tasks in the list.")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
