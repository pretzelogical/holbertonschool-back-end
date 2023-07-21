#!/usr/bin/python3
""" Use requests and json to get and transform user and todo data from
jsonplaceholder into a json file
"""
import requests
import json

employeeURL = f"http://jsonplaceholder.typicode.com/users/"
todoURL = f"http://jsonplaceholder.typicode.com/todos"
employee = requests.get(employeeURL).json()
todo = requests.get(todoURL).json()
id_to_username = {emp.get('id'): emp.get('username') for emp in employee}

all_users_tasks = {}
for emp in employee:
    users_tasks = []
    for task in todo:
        userID = emp.get('id')
        username = id_to_username.get(userID)
        if task.get('userId') == userID:
            users_tasks.append({"username": username,
                                "task": task.get('title'),
                                "completed": task.get('completed')})
    all_users_tasks.update({str(emp.get('id')): users_tasks})

with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_users_tasks, jsonfile)
