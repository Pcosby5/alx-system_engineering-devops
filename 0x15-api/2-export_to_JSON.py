#!/usr/bin/python3
"""Accessing a REST API for employees to do lists progress"""

import requests
import sys
import json

if __name__ == '__main__':

    # Extracting employee ID from command line argument
    employee_Id = sys.argv[1]

    # Base URL for the API
    base_Url = "https://jsonplaceholder.typicode.com"

    # Constructing the URL for fetching employee details
    url = base_Url + "/users" + "/" + employee_Id

    # Fetching employee details
    response = requests.get(url)

    # Extracting employee name from the response JSON
    username = response.json().get('username')

    # Constructing the URL for fetching employee's TODO list
    todo_Url = url + "/todos"

    # Fetching employee's TODO list
    response = requests.get(todo_Url)
    tasks = response.json()

    # Construct a dictionary
    json_dict = {"employee_id": []}

    for task in tasks:
        task_obj = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        json_dict["employee_id"].append(task_obj)

    # Export into json file
    with open('{}.json'.format(employee_Id), 'w') as file:
        json.dump(json_dict, file)
