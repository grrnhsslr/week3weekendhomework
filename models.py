class Task:
    task_counter = 0

    def __init__(self, task):
        self.task_id = Task.task_counter
        Task.task_counter += 1
        self.task = task

    def __str__(self):
        return self.task

    def __repr__(self):
        return f'<task {self.task}>'
