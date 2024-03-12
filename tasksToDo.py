import time, importme
from models import Task


def run_tasklist():
    print('Running tasklist....')
    time.sleep(1)
    # create an instance of the to do list
    todo = importme.ToDo()
    # create initial data
    task0 = Task('take out trash')
    task1 = Task('do laundry')
    task2 = Task('do dishes')
    task3 = Task('dust the house')
    todo.incomplete_tasks.append(task0)
    todo.incomplete_tasks.append(task1)
    todo.incomplete_tasks.append(task2)
    todo.incomplete_tasks.append(task3)

    # start 'running' the to do list until the user quits
    while True:
        task_choice = input('1 View incomplete tasks:\n2. To view a single task by ID\n3. To create a new task\n4. Mark a task complete\n5. View completed tasks\n6. to delete a task\nor Type or type "quit" to quit \n')
        if task_choice == '1':
            print('=' * 50)
            todo.view_tasks()
            print('=' * 50)
            time.sleep(1)
        elif task_choice == '2':
            print('=' * 50)
            todo.view_task()
            print('=' * 50)
            time.sleep(2)
        elif task_choice == '3':
            print('=' * 50)
            todo.add_task()
            print('=' * 50)
            time.sleep(2)
        elif task_choice == '4':
            print('=' * 50)
            todo.finished_tasks()
            print('=' * 50)
            time.sleep(2)
        elif task_choice == '5':
            print('=' * 50)
            todo.view_completed_tasks()
            print('=' * 50)
            time.sleep(2)
        elif task_choice == '6':
            print('=' * 50)
            todo.delete_task()
            print('=' * 50)
            time.sleep(2)
        elif task_choice == 'quit':
            break


run_tasklist()
