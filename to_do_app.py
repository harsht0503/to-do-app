tasks = []
def add_task():
    title = input("Enter task description: ").strip()
    if title:
        task = {
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        }
        tasks.append(task)
        print(f"Task '{title}' added successfully!!!\n")
    else:
        print("Task description cannot be empty!!!\n")

def show_tasks():
    if not tasks:
        print("No tasks found.\n")
        return
    
    print("\nYour To-Do List:")
    for task in tasks:
        status = "COMPLETE" if task["completed"] else "INCOMPLETE"
        print(f"[{status}] {task['id']}. {task['title']}")
    print()

def complete_task():
    show_tasks()
    
    try:
        task_id = int(input("Enter the task ID to mark as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task '{task['title']}' marked as completed!\n")
                return
        print("Task not found!\n")
    except ValueError:
        print("Invalid input\nPlease enter a valid task ID\n")

def edit_task():
    show_tasks()

    try:
        task_id = int(input("Enter the task ID to edit: "))
        for task in tasks:
            if task["id"] == task_id:
                new_title = input("Enter new task description: ").strip()
                if new_title:
                    task["title"] = new_title
                    print("Task updated successfully!!!\n")
                else:
                    print("Task description cannot be empty!!!\n")
                return
        print("Task not found!\n")
    except ValueError:
        print("Invalid input\nPlease enter a valid task ID\n")

def delete_task():
    show_tasks()

    try:
        task_id = int(input("Enter the task ID to delete: "))
        global tasks
        new_tasks = [task for task in tasks if task["id"] != task_id]

        if len(new_tasks) == len(tasks):
            print("Task not found!\n")
        else:
            tasks = new_tasks
            print("Task deleted successfully!!!\n")
    except ValueError:
        print("Invalid input\nPlease enter a valid task ID\n")

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1 Add Task")
        print("2 Show Tasks")
        print("3 Complete Task")
        print("4 Edit Task")
        print("5 Delete Task")
        print("6 Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice\nPlease enter a number between 1-6\n")

if __name__ == "__main__":
    main()
