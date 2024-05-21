#!/usr/bin/python3

"""
Python script to export data in JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 1:
        exit()

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

all_tasks = {}

for user in users:
    user_id = str(user['id'])
    username = user['username']

    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()

    task_list = []
    for tasks in tasks:
        task_list.append({
            "username": username,
            "task": tasks['title'],
            "completed": tasks['completed']
            })

    all_tasks[user_id] = task_list
with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)
