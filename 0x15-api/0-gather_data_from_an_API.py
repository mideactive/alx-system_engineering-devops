#!/usr/bin/python3
"""
Module to gather data from an API for a given employee ID.
"""

import requests
import sys


def gather_data(employee_id):
    """
    Gather data from the API for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee name,
        number of completed tasks,
        total number of tasks, and a list of completed task titles.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get("completed")]

    return (employee_name, len(done_tasks), total_tasks,
            [task.get("title") for task in done_tasks])


def display_data(employee_id):
    """
    Display the employee TODO list progress in the specified format.

    Args:
        employee_id (int): The ID of the employee.
    """
    emp_name, done_tasks, total_tasks, task_titles = gather_data(employee_id)

    print(f"Employee {emp_name} is done with\
            tasks({done_tasks}/{total_tasks}):")
    for title in task_titles:
        print("\t", title)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py\
                <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        display_data(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide an integer value.")
        sys.exit(1)
