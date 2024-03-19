#!/usr/bin/python3

''' Module for retrieving API data'''

import json
import requests
import sys

if __name__ == '__main__':

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_ext = '/users/{}'.format(sys.argv[1])
    todo_ext = '/todos'
    file_name = "{}.json".format(sys.argv[1])

    employee_response = requests.get(base_url+user_ext)
    employee = employee_response.json()
    todo_response = requests.get(base_url+user_ext+todo_ext)
    todos = todo_response.json()

    json_key = "{}".format(employee['id'])
    employee_json = {json_key: []}
    for todo in todos:
        task_dict = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee['username']}
        employee_json[json_key].append(task_dict)

        with open(file_name, 'w') as file:
            file.write(json.dumps(employee_json))