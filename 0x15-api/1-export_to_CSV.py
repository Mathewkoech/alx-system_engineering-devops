#!/usr/bin/python3
"""
Python script for fetching todo list of employees REST API
"""
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'
    url = base_url + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, task.get('completed'),
                               task.get('title')))
