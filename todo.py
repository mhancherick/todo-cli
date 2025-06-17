import argparse, datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, date, description=None, priority, completed):
        self.tasks.append(Task(name, date, description, priority, completed))



class Task:
    def __init__(self, name, date=datetime.date.today(), description=None, priority=5, completed=False):
        self.name = name
        self.date = date
        self.description = description
        self.priority = priority
        self.completed = completed