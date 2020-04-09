from utils import Todo

todo = Todo()
document_name = input('What is the document you want to read? ')

if not len(document_name):
    print('To read a document you need to type any name')
else:
    todo.read_document(document_name)