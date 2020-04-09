from utils import Todo

todo = Todo()

document_name = input('Select a document ')

if not len(document_name):
    print('Must select a document ')
else:
    todo.delete_task(document_name)