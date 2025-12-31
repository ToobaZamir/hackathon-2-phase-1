"""
TodoService - Business logic for todo operations with in-memory storage.
Implements all CRUD operations for todo items.
"""

from typing import List, Optional
from ..models.todo_item import TodoItem
from ..exceptions import InvalidTaskError, TaskNotFoundError


class TodoService:
    """
    Manages a collection of todo items with CRUD operations.
    Uses in-memory storage as specified in the requirements.
    """
    def __init__(self):
        """
        Initialize the todo service with an empty list of items.
        """
        self.items: List[TodoItem] = []
        self.next_id = 1

    def add_item(self, text: str) -> TodoItem:
        """
        Add a new todo item to the collection.

        Args:
            text (str): Description of the item

        Returns:
            TodoItem: The newly created item

        Raises:
            InvalidTaskError: If the text is invalid
        """
        if not isinstance(text, str) or len(text) < 1 or len(text) > 500:
            raise InvalidTaskError("Item text must be a string between 1 and 500 characters")

        item = TodoItem(self.next_id, text)
        self.items.append(item)
        self.next_id += 1
        return item

    def get_all_items(self) -> List[TodoItem]:
        """
        Get all todo items in the collection.

        Returns:
            List[TodoItem]: List of all items
        """
        return self.items.copy()

    def get_item_by_id(self, item_id: int) -> Optional[TodoItem]:
        """
        Get a todo item by its ID.

        Args:
            item_id (int): ID of the item to retrieve

        Returns:
            TodoItem or None: The item if found, None otherwise
        """
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def update_item(self, item_id: int, new_text: str) -> bool:
        """
        Update the text of an existing item.

        Args:
            item_id (int): ID of the item to update
            new_text (str): New text for the item

        Returns:
            bool: True if the item was updated, False if not found

        Raises:
            InvalidTaskError: If the new text is invalid
        """
        if not isinstance(new_text, str) or len(new_text) < 1 or len(new_text) > 500:
            raise InvalidTaskError("Item text must be a string between 1 and 500 characters")

        item = self.get_item_by_id(item_id)
        if item:
            item.text = new_text
            return True
        else:
            raise TaskNotFoundError(f"Task with ID {item_id} not found.")

    def delete_item(self, item_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            item_id (int): ID of the item to delete

        Returns:
            bool: True if the item was deleted, False if not found

        Raises:
            TaskNotFoundError: If the item is not found
        """
        item = self.get_item_by_id(item_id)
        if item:
            self.items.remove(item)
            return True
        else:
            raise TaskNotFoundError(f"Task with ID {item_id} not found.")

    def mark_item_complete(self, item_id: int) -> bool:
        """
        Mark a todo item as complete.

        Args:
            item_id (int): ID of the item to mark complete

        Returns:
            bool: True if the item was marked complete, False if not found

        Raises:
            TaskNotFoundError: If the item is not found
        """
        item = self.get_item_by_id(item_id)
        if item:
            item.completed = True
            return True
        else:
            raise TaskNotFoundError(f"Task with ID {item_id} not found.")

    def mark_item_incomplete(self, item_id: int) -> bool:
        """
        Mark a todo item as incomplete.

        Args:
            item_id (int): ID of the item to mark incomplete

        Returns:
            bool: True if the item was marked incomplete, False if not found

        Raises:
            TaskNotFoundError: If the item is not found
        """
        item = self.get_item_by_id(item_id)
        if item:
            item.completed = False
            return True
        else:
            raise TaskNotFoundError(f"Task with ID {item_id} not found.")

    def get_item_count(self) -> int:
        """
        Get the total number of items.

        Returns:
            int: Number of items in the collection
        """
        return len(self.items)

    def get_completed_item_count(self) -> int:
        """
        Get the number of completed items.

        Returns:
            int: Number of completed items
        """
        return sum(1 for item in self.items if item.completed)

    def get_pending_item_count(self) -> int:
        """
        Get the number of pending items.

        Returns:
            int: Number of pending items
        """
        return sum(1 for item in self.items if not item.completed)