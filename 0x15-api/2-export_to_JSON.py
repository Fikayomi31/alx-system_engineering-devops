#!/usr/bin/python3
"""script to export data to JSON format
by using data from api
"""

import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/" + employee_id

    response = requests.get(url)
    response = response.json()
    user_name = response.get('username')

    """getting info about todos url"""
    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    """putting it into a csv file"""
    json_content = {employee_id: []}
    for task in tasks:
        json_content[employee_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
                })
    try:
        with open("{}.json".format(employee_id), "w") as file:
            json.dump(json_content, file)

    except Exception as e:
        print(e)
