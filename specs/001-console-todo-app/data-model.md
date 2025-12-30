# Data Model: Console Todo App

## TodoItem Entity

### Fields
- **id**: `int` - Unique numeric identifier for the todo item (auto-incremented)
- **text**: `str` - The description of the task (max 500 characters)
- **completed**: `bool` - Status indicator for completion (default: False)

### Relationships
- None (standalone entity)

### Validation Rules
- `text` must be between 1 and 500 characters (inclusive)
- `id` must be a positive integer
- `completed` must be a boolean value

### State Transitions
- `completed` can transition from `False` to `True` (mark complete)
- `completed` can transition from `True` to `False` (mark incomplete)

## TodoList Container

### Fields
- **items**: `List[TodoItem]` - Collection of TodoItem objects
- **next_id**: `int` - Counter for generating next unique ID (starts at 1)

### Validation Rules
- No duplicate IDs allowed
- IDs must be sequential starting from 1
- Items list must not contain None values