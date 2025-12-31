# Console Todo App

A simple command-line todo application with in-memory storage, built with Python.

## Features

- Add new todo items
- View all todo items with completion status
- Update existing todo items
- Delete todo items
- Mark items as complete/incomplete

## Requirements

- Python 3.8 or higher

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.8+ is available in your environment
4. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

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

The application follows a modular architecture with separation of concerns:

- `main.py`: Application entry point and command-line interface
- `todo_app/`: Main package containing all application components
  - `cli/todo_cli.py`: Command-line interface and command parsing
  - `services/todo_service.py`: Business logic and data management
  - `models/todo_item.py`: Data model representing individual todo items
  - `exceptions.py`: Custom exception classes
- `TodoItem` class: Represents individual todo items with ID, text, and completion status
- `TodoService` class: Handles all CRUD operations with in-memory storage
- `TodoCLI` class: Handles user commands and interacts with the TodoService

## Project Structure

```
src/
├── main.py                 # Application entry point
├── todo_app/               # Main application package
│   ├── __init__.py
│   ├── cli/                # Command-line interface components
│   │   ├── __init__.py
│   │   └── todo_cli.py     # CLI interface and command handling
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   └── todo_item.py    # TodoItem model
│   ├── services/           # Business logic
│   │   ├── __init__.py
│   │   └── todo_service.py # TodoService with CRUD operations
│   └── exceptions.py       # Custom exception classes
```

## Development

This project uses a clean architecture with clear separation between:
- Presentation layer (CLI)
- Business logic layer (Services)
- Data layer (Models)

## Note

There are some merge conflicts in the main.py file that should be resolved before further development.