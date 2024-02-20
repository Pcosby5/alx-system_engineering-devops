#!/usr/bin/python3
"""Accessing a REST API for employees to do lists progress"""

import requests
import sys

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
    employee_Name = response.json().get('name')

    # Constructing the URL for fetching employee's TODO list
    todo_Url = url + "/todos"

    # Fetching employee's TODO list
    response = requests.get(todo_Url)
    tasks = response.json()
    num_of_done_task = 0
    completed_tasks = []

    # Iterating through tasks to count completed tasks and gather their details
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            num_of_done_task += 1

    # Displaying employee's TODO list progress
    total_num_of_task = len(tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_Name, num_of_done_task, total_num_of_task))

    # Displaying titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
