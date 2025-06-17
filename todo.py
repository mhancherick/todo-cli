import argparse, datetime

class ToDoList:
    def __init__(self):
        self.tasks = []


class Task:
    def __init__(self, task_name, task_date=datetime.date.today(), task_description=None, task_priority=5):
        self.task_name = task_name
        self.task_date = task_date
        self.task_description = task_description
        self.task_priority = task_priority