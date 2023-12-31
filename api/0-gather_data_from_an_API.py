#!/usr/bin/python3
""" Use requests and json to get and deserialize data from jsonplaceholder """
import requests
from sys import argv

if len(argv) != 2:
    print("user_id required!")
    exit()
employeeURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}"
todoURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
employee = requests.get(employeeURL).json()
todo = requests.get(todoURL).json()


total_tasks = 0
finished_tasks = 0
finished_task_text = []
for task in todo:
    total_tasks += 1
    if task.get('completed') is True:
        finished_task_text.append(task.get('title'))
        finished_tasks += 1

print("Employee {} is done with tasks({}/{}):"
      .format(employee.get('name'), finished_tasks, total_tasks))

for task in finished_task_text:
    print(f"\t {task}")
