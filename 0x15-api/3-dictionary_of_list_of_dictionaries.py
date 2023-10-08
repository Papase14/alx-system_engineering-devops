#!/usr/bin/python3
"""
gather employee data from API and export to JSON
"""

import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch user data
user_response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}"
)
user_data = user_response.json()

# Fetch tasks data
tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")
tasks_data = tasks_response.json()

# Filter tasks for the specified user
user_tasks = [
    task for task in tasks_data if task["userId"] == int(employee_id)
]

# Create a dictionary to store the user's tasks
user_task_dict = {
    user_data["id"]: [
        {
            "username": user_data["username"],
            "task": task["title"],
            "completed": task["completed"],
        }
        for task in user_tasks
    ]
}

# Export the data to JSON
with open(f"{employee_id}.json", "w") as json_file:
    json.dump(user_task_dict, json_file, indent=4)

print(f"Data for user {employee_id} exported to {employee_id}.json")
