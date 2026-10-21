"""
Simple command-line To-Do List
Usage:
    python todo.py add Buy groceries
    python todo.py list
"""
import json
import os
import sys

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['text']}")


def complete_task(number):
    tasks = load_tasks()
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print(f"Completed: {tasks[number - 1]['text']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py add <task> | list")
        sys.exit()

    command = sys.argv[1]
    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        complete_task(int(sys.argv[2]))
    else:
        print("Unknown command")
