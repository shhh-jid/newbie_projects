tasks = []

def show_menu():
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f'"{task}" added.')

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        print(f'"{removed}" removed.')
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
