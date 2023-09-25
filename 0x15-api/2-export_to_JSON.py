#!/usr/bin/python3
"""
gather employee data from API and export to JSON
"""


import json
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    req = requests.get(f"{REST_API}/users/{employee_id}").json()
    task_req = requests.get(f"{REST_API}/todos").json()
    emp_name = req.get("name")
    tasks = list(filter(lambda x: x.get("userId") == employee_id, task_req))
    completed_tasks = list(filter(lambda x: x.get("completed"), tasks))

    return emp_name, completed_tasks


def export_to_json(employee_id, emp_name, completed_tasks):
    data = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": emp_name,
            }
            for task in completed_tasks
        ]
    }
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not re.fullmatch(r"\d+", sys.argv[1]):
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    emp_name, completed_tasks = get_employee_todo_progress(employee_id)

    export_to_json(employee_id, emp_name, completed_tasks)

    print(f"Data exported to {employee_id}.json")
