#!/usr/bin/python3
""" Use requests and json to get and transform user and todo data from
jsonplaceholder into csv
"""
import csv
import requests
from sys import argv

if len(argv) != 2:
    print("user_id required!")
    exit()
employeeURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}"
todoURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
employee = requests.get(employeeURL).json()
todo = requests.get(todoURL).json()

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
