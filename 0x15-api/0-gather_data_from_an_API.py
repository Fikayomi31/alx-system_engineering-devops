#!/usr/bin/python3
"""Fetch and display information about an employee
API: https://jsonplaceholder.typicode.com/
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = api = "https://jsonplaceholder.typicode.com/users"

    response = requests.get("{}/{}".format(url, employee_id))
    employee_name = response.json().get('name')

    todo_url = url + "/" + employee_id + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
