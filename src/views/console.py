from src.controllers.list_controller import ListTaskController
from src.controllers.task_controller import TaskController
from src.db.db_connection import get_connection, init_db

def console_view_todo_app():
    conn = get_connection()
    init_db(conn)
    task_controller = TaskController(conn)
    list_controller = ListTaskController(conn)

    while True:
        print("Hello, welcome to the todo app")
        print("Choose an option:")
        print("1. Add a new task")
        print("2. View a task")
        print("3. Delete a task")
        print("4. Add a new list")
        print("5. View a list")
        print("6. Delete a list")
        print("8. Add task to a list")
        print("7. Exit")
        
        user_input = input("Enter a number: ")
        
        if user_input == "1":
            print("Provide the following details to add a new task:")
            title = input("Title: ")
            description = input("Description (optional): ")
            deadline = input("Deadline (YYYY-MM-DD) (optional): ")
            list_id = input("List ID (optional): ")
            list_id = int(list_id) if list_id else None
            task_id = task_controller.add_task(title, description, deadline, list_id)
            print(f"Task added {task_id}")
        elif user_input == "2":
            print("Provide the ID of the task you want to view:")
            task_id = int(input("Task ID: "))
            task = task_controller.get_task(task_id)
            if task:
                print(f"Task ID: {task.id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Deadline: {task.deadline}")
                print(f"List ID: {task.list_id}")
            else:
                print("Task was not found")
        elif user_input == "4":
            print("Provide the following details to add a new list:")
            name = input("List Name: ")
            list_id = list_controller.add_list(name)
            print(f"List added with ID: {list_id}")
        elif user_input == "8":
            print("Provide the following details to add a task to a list:")
            task_id = int(input("Task ID: "))
            list_id = int(input("List ID: "))
            task_controller.add_task_to_list(task_id, list_id)
            task = task_controller.get_task(task_id)
            print(f"Task ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Deadline: {task.deadline}")
            print(f"List ID: {task.list_id}")
            print()
        elif user_input == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
