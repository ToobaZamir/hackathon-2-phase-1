# Quickstart Guide: Console Todo App

## Prerequisites
- Python 3.13+ installed
- Windows users: WSL 2 (as per specification)

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is available in your environment

## Running the Application
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
Added task: Buy groceries [ID: 1]

> add "Walk the dog"
Added task: Walk the dog [ID: 2]

> view
1. [ ] Buy groceries
2. [x] Walk the dog

> mark 2 complete
Task 2 marked as complete

> update 1 "Buy groceries and cook dinner"
Task 1 updated: Buy groceries and cook dinner

> delete 2
Task 2 deleted

> view
1. [ ] Buy groceries and cook dinner

> quit
```

## Error Handling
The application provides descriptive error messages for:
- Invalid command syntax
- Non-existent task IDs
- Empty task descriptions
- Invalid command parameters