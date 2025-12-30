"""
Task management logic for the console todo application.
Implements all CRUD operations for tasks with in-memory storage.
"""

from typing import List, Optional
import re


class Task:
    """
    Represents a single todo task with ID, text, and completion status.
    """
    def __init__(self, task_id: int, text: str, completed: bool = False):
        """
        Initialize a new task.

        Args:
            task_id (int): Unique identifier for the task
            text (str): Description of the task (max 500 characters)
            completed (bool): Completion status (default: False)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not isinstance(text, str) or len(text) < 1 or len(text) > 500:
            raise ValueError("Task text must be a string between 1 and 500 characters")

        if not isinstance(completed, bool):
            raise ValueError("Completion status must be a boolean")

        self.id = task_id
        self.text = text
        self.completed = completed

    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            str: Formatted string with status indicator, ID, and text
        """
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.text}"

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary with task properties
        """
        return {
            "id": self.id,
            "text": self.text,
            "completed": self.completed
        }


class TaskManager:
    """
    Manages a collection of tasks with CRUD operations.
    Uses in-memory storage as specified in the requirements.
    """
    def __init__(self):
        """
        Initialize the task manager with an empty list of tasks.
        """
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, text: str) -> Task:
        """
        Add a new task to the collection.

        Args:
            text (str): Description of the task

        Returns:
            Task: The newly created task

        Raises:
            ValueError: If the text is invalid
        """
        if not isinstance(text, str) or len(text) < 1 or len(text) > 500:
            raise ValueError("Task text must be a string between 1 and 500 characters")

        task = Task(self.next_id, text)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, new_text: str) -> bool:
        """
        Update the text of an existing task.

        Args:
            task_id (int): ID of the task to update
            new_text (str): New text for the task

        Returns:
            bool: True if the task was updated, False if not found

        Raises:
            ValueError: If the new text is invalid
        """
        if not isinstance(new_text, str) or len(new_text) < 1 or len(new_text) > 500:
            raise ValueError("Task text must be a string between 1 and 500 characters")

        task = self.get_task_by_id(task_id)
        if task:
            task.text = new_text
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if the task was marked complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): ID of the task to mark incomplete

        Returns:
            bool: True if the task was marked incomplete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            int: Number of tasks in the collection
        """
        return len(self.tasks)

    def get_completed_task_count(self) -> int:
        """
        Get the number of completed tasks.

        Returns:
            int: Number of completed tasks
        """
        return sum(1 for task in self.tasks if task.completed)

    def get_pending_task_count(self) -> int:
        """
        Get the number of pending tasks.

        Returns:
            int: Number of pending tasks
        """
        return sum(1 for task in self.tasks if not task.completed)