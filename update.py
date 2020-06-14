from utils import Todo

todo = Todo()
document_name = input('Select a document ')

while len(document_name) < 1:
    print('Must select a document ')
    document_name = input('Select a document ')
else:
    todo.update_task(document_name)