#!/usr/bin/python3
""" Use requests and json to get and deserialize data from jsonplaceholder """

import requests
import sys

employeeID = sys.argv[1]
employeeURL = f"http://jsonplaceholder.typicode.com/users/{employeeID}"
todoURL = f"http://jsonplaceholder.typicode.com/users/{employeeID}/todos"
employeeREQ = requests.get(employeeURL)
todoREQ = requests.get(todoURL)
employee = employeeREQ.json()
todo = todoREQ.json()

total_tasks = 0
finished_tasks = 0
finished_task_text = []
for task in todo:
    total_tasks += 1
    if task.get('completed') is True:
        finished_task_text.append(task.get('title'))
        finished_tasks += 1

print("Employee {} is done with tasks({}/{})"
      .format(employee.get('name'), finished_tasks, total_tasks))

for task in finished_task_text:
    print(f"\t {task}")
