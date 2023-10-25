#!/usr/bin/python3
"""Fetch and display information about an employee
API https://jsonplaceholder.typicode.com/
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get("{}/{}".format(url, employee_id))

    employee_name = response.json().get('name')

    """To get the todos """
    todo_url = url + "/" + employee_id + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_task.append(task)
            done += 1

    print("Employee {} is done with task({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_task:
        print("\t {}".format(task.get('title')))
