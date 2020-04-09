from utils import Todo

todo = Todo()
task_name = input('What is the task name? ')

if not len(task_name):
    print('To create the task, it is necessary you put any name')
else:
    todo.create_task(task_name)