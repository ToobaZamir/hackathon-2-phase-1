# Console Todo App - Development Guide for Claude

## Project Overview

This is a simple command-line todo application with in-memory storage, built with Python. The application implements all 5 core features: Add, View, Update, Delete, and Mark Complete.

## Run Command

To run the application:

```bash
python src/main.py
```

## Project Setup

1. Ensure Python 3.13 or higher is installed
2. Clone the repository
3. Navigate to the project directory
4. Run the application with the command above

For Windows users: WSL 2 is recommended for optimal compatibility.

## Code Structure

The application follows a modular Python architecture:

- `src/main.py` - Command-line interface and application entry point
- `src/task_manager.py` - Business logic and data management
- `src/__init__.py` - Package initialization file

## Code Style Guidelines

### Modular Design
- Separate concerns between UI (main.py) and business logic (task_manager.py)
- Keep classes focused on single responsibilities
- Use clear, descriptive function and variable names

### Python Best Practices
- Follow PEP 8 style guidelines
- Include type hints for all function parameters and return values
- Add docstrings for all classes and functions
- Use meaningful variable names (e.g., `add_task` instead of `add`)

### Error Handling
- Validate inputs and provide descriptive error messages
- Use appropriate exception handling
- Fail gracefully with user-friendly messages

### In-Memory Storage
- All data is stored in memory only (no persistence to files)
- Use appropriate data structures (lists, dictionaries) for efficient operations
- Maintain data integrity with proper validation

## Core Features

The application implements these 5 core features:
1. Add new todo items with descriptions
2. View all todo items with completion status
3. Update existing todo items
4. Delete todo items by ID
5. Mark items as complete/incomplete

## Validation Rules

- Task descriptions must be between 1 and 500 characters
- Task IDs are numeric and auto-incremented
- All user inputs are validated before processing
- Appropriate error messages are displayed for invalid inputs