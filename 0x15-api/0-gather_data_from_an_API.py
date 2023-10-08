#!/usr/bin/python3
"""
script for parsing web data from an api
"""
import json
import requests
import sys


def fetch_user_info(userId):
    # create Response object for specific user
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error fetching user data.")
        sys.exit(1)

    user_info = json.loads(user_response.text)
    return user_info


def fetch_user_tasks(userId):
    # create Response object for user's tasks
    tasks_url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(userId)
    tasks_response = requests.get(tasks_url)

    if tasks_response.status_code != 200:
        print("Error fetching user's tasks data.")
        sys.exit(1)

    tasks_info = json.loads(tasks_response.text)
    return tasks_info


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <userId>")
        sys.exit(1)

    userId = sys.argv[1]
    user_info = fetch_user_info(userId)
    tasks_info = fetch_user_tasks(userId)

    employee_name = user_info["name"]
    num_done = sum(1 for task in tasks_info if task["completed"])
    num_tasks = len(tasks_info)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, num_done, num_tasks
        )
    )

    for task in tasks_info:
        if task["completed"]:
            print("\t {}".format(task["title"]))
