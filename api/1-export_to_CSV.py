#!/usr/bin/python3
"""Script that fetches info about a given employee using an API
and exports it in CSV format.
"""
import json
import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info, e.g., https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(BASE_URL, user_id)

    # Get info from API
    response = requests.get(user_url)
    # Pull data from API
    data = response.text
    # Parse the data into JSON format
    data = json.loads(data)
    # Extract user data, in this case, username of employee
    user_name = data[0].get('username')

    # Get user info about todo tasks
    # e.g., https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(BASE_URL, user_id)

    # Get info from API
    response = requests.get(tasks_url)
    # Pull data from API
    tasks = response.text
    # Parse the data into JSON format
    tasks = json.loads(tasks)
    # Build the CSV
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
