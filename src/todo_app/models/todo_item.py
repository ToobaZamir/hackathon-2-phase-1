"""
TodoItem model representing a single todo task with ID, text, and completion status.
"""
from typing import Dict


class TodoItem:
    """
    Represents a single todo task with ID, text, and completion status.
    """
    def __init__(self, item_id: int, text: str, completed: bool = False):
        """
        Initialize a new todo item.

        Args:
            item_id (int): Unique identifier for the item
            text (str): Description of the task (max 500 characters)
            completed (bool): Completion status (default: False)
        """
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer")

        if not isinstance(text, str) or len(text) < 1 or len(text) > 500:
            raise ValueError("Item text must be a string between 1 and 500 characters")

        if not isinstance(completed, bool):
            raise ValueError("Completion status must be a boolean")

        self.id = item_id
        self.text = text
        self.completed = completed

    def __str__(self) -> str:
        """
        String representation of the todo item.

        Returns:
            str: Formatted string with status indicator, ID, and text
        """
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.text}"

    def to_dict(self) -> Dict:
        """
        Convert the todo item to a dictionary representation.

        Returns:
            dict: Dictionary with item properties
        """
        return {
            "id": self.id,
            "text": self.text,
            "completed": self.completed
        }