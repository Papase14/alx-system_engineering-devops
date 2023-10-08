#!/usr/bin/python3
"""script for parsing web data from an api
"""
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_url = f"{base_url}/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()

    # Fetch user's todos
    todos_url = f"{base_url}/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Print progress information
    print(
        f'Employee {user_data["name"]} is done with' +
        f'tasks({completed_tasks}/{total_tasks}):'
    )

    for todo in todos_data:
        if todo["completed"]:
            print(f'\t{todo["title"]}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
