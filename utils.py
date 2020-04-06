from pathlib import Path
import time
from datetime import date

class Todo:
    def create_document(self, doc_name):
        path = Path(f'{doc_name}.txt')
        path.write_text('')
        return path

    def create_task(self, task_name):
        doc_name = input('What is the document name where you want to type this task? ')
        path = Path(doc_name)

        if path.exists():
            new_content = f'{path.read_text()}\n{task_name} - {date.today()} at {time.time()}'
            path.write_text(new_content)
        else:
            create_document = input('The document name does not exist, do you want yo create it? (Y/n) ')
            if create_document.upper() == 'Y':
                self.create_document(doc_name).write_text(f'{task_name} - {date.today()} at {time.time()}')