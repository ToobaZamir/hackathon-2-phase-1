"""
CLI interface and command handling for the todo application.
"""
from typing import List
from .todo_service import TodoService
from ..exceptions import InvalidTaskError, TaskNotFoundError


class TodoCLI:
    """
    Command-line interface for the todo application.
    Handles user commands and interacts with the TodoService.
    """
    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a TodoService instance.

        Args:
            service (TodoService): The service to handle business logic
        """
        self.service = service

    def print_help(self):
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

    def print_items(self, items: List):
        """Print all items in a formatted way."""
        if not items:
            print("\nNo tasks found.")
            return

        print("\nYour tasks:")
        for item in items:
            print(f"  {item}")

    def handle_add(self, description: str):
        """
        Handle the add command.

        Args:
            description (str): Description of the task to add
        """
        try:
            item = self.service.add_item(description)
            print(f"Added task: {item}")
        except InvalidTaskError as e:
            print(f"Error: {e}")

    def handle_view(self):
        """Handle the view command."""
        items = self.service.get_all_items()
        self.print_items(items)

    def handle_delete(self, item_id: int):
        """
        Handle the delete command.

        Args:
            item_id (int): ID of the item to delete
        """
        try:
            self.service.delete_item(item_id)
            print(f"Task {item_id} deleted successfully.")
        except TaskNotFoundError as e:
            print(f"Error: {e}")

    def handle_update(self, item_id: int, new_description: str):
        """
        Handle the update command.

        Args:
            item_id (int): ID of the item to update
            new_description (str): New description for the item
        """
        try:
            self.service.update_item(item_id, new_description)
            item = self.service.get_item_by_id(item_id)
            print(f"Task {item_id} updated: {item}")
        except TaskNotFoundError as e:
            print(f"Error: {e}")
        except InvalidTaskError as e:
            print(f"Error: {e}")

    def handle_mark(self, item_id: int, status: str):
        """
        Handle the mark command.

        Args:
            item_id (int): ID of the item to mark
            status (str): Status to set ('complete' or 'incomplete')
        """
        try:
            if status.lower() in ['complete', 'done']:
                self.service.mark_item_complete(item_id)
                item = self.service.get_item_by_id(item_id)
                print(f"Task {item_id} marked as complete: {item}")
            elif status.lower() in ['incomplete', 'todo']:
                self.service.mark_item_incomplete(item_id)
                item = self.service.get_item_by_id(item_id)
                print(f"Task {item_id} marked as incomplete: {item}")
            else:
                print("Error: Status must be 'complete' or 'incomplete'.")
        except TaskNotFoundError as e:
            print(f"Error: {e}")

    def parse_command(self, user_input: str):
        """
        Parse and execute a command from user input.

        Args:
            user_input (str): The command input from the user

        Returns:
            bool: True if the application should continue, False to quit
        """
        if not user_input.strip():
            return True

        parts = user_input.split()
        command = parts[0].lower()

        if command == "quit":
            return False
        elif command == "help":
            self.print_help()
        elif command == "add":
            # Extract the task description from the input
            # Handle quoted strings properly
            if len(parts) < 2:
                print("Error: Please provide a task description. Usage: add \"<task description>\"")
                return True

            # Reconstruct the description from the remaining parts
            description = " ".join(parts[1:])

            # If the description is quoted, extract just the quoted part
            if description.startswith('"') and description.endswith('"') and len(description) > 1:
                description = description[1:-1]  # Remove the quotes

            self.handle_add(description)
        elif command == "view":
            self.handle_view()
        elif command == "delete":
            if len(parts) != 2:
                print("Error: Please provide a task ID. Usage: delete <id>")
                return True

            try:
                item_id = int(parts[1])
                self.handle_delete(item_id)
            except ValueError:
                print("Error: Task ID must be a number.")
        elif command == "update":
            if len(parts) < 3:
                print("Error: Please provide task ID and new description. Usage: update <id> \"<new description>\"")
                return True

            try:
                item_id = int(parts[1])

                # Extract the new description
                description_parts = parts[2:]
                new_description = " ".join(description_parts)

                # If the description is quoted, extract just the quoted part
                if new_description.startswith('"') and new_description.endswith('"') and len(new_description) > 1:
                    new_description = new_description[1:-1]  # Remove the quotes

                self.handle_update(item_id, new_description)
            except ValueError:
                print("Error: Task ID must be a number.")
        elif command == "mark":
            if len(parts) != 3:
                print("Error: Please provide task ID and status. Usage: mark <id> <complete|incomplete>")
                return True

            try:
                item_id = int(parts[1])
                status = parts[2].lower()
                self.handle_mark(item_id, status)
            except ValueError:
                print("Error: Task ID must be a number.")
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")

        return True