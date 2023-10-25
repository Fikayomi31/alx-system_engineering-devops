#!/usr/bin/python3
"""script to export data in the CSV format
by using data from api
"""

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
    try:
        with open("{}.csv".format(employee_id), "w") as file:
            for task in tasks:
                """writing it into csv file"""
                file.write('"{}","{}","{}","{}"\n'
                           .format(employee_id, user_name,
                                   task.get('completed'),
                                   task.get('title')))
    except Exception as e:
        print(e)
