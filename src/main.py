"""
Todo CLI entry point
Implements the command-line interface for the todo application.
"""
import sys
from task_manager import TaskManager


def print_help():
    """Print the help message with available commands."""
    print("\nAvailable commands:")
    print("  add \"<task description>\"    - Add a new task")
    print("  view                        - View all tasks")
    print("  update <id> \"<new text>\"    - Update a task")
    print("  delete <id>                 - Delete a task")
    print("  mark <id> <complete|incomplete> - Mark task as complete/incomplete")
    print("  help                        - Show this help message")
    print("  quit                        - Exit the application")
    print()


def print_tasks(tasks):
    """Print all tasks in a formatted way."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour tasks:")
    for task in tasks:
        print(f"  {task}")


def main():
    """Main entry point for the todo application."""
    print("Welcome to the Todo CLI Application!")
    print("Type 'help' for available commands or 'quit' to exit.")

    task_manager = TaskManager()

    while True:
        try:
            # Get user input
            user_input = input("\n> ").strip()

            # Parse the command
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "quit":
                print("Goodbye!")
                break
            elif command == "help":
                print_help()
            elif command == "add":
                # Extract the task description from the input
                # Handle quoted strings properly
                if len(parts) < 2:
                    print("Error: Please provide a task description. Usage: add \"<task description>\"")
                    continue

                # Reconstruct the description from the remaining parts
                description = " ".join(parts[1:])

                # If the description is quoted, extract just the quoted part
                if description.startswith('"') and description.endswith('"') and len(description) > 1:
                    description = description[1:-1]  # Remove the quotes

                try:
                    task = task_manager.add_task(description)
                    print(f"Added task: {task}")
                except ValueError as e:
                    print(f"Error: {e}")
            elif command == "view":
                tasks = task_manager.get_all_tasks()
                print_tasks(tasks)
            elif command == "delete":
                if len(parts) != 2:
                    print("Error: Please provide a task ID. Usage: delete <id>")
                    continue

                try:
                    task_id = int(parts[1])
                    if task_manager.delete_task(task_id):
                        print(f"Task {task_id} deleted successfully.")
                    else:
                        print(f"Error: Task with ID {task_id} not found.")
                except ValueError:
                    print("Error: Task ID must be a number.")
            elif command == "update":
                if len(parts) < 3:
                    print("Error: Please provide task ID and new description. Usage: update <id> \"<new description>\"")
                    continue

                try:
                    task_id = int(parts[1])

                    # Extract the new description
                    description_parts = parts[2:]
                    new_description = " ".join(description_parts)

                    # If the description is quoted, extract just the quoted part
                    if new_description.startswith('"') and new_description.endswith('"') and len(new_description) > 1:
                        new_description = new_description[1:-1]  # Remove the quotes

                    if task_manager.update_task(task_id, new_description):
                        task = task_manager.get_task_by_id(task_id)
                        print(f"Task {task_id} updated: {task}")
                    else:
                        print(f"Error: Task with ID {task_id} not found.")
                except ValueError:
                    print("Error: Task ID must be a number.")
            elif command == "mark":
                if len(parts) != 3:
                    print("Error: Please provide task ID and status. Usage: mark <id> <complete|incomplete>")
                    continue

                try:
                    task_id = int(parts[1])
                    status = parts[2].lower()

                    if status == "complete" or status == "done":
                        if task_manager.mark_task_complete(task_id):
                            task = task_manager.get_task_by_id(task_id)
                            print(f"Task {task_id} marked as complete: {task}")
                        else:
                            print(f"Error: Task with ID {task_id} not found.")
                    elif status == "incomplete" or status == "todo":
                        if task_manager.mark_task_incomplete(task_id):
                            task = task_manager.get_task_by_id(task_id)
                            print(f"Task {task_id} marked as incomplete: {task}")
                        else:
                            print(f"Error: Task with ID {task_id} not found.")
                    else:
                        print("Error: Status must be 'complete' or 'incomplete'.")
                except ValueError:
                    print("Error: Task ID must be a number.")
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()