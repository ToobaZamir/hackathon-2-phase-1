"""
Custom exceptions for the todo application.
"""


class TodoError(Exception):
    """
    Base exception class for todo application errors.
    """
    pass


class InvalidTaskError(TodoError):
    """
    Raised when a task is invalid (e.g., invalid ID, text too long, etc.).
    """
    pass


class TaskNotFoundError(TodoError):
    """
    Raised when a requested task is not found.
    """
    pass


class ValidationError(TodoError):
    """
    Raised when validation fails for any input.
    """
    pass