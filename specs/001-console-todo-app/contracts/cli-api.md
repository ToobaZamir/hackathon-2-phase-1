# CLI API Contract: Console Todo App

## Command Structure
```
python main.py <command> [arguments]
```

## Commands

### Add Todo
```
add "task description"
```
- **Purpose**: Add a new todo item
- **Input**: Task description (string, 1-500 characters)
- **Output**: Success message with assigned ID
- **Error Cases**: 
  - Empty description: Returns error message
  - Description too long (>500 chars): Returns error message

### View Todos
```
view
```
- **Purpose**: Display all todo items
- **Input**: None
- **Output**: List of all todos with ID and completion status
- **Error Cases**: None

### Update Todo
```
update <id> "new description"
```
- **Purpose**: Update the description of an existing todo
- **Input**: Valid ID (positive integer), new description (1-500 characters)
- **Output**: Success message
- **Error Cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message
  - Empty description: Returns error message
  - Description too long: Returns error message

### Delete Todo
```
delete <id>
```
- **Purpose**: Remove a todo item
- **Input**: Valid ID (positive integer)
- **Output**: Success message
- **Error Cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message

### Mark Todo
```
mark <id> <complete|incomplete>
```
- **Purpose**: Change completion status of a todo
- **Input**: Valid ID (positive integer), status (complete|incomplete)
- **Output**: Success message
- **Error Cases**:
  - Invalid ID: Returns error message
  - Non-existent ID: Returns error message
  - Invalid status: Returns error message

### Help
```
help
```
- **Purpose**: Display available commands
- **Input**: None
- **Output**: Help text
- **Error Cases**: None

### Quit
```
quit
```
- **Purpose**: Exit the application
- **Input**: None
- **Output**: Application terminates
- **Error Cases**: None