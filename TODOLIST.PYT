tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        show_tasks()
        try:
            task_no = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed}")
        except:
            print("Invalid task number!")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")