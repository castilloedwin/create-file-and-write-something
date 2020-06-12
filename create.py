from utils import Todo

todo = Todo()
task_name = input('What is the task name? ')

while len(task_name) < 1:
    print('To create the task, it is necessary you put any name')
    task_name = input('What is the task name? ')
else:
    todo.create_task(task_name)