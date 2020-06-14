from pathlib import Path
import datetime
from alert import Alert

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
        doc_name = input(Alert().messages['document_name'])
        path = self.path(doc_name)

        if path.exists():
            _id = self.generate_task_id(doc_name)
            read_text = self.is_there_content( path.read_text() )
            new_content = f'{read_text}{_id} - {task_name} - {datetime.datetime.now()}'
            path.write_text(new_content)
            
            print(Alert().messages['task_created'])
        else:
            create_document = input(Alert().messages['do_you_wanna_create_it'])
            if create_document.upper() == 'Y' or len(create_document) == 0:
                self.create_document(doc_name).write_text(f'{1} - {task_name} - {datetime.datetime.now()}')
                print(Alert().messages['task_created'])

    def read_document(self, doc_name):
        path = self.path(doc_name)
        
        if not path.exists():
            print(Alert().messages['document_does_not_exist'])
            return False
        else:
            print(path.read_text())
            return True

    def update_task(self, doc_name):
        if self.read_document(doc_name):
            path = self.path(doc_name)
            task_id = input(Alert().messages['task_id']) # It's neccesary to select a task id

            with path.open() as f:
                memory_tasks = { f"{fl.split('-')[0].strip()}": fl for fl in f.readlines() }

            if task_id in memory_tasks:
                task = memory_tasks.get(str(task_id))
                word = input('What word do you wanna change? ')
                new_word = input('What is the new word? ')
                
                memory_tasks[str(task_id)] = task.replace(word, new_word)

                new_content = ''
                for mt in memory_tasks:
                    new_content += memory_tasks[mt]

                path.write_text(new_content)
                print('Task has beed updated successfuly')
            else:
                print('Task you want to update does not exist')

    def delete_task(self, doc_name):
        if self.read_document(doc_name):
            path = self.path(doc_name)
            task_id = input(Alert().messages['task_id']) # It's neccesary to select a task id

            with path.open() as f:
                memory_tasks = { f"{fl.split('-')[0].strip()}": fl for fl in f.readlines() }

            if task_id in memory_tasks:
                memory_tasks.pop(task_id)

                new_content = ''
                for task in memory_tasks:
                    new_content += memory_tasks[task]

                path.write_text(new_content)
                print(Alert().messages['task_deleted'])
            else:
                print(Alert().messages['task_no'])