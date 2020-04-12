from pathlib import Path
import time
from datetime import date

class Todo:
    def path(self, doc_name):
        path = Path(f'{doc_name}.txt')
        return path

    def generate_task_id(self, doc_name):
        path = self.path(doc_name)
        with path.open() as f:
            return len(f.readlines()) + 1

    def create_document(self, doc_name):
        path = self.path(doc_name)
        path.write_text('')
        return path

    # This method verify if there is content into a file
    def is_there_content(self, text):

        if len(text):
            return f'{text}\n'

        return ''

    def create_task(self, task_name):
        doc_name = input('What is the document name where you want to type this task? ')
        path = self.path(doc_name)

        if path.exists():
            _id = self.generate_task_id(doc_name)
            
            read_text = self.is_there_content( path.read_text() )

            new_content = f'{read_text}{_id} - {task_name} - {date.today()} at {time.time()}'
            path.write_text(new_content)
            print('The task has been created')
        else:
            create_document = input('The document name does not exist, do you want yo create it? (Y/n) ')
            if create_document.upper() == 'Y' or len(create_document) == 0:
                self.create_document(doc_name).write_text(f'{1} - {task_name} - {date.today()} at {time.time()}')
                print('The task has been created')

    def read_document(self, doc_name):
        path = self.path(doc_name)
        
        if not path.exists():
            print('This document does not exist')
            return False
        else:
            print(path.read_text())
            return True

    def delete_task(self, doc_name):
        if self.read_document(doc_name):
            path = self.path(doc_name)
            task_id = input('Which do these tasks you want to remove? ')

            # This variable saves in memory the tasks to be able having id into dictionary
            memory_tasks = {}

            with path.open() as f:
                for fl in f.readlines():
                    _id = fl.split('-')[0].replace(' ', '')
                    memory_tasks[_id] = fl

            if task_id in memory_tasks:
                memory_tasks.pop(task_id)

                new_content = ''
                for task in memory_tasks:
                    new_content += memory_tasks[task]

                print(new_content)
                path.write_text(new_content)
                print('Task has been deleted')

            else:
                print('Task you want to remove does not exist')