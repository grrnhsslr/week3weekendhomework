# Task Class
# Implement a Task class to represent individual tasks.
# Each task should have a unique ID, a description, and a completion status
# Include a method to display the task in a user-friendly format.
# To-Do List Class
# Implement a ToDoList class to manage a list of tasks.
# Include methods for adding tasks, viewing tasks, editing task completion status, deleting tasks, and retrieving tasks by ID.
# User Interactions
# Create a simple user interface for the To-Do List Manager using a loop.
# Provide options for users to:
# Add a new task.
# View all tasks.
# Edit the completion status of a task.
# Delete a task.
# Quit the manager.
# Implement appropriate data validation to handle user input and prevent errors.
import time
from models import Task


class ToDo:
    def __init__(self):
        self.incomplete_tasks = []
        self.completed_tasks = []

    def __get_task_from_id(self):
        task_id = input('What is your task id?')
        while not task_id.isdigit():
            task_id = 'Invalid task id? ID must be an integer'
        for task in self.incomplete_tasks:
            if task.task_id == int(task_id):
                return task
        print('Task Does not exist')

    def add_task(self):
        task_create = input("Would you like to create a new task? (y/n): ")
        while task_create in {t.task for t in self.incomplete_tasks}:
            print('Task already exists')
            task_create = input("Enter a different task")
        task_create = input("Enter the task ")
        new_task = Task(task_create)
        self.incomplete_tasks.append(new_task)
        print(f'Task {new_task} has been created')
        time.sleep(1)

    def view_tasks(self):
        if self.incomplete_tasks:
            for task in self.incomplete_tasks:
                print(task)
        else:
            print('No tasks available. Nice!')

    def view_task(self):
        # get the task from the private method
        task = self.__get_task_from_id()
        # check if task exists
        if task:
            print(task)

    def delete_task(self):
        task = self.__get_task_from_id()
        if task:
            print(task)
            # asks for confirmation
            are_you_sure = input("Are you sure you want to remove this task? Enter y for yes, or n for no ").lower()
            if are_you_sure == 'y' or are_you_sure == 'yes':
                # remove task from the task list
                self.incomplete_tasks.remove(task)
                print(f'Task {task} has been removed')
                time.sleep(1.5)
            elif are_you_sure == 'n' or are_you_sure == 'no':
                print('Task deletion cancelled. Returning to menu')
                time.sleep(1.5)

    def finished_tasks(self):
        task = self.__get_task_from_id()
        if task:
            print(task)
            complete = input("Do you want to mark this task as completed? Enter y for yes, or n for no ").lower()
            if complete == 'y' or complete == 'yes':
                print(f'Marking task {complete} as completed')
                self.completed_tasks.append(task)
                self.incomplete_tasks.remove(task)

    def view_completed_tasks(self):
        if self.completed_tasks:
            for task in self.completed_tasks:
                print(task)
        else:
            print('No tasks completed yet')
