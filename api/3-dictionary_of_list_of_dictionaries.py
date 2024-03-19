#!/usr/bin/python3

''' Module for retrieving API data'''

import json
import requests
import sys

if __name__ == '__main__':

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_ext = '/users/'
    todo_ext = '/todos'

    employees_dict = {}
    employee_response = requests.get(base_url+user_ext)
    employees = employee_response.json()

    for employee in employees:
        json_key = "{}".format(employee['id'])
        employee_json = {json_key: []}
        todo_response = requests.get(base_url+user_ext+json_key+todo_ext)
        todos = todo_response.json()
        for todo in todos:
            task_dict = {
                "username": employee['username'],
                "task": todo['title'],
                "completed": todo['completed']}
            employee_json[json_key].append(task_dict)
        employees_dict.update(employee_json)

    with open('todo_all_employees.json', 'w') as file:
        file.write(json.dumps(employees_dict))