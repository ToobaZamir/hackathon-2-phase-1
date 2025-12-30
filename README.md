# Console Todo App

A simple command-line todo application with in-memory storage, built with Python.

## Features

- Add new todo items
- View all todo items with completion status
- Update existing todo items
- Delete todo items
- Mark items as complete/incomplete

## Requirements

- Python 3.13 or higher
- Windows users: WSL 2 recommended

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is available in your environment

## Usage

Run the application from the src directory:

```bash
cd src
python main.py
```

## Available Commands

- `add "task description"` - Add a new todo item
- `view` - View all todo items with status
- `update <id> "new description"` - Update a todo item
- `delete <id>` - Delete a todo item
- `mark <id> <complete|incomplete>` - Mark item as complete/incomplete
- `help` - Show available commands
- `quit` - Exit the application

## Example Usage

```
> add "Buy groceries"
Added task: [ ] 1. Buy groceries

> add "Walk the dog"
Added task: [ ] 2. Walk the dog

> view
Your tasks:
  [ ] 1. Buy groceries
  [ ] 2. Walk the dog

> mark 2 complete
Task 2 marked as complete: [x] 2. Walk the dog

> update 1 "Buy groceries and cook dinner"
Task 1 updated: [ ] 1. Buy groceries and cook dinner

> delete 2
Task 2 deleted successfully.

> view
Your tasks:
  [ ] 1. Buy groceries and cook dinner

> quit
```

## Error Handling

The application provides descriptive error messages for:
- Invalid command syntax
- Non-existent task IDs
- Empty task descriptions
- Invalid command parameters
- Task text exceeding 500 characters

## Architecture

The application follows a modular architecture:
- `main.py`: Command-line interface and application entry point
- `task_manager.py`: Business logic and data management
- `Task` class: Represents individual todo items
- `TaskManager` class: Handles all CRUD operations with in-memory storage