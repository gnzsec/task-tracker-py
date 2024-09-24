import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')

# List all tasks
def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if status is None or task['status'] == status:
            print(task)

# Update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully.')
            return
    print(f'Task {task_id} not found.')

# Mark a task as done or in progress
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}.')
            return
    print(f'Task {task_id} not found.')

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully.')

# Main function to handle command line arguments
def main():
    if len(sys.argv) < 2:
        print("Please provide a command.")
        return

    command = sys.argv[1]

    if command == 'add':
        add_task(' '.join(sys.argv[2:]))
    elif command == 'list':
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    elif command == 'update':
        task_id = int(sys.argv[2])
        new_description = ' '.join(sys.argv[3:])
        update_task(task_id, new_description)
    elif command == 'mark-done':
        task_id = int(sys.argv[2])
        mark_task(task_id, 'done')
    elif command == 'mark-in-progress':
        task_id = int(sys.argv[2])
        mark_task(task_id, 'in-progress')
    elif command == 'delete':
        task_id = int(sys.argv[2])
        delete_task(task_id)
    else:
        print("Unknown command.")

if __name__ == '__main__':
    main()
