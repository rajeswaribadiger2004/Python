class Task:
    def __init__(self, id, title, description, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Status: {self.status}\nDescription: {self.description}"


def create_task(task_list):
    task_id = len(task_list) + 1  # Assigning a new ID based on the length of the list
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status (Default: Pending): ") or "Pending"
    
    new_task = Task(task_id, title, description, status)
    task_list.append(new_task)
    print(f"Task '{title}' created successfully!")


def read_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        for task in task_list:
            print(task)
            print("-" * 40)


def update_task(task_list):
    task_id = int(input("Enter task ID to update: "))
    
    # Find the task with the given ID
    task = next((t for t in task_list if t.id == task_id), None)
    
    if task:
        print(f"Updating task {task_id}: {task.title}")
        new_title = input(f"Enter new title (current: {task.title}): ") or task.title
        new_description = input(f"Enter new description (current: {task.description}): ") or task.description
        new_status = input(f"Enter new status (current: {task.status}): ") or task.status
        
        task.title = new_title
        task.description = new_description
        task.status = new_status
        print(f"Task {task_id} updated successfully!")
    else:
        print("Task not found.")


def delete_task(task_list):
    task_id = int(input("Enter task ID to delete: "))
    
    # Find and remove the task
    task = next((t for t in task_list if t.id == task_id), None)
    
    if task:
        task_list.remove(task)
        print(f"Task {task_id} deleted successfully!")
    else:
        print("Task not found.")


def display_menu():
    print("\nTask Manager Application")
    print("1. Create a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")


def main():
    task_list = []  # List to store tasks
    
    while True:
        display_menu()
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            create_task(task_list)
        elif choice == "2":
            read_tasks(task_list)
        elif choice == "3":
            update_task(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


#OUTPUT
'''
Task Manager Application
1. Create a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Exit
Choose an option (1-5): 1
Enter task title: eat
Enter task description: eating apple
Enter task status (Default: Pending): completed
Task 'eat' created successfully!

Task Manager Application
1. Create a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Exit
Choose an option (1-5): 3
Enter task ID to update: 1
Updating task 1: eat
Enter new title (current: eat): drink
Enter new description (current: eating apple): drink apple juice
Enter new status (current: completed): pending
Task 1 updated successfully!

Task Manager Application
1. Create a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Exit
Choose an option (1-5): 2
ID: 1, Title: drink, Status: pending
Description: drink apple juice
----------------------------------------

Task Manager Application
1. Create a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Exit'''