#!/usr/bin/python3

import requests
import sys


def fetch_employee_data(employee_id):
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Error fetching employee data")
        return

    # Fetch todos data
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employees TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching TODO list")
        return

    todos_data = todos_response.json()

    # Flter completed tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # print the required information
    print(f"Employee {employee_name} is done with tasks "
          f"({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueErrorr:
        print("Employee ID must be an Integer")
        sys.exit(1)

    fetch_employee_data(employee_id)
