#!/usr/bin/python3
""" Use requests and json to get and transform user and todo data from
jsonplaceholder into a json file
"""
import json
import requests
from sys import argv

if len(argv) != 2:
    print("user_id required!")
    exit()
employeeURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}"
todoURL = f"http://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
employee = requests.get(employeeURL).json()
todo = requests.get(todoURL).json()
employee_username = employee.get('username')

user_tasks = []
for task in todo:
    user_tasks.append({"task": task.get('title'),
                       "completed": task.get('completed'),
                       "username": employee_username})
user_and_tasks = {str(employee.get('id')): user_tasks}

with open(f"{argv[1]}.json", "w") as jsonfile:
    json.dump(user_and_tasks, jsonfile)
