#!/usr/bin/python3
""" Use requests and json to get and transform data from jsonplaceholder 
into csv
"""

import requests
from sys import argv
import csv

if not argv[1]:
    exit()
employeeURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}"
todoURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
employeeREQ = requests.get(employeeURL)
todoREQ = requests.get(todoURL)
employee = employeeREQ.json()
todo = todoREQ.json()

tasks = []
for task in todo:
    tasks.append({'USER_ID': employee.get('id'),
                  'USERNAME': employee.get('username'),
                  'TASK_COMPLETED_STATUS': str(task.get('completed')),
                  'TASK_TITLE': task.get('title')})

with open(f'{argv[1]}.csv', 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(
        csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writerows(tasks)
