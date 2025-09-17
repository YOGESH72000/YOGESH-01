import json
import os

FILE_NAME = "todo_list.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"✅ Task '{title}' added.")
    else:
        print("⚠️ Task title cannot be empty.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📝 Your Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. [{status}] {task['title']}")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as complete: ")) - 1
        tasks[idx]["completed"] = True
        print("✅ Task marked as completed.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        task = tasks.pop(idx)
        print(f"🗑️ Task '{task['title']}' deleted.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()