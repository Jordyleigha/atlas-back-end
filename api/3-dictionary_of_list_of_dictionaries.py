#!/usr/bin/python3
"""
Export data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be: {
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS},
        ...
    ]
}
File name must be: todo_all_employees.json
"""

import json
import requests


def export_to_json():
    """
    Export data to JSON file.
    """
    # URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch data
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Initialize dictionary to store user tasks
    user_tasks = {}

    # Populate user_tasks dictionary
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = []
        for todo in todos:
            if todo['userId'] == user_id:
                task = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks[user_id].append(task)

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    export_to_json()
     # Add a new line chraccter at the end of file