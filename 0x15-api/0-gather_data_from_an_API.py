#!/usr/bin/python3
"""
gather employee data from API
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_progress(employee_id):
    req = requests.get(f"{REST_API}/users/{employee_id}").json()
    task_req = requests.get(f"{REST_API}/todos").json()
    emp_name = req.get("name")
    tasks = list(filter(lambda x: x.get("userId") == employee_id, task_req))
    completed_tasks = list(filter(lambda x: x.get("completed"), tasks))

    progress_message = "Employee {} is done with tasks({}/{}):".format(
        emp_name, len(completed_tasks), len(tasks)
    )

    return progress_message, [task.get("title") for task in completed_tasks]


if __name__ == "__main__":
    if len(sys.argv) != 2 or not re.fullmatch(r"\d+", sys.argv[1]):
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    progress_message, completed_task_titles = get_progress(employee_id)

    print(progress_message)
    if completed_task_titles:
        for title in completed_task_titles:
            print("\t" + title)
