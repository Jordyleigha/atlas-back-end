#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""
import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # Get info from API
    response = requests.get(user_url)
    # Parse the data into JSON format
    data = json.loads(response.text)
    # Extract user data, in this case, name of employee
    username = data[0].get('name')

    # Get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # Get info from API
    response = requests.get(tasks_url)
    # Parse the data into JSON format
    tasks = json.loads(response.text)

    # Check if all tasks are found
    if len(tasks) == 20:
        print("All tasks found: OK")
    else:
        print("Number of tasks missing:", 20 - len(tasks))
