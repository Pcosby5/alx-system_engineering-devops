#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    # API URL to fetch the list of users
    url = "https://jsonplaceholder.typicode.com/users"

    # Fetching users data
    response = requests.get(url)
    users = response.json()

    # Dictionary to store tasks for each user
    dictionary = {}

    # Iterating through each user to fetch their tasks
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # URL to fetch tasks for the current user
        todo_url = ("https://jsonplaceholder.typicode.com/users/{}/todos/"
        .format(user_id))

        # Fetching tasks for the user
        response = requests.get(todo_url)
        tasks = response.json()

        # Storing tasks for the user in the dictionary
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    # Exporting the dictionary to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
